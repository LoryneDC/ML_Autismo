# API de Predicción de Autismo 🧠

API REST construida con FastAPI para realizar predicciones de autismo (ASD - Autism Spectrum Disorder) utilizando un modelo de Machine Learning entrenado con RandomForestClassifier.

## 📋 Descripción

Esta API consume un modelo de Machine Learning entrenado en el dataset de predicción de autismo y proporciona endpoints para realizar predicciones basadas en características demográficas y respuestas a cuestionarios.

## 🚀 Características

- ✅ **Predicción de ASD**: Predice la probabilidad de autismo basándose en 19 características
- ✅ **Validación de datos**: Validación automática de tipos y rangos de datos de entrada
- ✅ **Manejo de errores**: Mensajes de error descriptivos y logging detallado
- ✅ **Documentación interactiva**: Swagger UI y ReDoc incluidos
- ✅ **Health check**: Endpoint para verificar el estado de la API
- ✅ **CORS habilitado**: Permite llamadas desde diferentes orígenes

## 📦 Instalación

### 1. Crear entorno virtual (recomendado)

```bash
python -m venv .venv
source .venv/bin/activate  # En Linux/Mac
# o
.venv\Scripts\activate  # En Windows
```

### 2. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 3. Verificar archivos necesarios

Asegúrate de tener estos archivos en el directorio:
- `best_model.pkl` - Modelo entrenado
- `encoders.pkl` - Encoders para variables categóricas
- `api.py` - Código de la API

## 🏃 Ejecución

### Iniciar el servidor

```bash
uvicorn api:app --reload
```

La API estará disponible en: `http://localhost:8000`

### Opciones de ejecución

```bash
# Con host y puerto personalizados
uvicorn api:app --host 0.0.0.0 --port 8080 --reload

# En producción (sin reload)
uvicorn api:app --host 0.0.0.0 --port 8000
```

## 📚 Documentación

Una vez que la API esté ejecutándose, puedes acceder a:

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## 🔌 Endpoints

### 1. Root - GET `/`
Información básica de la API

```bash
curl http://localhost:8000/
```

### 2. Health Check - GET `/health`
Verifica el estado de la API y los modelos cargados

```bash
curl http://localhost:8000/health
```

**Respuesta:**
```json
{
  "status": "healthy",
  "model_loaded": true,
  "encoders_loaded": true
}
```

### 3. Features Info - GET `/features/info`
Obtiene información sobre las características esperadas

```bash
curl http://localhost:8000/features/info
```

### 4. Predict - POST `/predict`
Realiza una predicción de autismo

**Ejemplo de solicitud:**

```bash
curl -X POST "http://localhost:8000/predict" \
  -H "Content-Type: application/json" \
  -d '{
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
  }'
```

**Respuesta:**
```json
{
  "prediction": 0,
  "prediction_label": "No ASD",
  "probability": 0.85
}
```

## 📊 Estructura de Datos de Entrada

### Campos Obligatorios

| Campo | Tipo | Valores | Descripción |
|-------|------|---------|-------------|
| `A1_Score` - `A10_Score` | int | 0 o 1 | Respuestas al cuestionario |
| `age` | int | 1-120 | Edad del individuo |
| `gender` | string | "m" o "f" | Género |
| `ethnicity` | string | Ver lista* | Etnicidad |
| `jaundice` | string | "yes" o "no" | ¿Nació con ictericia? |
| `austim` | string | "yes" o "no" | ¿Familiar con autismo? |
| `contry_of_res` | string | Ver lista* | País de residencia |
| `used_app_before` | string | "yes" o "no" | ¿Ha usado la app antes? |
| `result` | float | - | Score del test |
| `relation` | string | Ver lista* | Relación con el individuo |

\* Consulta `/features/info` para obtener listas completas de valores válidos

### Valores Comunes

**ethnicity**: `?`, `White-European`, `Hispanic`, `Asian`, `Black`, `South Asian`, `Middle Eastern`, `Others`, etc.

**contry_of_res**: `United States`, `India`, `United Kingdom`, `Canada`, `Australia`, etc.

**relation**: `Self`, `Parent`, `Relative`, `Health care professional`, `Others`, `?`

## 🧪 Pruebas

### Ejecutar script de pruebas

```bash
# Asegúrate de que la API esté ejecutándose primero
python test_api.py
```

El script realizará varias pruebas:
- Health check
- Información de features
- Predicción con diferentes casos
- Validación de datos inválidos

### Prueba manual con Python

```python
import requests

url = "http://localhost:8000/predict"
data = {
    "A1_Score": 1,
    "A2_Score": 1,
    "A3_Score": 1,
    "A4_Score": 1,
    "A5_Score": 1,
    "A6_Score": 1,
    "A7_Score": 1,
    "A8_Score": 1,
    "A9_Score": 1,
    "A10_Score": 1,
    "age": 7,
    "gender": "m",
    "ethnicity": "White-European",
    "jaundice": "no",
    "austim": "yes",
    "contry_of_res": "United States",
    "used_app_before": "no",
    "result": 14.85,
    "relation": "Self"
}

response = requests.post(url, json=data)
print(response.json())
```

## 🔧 Desarrollo

### Estructura del Proyecto

```
ML-project/
├── api.py                  # Código principal de la API
├── best_model.pkl          # Modelo entrenado
├── encoders.pkl            # Encoders para variables categóricas
├── requirements.txt        # Dependencias
├── test_api.py            # Script de pruebas
├── README.md              # Este archivo
└── Autism_Preidiction_using_machine_Learning.ipynb  # Notebook de entrenamiento
```

### Agregar nuevas funcionalidades

Para agregar nuevos endpoints, edita `api.py`:

```python
@app.get("/mi-endpoint")
async def mi_funcion():
    return {"mensaje": "Hola"}
```

## 📈 Modelo

- **Tipo**: RandomForestClassifier
- **Accuracy**: ~93% (cross-validation)
- **Features**: 19 características (10 scores + 9 demográficas)
- **Target**: Clasificación binaria (0: No ASD, 1: ASD)

## ⚠️ Limitaciones

1. **Valores categóricos**: Si se proporciona un valor desconocido para campos categóricos (ethnicity, contry_of_res, relation), la API usará un valor por defecto o retornará un error.

2. **Idioma**: Los valores deben estar en inglés (ej: "United States", no "Estados Unidos")

3. **Versiones**: El modelo fue entrenado con versiones específicas de scikit-learn y otras librerías. Asegúrate de usar las versiones especificadas en `requirements.txt`

## 🐛 Troubleshooting

### Error: "FileNotFoundError"
- Verifica que `best_model.pkl` y `encoders.pkl` estén en el mismo directorio que `api.py`

### Error: "Address already in use"
- El puerto 8000 ya está en uso. Usa otro puerto: `uvicorn api:app --port 8001`

### Error en predicción
- Verifica que todos los campos estén presentes en la solicitud
- Asegúrate de que los valores sean del tipo correcto (int, float, string)
- Consulta `/features/info` para valores válidos

## 📝 Notas Adicionales

- La API incluye logging para facilitar el debugging
- Los logs se muestran en la consola donde se ejecuta uvicorn
- Para producción, considera agregar autenticación y rate limiting

## 🤝 Contribuciones

Si deseas mejorar esta API:
1. Agrega validaciones adicionales
2. Implementa caching para mejorar el rendimiento
3. Agrega autenticación con JWT
4. Implementa versionado de la API
5. Agrega más tests

## 📄 Licencia

Este proyecto es de código abierto y está disponible bajo la licencia MIT.

---

**Desarrollado con ❤️ usando FastAPI y scikit-learn**
