from contextlib import asynccontextmanager
from fastapi import FastAPI, HTTPException, BackgroundTasks
from fastapi.responses import JSONResponse
from typing import List
from time import sleep
from pydantic import BaseModel, Field
from uuid import UUID, uuid4


class Producto(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    nombre: str
    precio: float
    stock: bool = True

    def to_json(self):
        return {
            "id": str(self.id),
            "nombre": self.nombre,
            "precio": self.precio,
            "stock": self.stock,
        }


def send_mail():
    print("Enviando mail....")
    sleep(10)
    print("Mail enviado")


productos_lista: List[Producto] = []


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Iniciando servidor.....")
    global productos_lista
    productos_lista = [
        Producto(nombre="Laptop", precio=1000.0),
        Producto(nombre="Mouse", precio=10.0),
        Producto(nombre="Teclado", precio=20.0),
    ]
    yield
    print("Shutdown")

app = FastAPI(lifespan=lifespan)


@app.get("/health")
def health():
    return {"status": "ok"}


# CRUD

@app.post("/productos/", response_model=Producto)
def create_product(
    producto: Producto,
    background_tasks: BackgroundTasks,
):
    productos_lista.append(producto)
    background_tasks.add_task(send_mail)
    print(productos_lista)
    return JSONResponse(status_code=201, content={"producto": producto.to_json()})


@app.get("/productos/")
def listar_productos():
    return JSONResponse(status_code=200, content={"productos": [producto.to_json() for producto in productos_lista]})


@app.get("/productos/{producto_id}",response_model=Producto)
def buscar_id(producto_id: UUID):
    for producto in productos_lista:
        if producto.id == producto_id:
            return {producto}
    raise HTTPException(status_code=404, detail="Producto no encontrado")
