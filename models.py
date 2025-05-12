from pydantic import BaseModel
from typing import Optional

class Produtos(BaseModel):
    nome: str
    descricao: Optional[str] = None
    preco: str
    quantidade: str
    validade: str

    