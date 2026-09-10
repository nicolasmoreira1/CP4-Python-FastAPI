from fastapi import APIRouter, HTTPException

from jogadores import service
from jogadores.models import JogadorCreate
from times import service as times_service

router = APIRouter(prefix="/jogadores", tags=["Jogadores"])


@router.get("")
def listar_jogadores():
    return service.listar_jogadores()


@router.get("/{jogador_id}")
def buscar_jogador(jogador_id: int):
    jogador = service.buscar_jogador(jogador_id)
    if not jogador:
        raise HTTPException(404, "Jogador não encontrado")
    return jogador


@router.post("", status_code=201)
def criar_jogador(jogador: JogadorCreate):
    if not times_service.buscar_time(jogador.time_id):
        raise HTTPException(404, "Time não encontrado")
    return service.criar_jogador(jogador.model_dump())


@router.put("/{jogador_id}")
def atualizar_jogador(jogador_id: int, jogador: JogadorCreate):
    if not service.buscar_jogador(jogador_id):
        raise HTTPException(404, "Jogador não encontrado")

    if not times_service.buscar_time(jogador.time_id):
        raise HTTPException(404, "Time não encontrado")

    return service.atualizar_jogador(jogador_id, jogador.model_dump())


@router.delete("/{jogador_id}")
def excluir_jogador(jogador_id: int):
    if not service.buscar_jogador(jogador_id):
        raise HTTPException(404, "Jogador não encontrado")

    service.excluir_jogador(jogador_id)
    return {"mensagem": "Jogador excluído"}
