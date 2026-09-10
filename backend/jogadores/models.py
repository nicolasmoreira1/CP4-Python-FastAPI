from pydantic import BaseModel


class JogadorCreate(BaseModel):
    nome: str
    posicao: str
    idade: int | None = None
    time_id: int
