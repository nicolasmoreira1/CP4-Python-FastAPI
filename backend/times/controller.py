from fastapi import APIRouter, HTTPException

from times import service
from times.models import TimeCreate

router = APIRouter(prefix="/times", tags=["Times"])


@router.get("")
def listar_times():
    return service.listar_times()


@router.get("/{time_id}")
def buscar_time(time_id: int):
    time = service.buscar_time(time_id)
    if not time:
        raise HTTPException(404, "Time não encontrado")
    return time


@router.post("", status_code=201)
def criar_time(time: TimeCreate):
    return service.criar_time(time.model_dump())


@router.put("/{time_id}")
def atualizar_time(time_id: int, time: TimeCreate):
    if not service.buscar_time(time_id):
        raise HTTPException(404, "Time não encontrado")
    return service.atualizar_time(time_id, time.model_dump())


@router.delete("/{time_id}")
def excluir_time(time_id: int):
    if not service.buscar_time(time_id):
        raise HTTPException(404, "Time não encontrado")

    if service.tem_jogadores(time_id):
        raise HTTPException(400, "Este time ainda possui jogadores")

    service.excluir_time(time_id)
    return {"mensagem": "Time excluído"}
