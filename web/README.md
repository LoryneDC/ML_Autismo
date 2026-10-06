#  ASD Predictor - Aplicación Web

Aplicación web moderna para realizar evaluaciones preliminares del Trastorno del Espectro Autista (ASD) utilizando Machine Learning.

## ✨ Características

-  **Diseño Premium**: Interfaz moderna con glassmorphism y gradientes animados
-  **Responsive**: Funciona perfectamente en desktop, tablet y móvil
-  **Rápido**: Predicciones en menos de 1 segundo
-  **Seguro**: Validación de datos del lado del cliente y servidor
-  **Intuitivo**: Formulario paso a paso con retroalimentación visual
-  **Animaciones**: Micro-interacciones y transiciones suaves

##  Inicio Rápido

### Opción 1: Python HTTP Server (Recomendado)

```bash
# Desde el directorio web/
python3 -m http.server 8080
```

Luego abre: `http://localhost:8080`

### Opción 2: Usar el script de inicio

```bash
# Desde el directorio principal
./start_web.sh
```

### Opción 3: Cualquier servidor web

Puedes usar cualquier servidor web local:
- Node.js: `npx serve`
- PHP: `php -S localhost:8080`
- VS Code: Extensión "Live Server"

##  Prerequisitos

1. **API de Backend corriendo**: Asegúrate de que la API esté ejecutándose en `http://localhost:8000`
   ```bash
   cd ..
   ./start.sh
   ```

2. **Navegador moderno**: Chrome, Firefox, Safari o Edge (versiones recientes)

##  Cómo Usar

1. **Abrir la aplicación** en tu navegador
2. **Verificar conexión** - El indicador en la esquina superior derecha debe mostrar "API Conectada" (verde)
3. **Responder el cuestionario** - 10 preguntas sobre comportamiento y preferencias
4. **Completar información** - Datos personales y médicos
5. **Realizar evaluación** - Click en "Realizar Evaluación"
6. **Ver resultados** - El sistema mostrará la predicción y nivel de confianza

##  Estructura del Cuestionario

### Sección 1: Cuestionario AQ-10
10 preguntas sobre:
- Preferencias de rutina
- Habilidades sociales
- Atención y concentración
- Patrones de comportamiento

### Sección 2: Información Personal
- Edad
- Género
- Etnicidad
- País de residencia

### Sección 3: Información Médica
- Ictericia al nacer
- Historia familiar de autismo
- Relación con el evaluado

##  Personalización

### Cambiar Colores

Edita las variables CSS en `styles.css`:

```css
:root {
    --primary: #667eea;        /* Color primario */
    --secondary: #764ba2;      /* Color secundario */
    --success: #10b981;        /* Color de éxito */
    --danger: #ef4444;         /* Color de error */
}
```

### Cambiar URL de la API

Edita `script.js`:

```javascript
const API_URL = 'http://localhost:8000';  // Cambia aquí
```

##  Capturas de Pantalla

### Vista Principal
<img src="../.docs/screenshots/hero.png" alt="Hero Section" width="600">

### Formulario
<img src="../.docs/screenshots/form.png" alt="Form Section" width="600">

### Resultados
<img src="../.docs/screenshots/results.png" alt="Results Section" width="600">

##  Tecnologías Utilizadas

- **HTML5**: Estructura semántica
- **CSS3**: Diseño moderno con:
  - CSS Grid y Flexbox
  - Custom Properties (variables)
  - Animations y Transitions
  - Glassmorphism
  - Gradientes
- **JavaScript (Vanilla)**: Lógica sin frameworks
  - Fetch API para comunicación
  - Async/Await
  - DOM Manipulation
  - Event Handling

##  Compatibilidad

| Navegador | Versión Mínima | Estado |
|-----------|----------------|--------|
| Chrome    | 90+            | ✅ Completo |
| Firefox   | 88+            | ✅ Completo |
| Safari    | 14+            | ✅ Completo |
| Edge      | 90+            | ✅ Completo |

##  Solución de Problemas

### "API Desconectada"
**Solución**: Asegúrate de que la API esté corriendo:
```bash
cd ..
./start.sh
```

### Error CORS
**Solución**: La API ya tiene CORS habilitado. Si el problema persiste, verifica que la URL en `script.js` sea correcta.

### Formulario no envía
**Solución**: 
1. Verifica que todas las preguntas estén respondidas
2. Completa todos los campos obligatorios
3. Revisa la consola del navegador (F12) para errores

### Estilos no se cargan
**Solución**: Asegúrate de que `styles.css` esté en el mismo directorio que `index.html`

##  Métricas de Rendimiento

- **Tiempo de carga**: < 1s
- **First Contentful Paint**: < 0.5s
- **Time to Interactive**: < 1s
- **Tamaño total**: ~50KB (sin comprimir)

##  Privacidad y Seguridad

- ✅ No se almacenan datos personales
- ✅ No se usan cookies
- ✅ No se comparte información con terceros
- ✅ Validación de datos en cliente y servidor
-  **Nota**: Este es un sistema de evaluación preliminar, NO un diagnóstico médico

##  Uso Educacional

Esta aplicación es ideal para:
- Proyectos educativos sobre ML
- Demostraciones de APIs REST
- Aprendizaje de diseño web moderno
- Prototipado rápido

##  Soporte

Si encuentras algún problema:
1. Verifica que la API esté ejecutándose
2. Revisa la consola del navegador (F12)
3. Lee la sección de Troubleshooting
4. Consulta el README principal del proyecto

##  Mejoras Futuras

- [ ] Modo claro/oscuro
- [ ] Múltiples idiomas (i18n)
- [ ] Exportar resultados como PDF
- [ ] Historial de evaluaciones
- [ ] Gráficas y visualizaciones
- [ ] PWA (Progressive Web App)
- [ ] Animaciones más elaboradas
- [ ] Accesibilidad mejorada (WCAG 2.1)

##  Licencia

MIT License - Ver archivo LICENSE en el directorio principal

---

**Desarrollado con ❤️ usando HTML, CSS y JavaScript**
