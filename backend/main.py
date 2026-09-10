from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import database
from times.controller import router as times_router
from jogadores.controller import router as jogadores_router

app = FastAPI(title="API de Times e Jogadores")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

database.criar_tabelas()

app.include_router(times_router)
app.include_router(jogadores_router)
