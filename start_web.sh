#!/bin/bash

# Script para iniciar la aplicación web
# Autor: ASD Predictor Team

set -e

echo "🌐 Iniciando Aplicación Web ASD Predictor..."
echo ""

# Colores
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Verificar que existe el directorio web
if [ ! -d "web" ]; then
    echo -e "${YELLOW}⚠ Directorio web no encontrado${NC}"
    exit 1
fi

# Función para verificar si la API está corriendo
check_api() {
    if curl -s http://localhost:8000/health > /dev/null 2>&1; then
        return 0
    else
        return 1
    fi
}

# Verificar API
echo -e "${BLUE}📡 Verificando API...${NC}"
if check_api; then
    echo -e "${GREEN}✓ API está corriendo en http://localhost:8000${NC}"
else
    echo -e "${YELLOW}⚠ API no detectada${NC}"
    echo ""
    read -p "¿Desea iniciar la API ahora? (s/n): " -n 1 -r
    echo
    if [[ $REPLY =~ ^[Ss]$ ]]; then
        echo -e "${BLUE}🚀 Iniciando API...${NC}"
        ./start.sh &
        API_PID=$!
        echo -e "${GREEN}✓ API iniciada (PID: $API_PID)${NC}"
        sleep 3
    else
        echo -e "${YELLOW}⚠ Continuando sin API. La aplicación web puede no funcionar correctamente.${NC}"
    fi
fi

echo ""
echo -e "${GREEN}════════════════════════════════════════════${NC}"
echo -e "${GREEN}  ASD Predictor - Aplicación Web${NC}"
echo -e "${GREEN}════════════════════════════════════════════${NC}"
echo ""
echo -e "  🌐 URL Local: ${BLUE}http://localhost:8080${NC}"
echo -e "  📡 API Backend: ${BLUE}http://localhost:8000${NC}"
echo ""
echo -e "${GREEN}════════════════════════════════════════════${NC}"
echo ""
echo -e "${YELLOW}Presiona Ctrl+C para detener el servidor${NC}"
echo ""

# Cambiar al directorio web e iniciar servidor
cd web
python3 -m http.server 8080
