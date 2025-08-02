from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from langchain_openai import ChatOpenAI
import os
from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import Request
from fastapi.staticfiles import StaticFiles

#Inicialización
app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"], #GET #POST
    allow_headers=["*"],
)

#variables de entorno
load_dotenv()

#Modelo de gpt 
model = ChatOpenAI(
    model_name="gpt-4o-mini",
    temperature=0.6,
    openai_api_key=os.getenv("OPENAI_API_KEY")
)

class DriverAssessmentRequest(BaseModel):
    context: str
    observation: str

@app.post("/recovery_plan")
async def recovery_plan(request: DriverAssessmentRequest):
    try:
        prompt = f"""
        Eres un experto en gestión de desastres, recuperación post-emergencia y planificación estratégica, 
        con énfasis en eventos relacionados con sequías severas. Tienes experiencia en evaluar el impacto ambiental, 
        económico y social de la escasez de agua, en estimar costos de recuperación y en coordinar recursos humanos, 
        técnicos y financieros para restablecer el equilibrio en comunidades afectadas.

        Contexto:
        {request.context}

        Observaciones:
        {request.observation}

        Proporciona una evaluación detallada que incluya:
        1. Indicadores de afectación identificados 
        2. Clasificación del impacto
        3. Estimación general de recursos necesarios
        4. Plan de acción propuesto
        5. Recomendaciones estratégicas
        """
        
        response = model.invoke(prompt)
        
        return {
            "assessment": response.content,
        }
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/", response_class=HTMLResponse)
async def landing(request: Request):
    return templates.TemplateResponse("landing.html", {"request": request})

@app.get("/evaluar", response_class=HTMLResponse)
async def evaluar(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000) 