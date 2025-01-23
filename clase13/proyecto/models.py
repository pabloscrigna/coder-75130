from pydantic import BaseModel, Field
from uuid import UUID, uuid4


class Producto(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    nombre: str
    precio: float
    stock: bool = True
