#  Índice de Documentación - API de Predicción de Autismo

Guía rápida para navegar por toda la documentación del proyecto.

---

##  Para Empezar (Nuevo Usuario)

1. **[QUICK_START.md](./QUICK_START.md)** 
   - Guía de inicio rápido
   - Cómo ejecutar la API en 5 minutos
   - Ejemplos básicos de uso

2. **[README.md](./README.md)**
   - Documentación completa
   - Instalación detallada
   - Referencia de la API

---

##  Para Desarrolladores

### Archivos de Código

- **[api.py](./api.py)** - Código principal de la API
- **[test_api.py](./test_api.py)** - Suite de pruebas
- **[start.sh](./start.sh)** - Script de inicio automatizado

### Configuración

- **[requirements.txt](./requirements.txt)** - Dependencias Python
- **[.env.example](./.env.example)** - Variables de entorno ejemplo

---

##  Documentación

### Guías de Usuario

1. **[QUICK_START.md](./QUICK_START.md)** - Inicio rápido 
2. **[README.md](./README.md)** - Documentación completa 
3. **[API_EXAMPLES.md](./API_EXAMPLES.md)** - Ejemplos de código 

### Documentación Técnica

4. **[PROJECT_SUMMARY.md](./PROJECT_SUMMARY.md)** - Resumen del proyecto 

### Herramientas

5. **[Autism_Prediction_API.postman_collection.json](./Autism_Prediction_API.postman_collection.json)** - Colección Postman 

---

##  Por Caso de Uso

### "Quiero ejecutar la API rápidamente"
→ **[QUICK_START.md](./QUICK_START.md)**

### "Necesito integrar la API en mi aplicación"
→ **[API_EXAMPLES.md](./API_EXAMPLES.md)** + **[README.md](./README.md)**

### "Quiero entender cómo funciona"
→ **[README.md](./README.md)** + **[PROJECT_SUMMARY.md](./PROJECT_SUMMARY.md)**

### "Necesito probar endpoints"
→ **[Postman Collection](./Autism_Prediction_API.postman_collection.json)** o **http://localhost:8000/docs**

### "Quiero modificar el código"
→ **[api.py](./api.py)** + **[test_api.py](./test_api.py)**

---

##  Guía de Lectura Sugerida

### Para Usuarios Finales
1. QUICK_START.md
2. README.md (secciones de uso)
3. Swagger UI (http://localhost:8000/docs)

### Para Desarrolladores Frontend
1. QUICK_START.md
2. API_EXAMPLES.md (busca tu lenguaje)
3. README.md (estructura de datos)
4. Postman Collection (para pruebas)

### Para Desarrolladores Backend
1. PROJECT_SUMMARY.md
2. README.md (completo)
3. api.py (código fuente)
4. test_api.py (tests)

### Para DevOps / SysAdmin
1. README.md (instalación)
2. requirements.txt
3. .env.example
4. start.sh

---

##  Enlaces Rápidos (cuando el servidor está corriendo)

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc
- **API Info**: http://localhost:8000/
- **Health Check**: http://localhost:8000/health
- **Features Info**: http://localhost:8000/features/info

---

##  Estructura del Proyecto

```
ML-project/
│
├──  Archivos de Código
│   ├── api.py                              # API principal
│   ├── test_api.py                         # Tests
│   └── start.sh                            # Script de inicio
│
├──  Documentación
│   ├── INDEX.md                            # Este archivo
│   ├── QUICK_START.md                      # Inicio rápido
│   ├── README.md                           # Documentación completa
│   ├── API_EXAMPLES.md                     # Ejemplos de código
│   └── PROJECT_SUMMARY.md                  # Resumen del proyecto
│
├──  Configuración
│   ├── requirements.txt                    # Dependencias
│   ├── .env.example                        # Variables de entorno
│   └── Autism_Prediction_API.postman_collection.json
│
├──  Modelo de ML
│   ├── best_model.pkl                      # Modelo entrenado
│   ├── encoders.pkl                        # Encoders
│   └── Autism_Preidiction_using_machine_Learning.ipynb
│
├──  Datos
│   └── train.csv                           # Dataset de entrenamiento
│
└──  Otros
    └── .venv/                              # Entorno virtual
```

---

##  FAQ Rápido

### ¿Cómo inicio la API?
```bash
./start.sh
```

### ¿Cómo pruebo la API?
```bash
python test_api.py
```
O visita: http://localhost:8000/docs

### ¿Dónde veo ejemplos de código?
**[API_EXAMPLES.md](./API_EXAMPLES.md)**

### ¿Cómo cambio el puerto?
```bash
uvicorn api:app --port 8001
```

### ¿Dónde está la documentación completa?
**[README.md](./README.md)**

---

##  Recursos de Aprendizaje

### FastAPI
- Documentación oficial: https://fastapi.tiangolo.com/
- Tutorial: https://fastapi.tiangolo.com/tutorial/

### Machine Learning
- Scikit-learn: https://scikit-learn.org/
- Modelo usado: RandomForestClassifier

### Python
- Python.org: https://www.python.org/
- Virtual Environments: https://docs.python.org/3/tutorial/venv.html

---

##  Soporte

Si tienes problemas:
1. Revisa **[README.md](./README.md)** (sección Troubleshooting)
2. Verifica que el servidor esté corriendo
3. Ejecuta los tests: `python test_api.py`
4. Revisa los logs en la consola

---

**Última actualización**: 2025-11-20
**Versión de la API**: 1.0.0
