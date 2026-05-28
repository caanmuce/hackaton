from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


from backend.api.clima_rutas import router as rutas_gubernamentales

from backend.api.zonas_router import router as zonas_criticas_router

app = FastAPI()

# Habilitar CORS para que tus archivos HTML locales puedan consumir las APIs
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)




app.include_router(rutas_gubernamentales, prefix="/api/rutas")


app.include_router(zonas_criticas_router, prefix="/api/zonas")