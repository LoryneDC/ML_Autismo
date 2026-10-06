#!/bin/bash

# Script de inicio rápido para la API de Predicción de Autismo
# Autor: API Development Team
# Descripción: Configura el entorno e inicia el servidor API

set -e  # Salir si hay algún error

echo "🚀 Iniciando API de Predicción de Autismo..."
echo ""

# Colores para output
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# Verificar si existe el entorno virtual
if [ ! -d ".venv" ]; then
    echo -e "${YELLOW}⚠ No se encontró el entorno virtual. Creándolo...${NC}"
    python3 -m venv .venv
    echo -e "${GREEN}✓ Entorno virtual creado${NC}"
fi

# Activar entorno virtual
echo -e "${YELLOW}📦 Activando entorno virtual...${NC}"
source .venv/bin/activate

# Verificar si las dependencias están instaladas
echo -e "${YELLOW}📚 Verificando dependencias...${NC}"
pip list | grep -q fastapi || {
    echo -e "${YELLOW}⚠ Instalando dependencias...${NC}"
    pip install --upgrade pip setuptools wheel
    pip install -r requirements.txt
    echo -e "${GREEN}✓ Dependencias instaladas${NC}"
}

# Verificar que existan los archivos del modelo
if [ ! -f "best_model.pkl" ]; then
    echo -e "${RED}❌ Error: No se encontró el archivo best_model.pkl${NC}"
    echo "   Por favor, asegúrate de tener el modelo entrenado en el directorio actual."
    exit 1
fi

if [ ! -f "encoders.pkl" ]; then
    echo -e "${RED}❌ Error: No se encontró el archivo encoders.pkl${NC}"
    echo "   Por favor, asegúrate de tener los encoders en el directorio actual."
    exit 1
fi

echo -e "${GREEN}✓ Archivos del modelo encontrados${NC}"
echo ""

# Obtener configuración del puerto (por defecto 8000)
PORT=${API_PORT:-8000}
HOST=${API_HOST:-0.0.0.0}

echo -e "${GREEN}════════════════════════════════════════════${NC}"
echo -e "${GREEN}  API de Predicción de Autismo${NC}"
echo -e "${GREEN}════════════════════════════════════════════${NC}"
echo ""
echo -e "  🌐 URL: ${YELLOW}http://localhost:$PORT${NC}"
echo -e "  📖 Docs: ${YELLOW}http://localhost:$PORT/docs${NC}"
echo -e "  📚 ReDoc: ${YELLOW}http://localhost:$PORT/redoc${NC}"
echo ""
echo -e "${GREEN}════════════════════════════════════════════${NC}"
echo ""
echo -e "${YELLOW}Presiona Ctrl+C para detener el servidor${NC}"
echo ""

# Iniciar servidor
uvicorn api:app --host "$HOST" --port "$PORT" --reload
