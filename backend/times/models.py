from pydantic import BaseModel


class TimeCreate(BaseModel):
    nome: str
    cidade: str
    ano_fundacao: int | None = None
