from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field, validator
import pickle
import numpy as np
from typing import Literal, Optional
import logging

# Configuración de logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Inicializar FastAPI
app = FastAPI(
    title="Autism Prediction API",
    description="API para predicción de autismo usando machine learning",
    version="1.0.0"
)

# Configurar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Cargar modelo y encoders
try:
    with open("best_model.pkl", "rb") as f:
        model = pickle.load(f)
    logger.info("Modelo cargado exitosamente")
    
    with open("encoders.pkl", "rb") as f:
        encoders = pickle.load(f)
    logger.info("Encoders cargados exitosamente")
except FileNotFoundError as e:
    logger.error(f"Error al cargar archivos: {e}")
    raise
except Exception as e:
    logger.error(f"Error inesperado: {e}")
    raise

# Modelo de datos de entrada
class AutismInput(BaseModel):
    """
    Estructura de datos de entrada para la predicción de autismo.
    Basado en el dataset de entrenamiento del modelo.
    """
    # Scores A1-A10 (respuestas a preguntas del cuestionario)
    A1_Score: int = Field(..., ge=0, le=1, description="Respuesta a pregunta A1 (0 o 1)")
    A2_Score: int = Field(..., ge=0, le=1, description="Respuesta a pregunta A2 (0 o 1)")
    A3_Score: int = Field(..., ge=0, le=1, description="Respuesta a pregunta A3 (0 o 1)")
    A4_Score: int = Field(..., ge=0, le=1, description="Respuesta a pregunta A4 (0 o 1)")
    A5_Score: int = Field(..., ge=0, le=1, description="Respuesta a pregunta A5 (0 o 1)")
    A6_Score: int = Field(..., ge=0, le=1, description="Respuesta a pregunta A6 (0 o 1)")
    A7_Score: int = Field(..., ge=0, le=1, description="Respuesta a pregunta A7 (0 o 1)")
    A8_Score: int = Field(..., ge=0, le=1, description="Respuesta a pregunta A8 (0 o 1)")
    A9_Score: int = Field(..., ge=0, le=1, description="Respuesta a pregunta A9 (0 o 1)")
    A10_Score: int = Field(..., ge=0, le=1, description="Respuesta a pregunta A10 (0 o 1)")
    
    # Información demográfica
    age: int = Field(..., ge=1, le=120, description="Edad del individuo")
    gender: Literal["m", "f"] = Field(..., description="Género (m: masculino, f: femenino)")
    ethnicity: str = Field(..., description="Etnicidad (ej: White-European, Hispanic, Asian, etc.)")
    jaundice: Literal["yes", "no"] = Field(..., description="¿Nació con ictericia?")
    austim: Literal["yes", "no"] = Field(..., description="¿Algún familiar tiene autismo?")
    contry_of_res: str = Field(..., description="País de residencia")
    used_app_before: Literal["yes", "no"] = Field(..., description="¿Ha usado la app antes?")
    result: float = Field(..., description="Resultado/score del test")
    relation: str = Field(..., description="Relación con el individuo (ej: Self, Parent, Relative, etc.)")
    
    class Config:
        schema_extra = {
            "example": {
                "A1_Score": 1,
                "A2_Score": 0,
                "A3_Score": 1,
                "A4_Score": 0,
                "A5_Score": 1,
                "A6_Score": 0,
                "A7_Score": 1,
                "A8_Score": 0,
                "A9_Score": 1,
                "A10_Score": 1,
                "age": 38,
                "gender": "f",
                "ethnicity": "White-European",
                "jaundice": "no",
                "austim": "no",
                "contry_of_res": "United States",
                "used_app_before": "no",
                "result": 6.35,
                "relation": "Self"
            }
        }

# Modelo de respuesta
class PredictionResponse(BaseModel):
    """Respuesta de la predicción"""
    prediction: int = Field(..., description="Predicción: 0 (No ASD) o 1 (ASD)")
    prediction_label: str = Field(..., description="Etiqueta de la predicción")
    probability: Optional[float] = Field(None, description="Probabilidad de la clase predicha (si está disponible)")
    
    class Config:
        schema_extra = {
            "example": {
                "prediction": 0,
                "prediction_label": "No ASD",
                "probability": 0.85
            }
        }

class HealthResponse(BaseModel):
    """Respuesta del health check"""
    status: str
    model_loaded: bool
    encoders_loaded: bool

def encode_categorical_features(data: AutismInput) -> dict:
    """
    Codifica las características categóricas usando los encoders guardados.
    """
    encoded_data = {}
    
    # Características categóricas que necesitan encoding
    categorical_features = {
        'gender': data.gender,
        'ethnicity': data.ethnicity,
        'jaundice': data.jaundice,
        'austim': data.austim,
        'contry_of_res': data.contry_of_res,
        'used_app_before': data.used_app_before,
        'relation': data.relation
    }
    
    for feature_name, value in categorical_features.items():
        encoder = encoders.get(feature_name)
        if encoder is None:
            raise ValueError(f"No se encontró encoder para {feature_name}")
        
        try:
            # Verificar si el valor está en las clases conocidas
            if value not in encoder.classes_:
                # Si no está, usar la primera clase como fallback o lanzar error
                logger.warning(f"Valor desconocido '{value}' para {feature_name}. Valores conocidos: {encoder.classes_}")
                # Usar '?' o el primer valor conocido como fallback
                if '?' in encoder.classes_:
                    value = '?'
                else:
                    # Usar el valor más común (primer elemento)
                    value = encoder.classes_[0]
                logger.warning(f"Usando valor por defecto: {value}")
            
            encoded_data[feature_name] = encoder.transform([value])[0]
        except Exception as e:
            logger.error(f"Error al codificar {feature_name}: {e}")
            raise ValueError(f"Error al codificar {feature_name}: {str(e)}")
    
    return encoded_data

@app.get("/", tags=["General"])
async def root():
    """Endpoint raíz de la API"""
    return {
        "message": "API de Predicción de Autismo",
        "version": "1.0.0",
        "endpoints": {
            "health": "/health",
            "predict": "/predict (POST)",
            "docs": "/docs"
        }
    }

@app.get("/health", response_model=HealthResponse, tags=["General"])
async def health_check():
    """Verifica el estado de la API y los modelos cargados"""
    return HealthResponse(
        status="healthy",
        model_loaded=model is not None,
        encoders_loaded=encoders is not None and len(encoders) > 0
    )

@app.post("/predict", response_model=PredictionResponse, tags=["Prediction"])
async def predict(data: AutismInput):
    """
    Realiza una predicción de autismo basándose en los datos de entrada.
    
    Retorna:
    - prediction: 0 (No ASD) o 1 (ASD)
    - prediction_label: Etiqueta legible de la predicción
    - probability: Probabilidad de la clase predicha (si está disponible)
    """
    try:
        # Codificar características categóricas
        encoded_categorical = encode_categorical_features(data)
        
        # Preparar el array de características en el orden correcto
        # Orden: A1-A10, age, gender, ethnicity, jaundice, austim, contry_of_res, used_app_before, result, relation
        features = np.array([[
            data.A1_Score,
            data.A2_Score,
            data.A3_Score,
            data.A4_Score,
            data.A5_Score,
            data.A6_Score,
            data.A7_Score,
            data.A8_Score,
            data.A9_Score,
            data.A10_Score,
            float(data.age),
            encoded_categorical['gender'],
            encoded_categorical['ethnicity'],
            encoded_categorical['jaundice'],
            encoded_categorical['austim'],
            encoded_categorical['contry_of_res'],
            encoded_categorical['used_app_before'],
            data.result,
            encoded_categorical['relation']
        ]])
        
        # Realizar predicción
        prediction = model.predict(features)[0]
        
        # Obtener probabilidad si el modelo lo soporta
        probability = None
        if hasattr(model, 'predict_proba'):
            probabilities = model.predict_proba(features)[0]
            probability = float(probabilities[prediction])
        
        # Crear etiqueta legible
        prediction_label = "ASD" if prediction == 1 else "No ASD"
        
        logger.info(f"Predicción exitosa: {prediction_label}")
        
        return PredictionResponse(
            prediction=int(prediction),
            prediction_label=prediction_label,
            probability=probability
        )
        
    except ValueError as e:
        logger.error(f"Error de validación: {e}")
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        logger.error(f"Error en la predicción: {e}")
        raise HTTPException(status_code=500, detail=f"Error en la predicción: {str(e)}")

@app.get("/features/info", tags=["Information"])
async def get_features_info():
    """
    Retorna información sobre las características esperadas y los valores válidos.
    """
    features_info = {
        "scores": {
            "A1_Score - A10_Score": "Valores binarios (0 o 1) representando respuestas a preguntas del cuestionario"
        },
        "demographic": {
            "age": "Edad del individuo (1-120)",
            "gender": ["m", "f"],
            "ethnicity": list(encoders['ethnicity'].classes_),
            "jaundice": ["yes", "no"],
            "austim": ["yes", "no"],
            "contry_of_res": list(encoders['contry_of_res'].classes_),
            "used_app_before": ["yes", "no"],
            "relation": list(encoders['relation'].classes_)
        },
        "other": {
            "result": "Valor numérico representando el resultado/score del test"
        }
    }
    
    return features_info

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
