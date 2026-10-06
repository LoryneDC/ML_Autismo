import requests
import json

# URL de la API (ajusta según tu configuración)
API_URL = "http://localhost:8000"

def test_health():
    """Prueba el endpoint de health check"""
    print("=== Test Health Check ===")
    response = requests.get(f"{API_URL}/health")
    print(f"Status: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")
    print()

def test_features_info():
    """Prueba el endpoint de información de features"""
    print("=== Test Features Info ===")
    response = requests.get(f"{API_URL}/features/info")
    print(f"Status: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")
    print()

def test_prediction_no_asd():
    """Prueba predicción para un caso sin autismo"""
    print("=== Test Prediction (No ASD) ===")
    
    # Datos de ejemplo basados en el dataset
    data = {
        "A1_Score": 0,
        "A2_Score": 0,
        "A3_Score": 0,
        "A4_Score": 0,
        "A5_Score": 0,
        "A6_Score": 0,
        "A7_Score": 0,
        "A8_Score": 0,
        "A9_Score": 0,
        "A10_Score": 0,
        "age": 47,
        "gender": "m",
        "ethnicity": "?",
        "jaundice": "no",
        "austim": "no",
        "contry_of_res": "India",
        "used_app_before": "no",
        "result": 2.26,
        "relation": "Self"
    }
    
    response = requests.post(f"{API_URL}/predict", json=data)
    print(f"Status: {response.status_code}")
    print(f"Input: {json.dumps(data, indent=2)}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")
    print()

def test_prediction_with_asd():
    """Prueba predicción para un caso con autismo"""
    print("=== Test Prediction (ASD) ===")
    
    # Datos de ejemplo con múltiples scores positivos
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
    
    response = requests.post(f"{API_URL}/predict", json=data)
    print(f"Status: {response.status_code}")
    print(f"Input: {json.dumps(data, indent=2)}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")
    print()

def test_prediction_mixed():
    """Prueba predicción para un caso mixto"""
    print("=== Test Prediction (Mixed) ===")
    
    data = {
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
        "ethnicity": "?",
        "jaundice": "no",
        "austim": "no",
        "contry_of_res": "Austria",
        "used_app_before": "no",
        "result": 6.35,
        "relation": "Self"
    }
    
    response = requests.post(f"{API_URL}/predict", json=data)
    print(f"Status: {response.status_code}")
    print(f"Input: {json.dumps(data, indent=2)}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")
    print()

def test_invalid_data():
    """Prueba con datos inválidos"""
    print("=== Test Invalid Data ===")
    
    # Edad fuera de rango
    data = {
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
        "age": 150,  # Edad inválida
        "gender": "f",
        "ethnicity": "?",
        "jaundice": "no",
        "austim": "no",
        "contry_of_res": "Austria",
        "used_app_before": "no",
        "result": 6.35,
        "relation": "Self"
    }
    
    response = requests.post(f"{API_URL}/predict", json=data)
    print(f"Status: {response.status_code}")
    print(f"Response: {response.text}")
    print()

if __name__ == "__main__":
    try:
        print("🧪 Iniciando pruebas de la API de Predicción de Autismo\n")
        print("="*60)
        print()
        
        # Ejecutar pruebas
        test_health()
        test_features_info()
        test_prediction_no_asd()
        test_prediction_with_asd()
        test_prediction_mixed()
        test_invalid_data()
        
        print("="*60)
        print("✅ Pruebas completadas")
        
    except requests.exceptions.ConnectionError:
        print("❌ Error: No se pudo conectar a la API.")
        print("Por favor, asegúrate de que la API esté ejecutándose en http://localhost:8000")
        print("Ejecuta: uvicorn api:app --reload")
    except Exception as e:
        print(f"❌ Error inesperado: {e}")
