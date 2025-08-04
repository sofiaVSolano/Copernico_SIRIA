# SIRIA - Sistema Inteligente de Recuperación por Impacto de Sequía Asistido por IA

SIRIA es una aplicación web que utiliza IA para evaluar condiciones de sequía y proporcionar planes de recuperación personalizados.

**🌐 [Ver aplicación desplegada](https://copernico-siria.onrender.com/)**

## Características

- Evaluación de condiciones de sequía mediante descripción textual
- Alertas en tiempo real basadas en ubicación geográfica
- Visualización de datos de humedad del suelo en mapas interactivos
- Generación de planes de recuperación personalizados

## Tecnologías utilizadas

- Backend: FastAPI
- Frontend: HTML, CSS, JavaScript
- Mapas: Leaflet
- IA: OpenAI API
- Estilo: Bootstrap/componentes personalizados

## Requisitos para desarrollo local

1. Python 3.10+
2. API key de OpenAI

## Instalación local

```bash
# Clonar el repositorio
git clone https://github.com/sofiaVSolano/Copernico_SIRIA.git
cd Copernico_SIRIA

# Crear entorno virtual
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate

# Instalar dependencias
pip install -r requirements.txt

# Configurar variables de entorno
# Crear archivo .env y añadir:
# OPENAI_API_KEY = "tu-api-key"

# Ejecutar la aplicación
uvicorn model:app --reload
```

## Despliegue en Render

El proyecto está actualmente desplegado en: [https://copernico-siria.onrender.com/](https://copernico-siria.onrender.com/)

Para desplegar tu propia instancia:

1. Crear una cuenta en Render.com
2. Conectar el repositorio de GitHub
3. Crear un nuevo Web Service con:
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `sh render.sh`
4. Configurar variables de entorno:
   - OPENAI_API_KEY = tu_api_key
   - PYTHONUNBUFFERED = true
   
El proyecto incluye un GitHub Action que hace ping al servicio cada 5 minutos para evitar que entre en modo de reposo (plan gratuito de Render).

## Equipo PADIA

Proyecto desarrollado por PADIA como parte del semillero Copérnico.
