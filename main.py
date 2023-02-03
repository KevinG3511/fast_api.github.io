""" Main """

from fastapi import FastAPI
# from core.config import settings
from api import router
# from schemas.modelos import Ricks,User

app = FastAPI()

app.include_router(router)

# @app.get("/names")
# async def root2(name:User = Depends()):
#     """ ruta para rick and morty """
#     # print(type(name.dict()),name.dict())
#     return {"message": name.dict()}


# @app.put("/comercio")
# async def root3(nombre_p: str,datos: Entrada):
#     return {"message": f"Hello World {datos.dict()}"}