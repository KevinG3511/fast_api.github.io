from fastapi import APIRouter, Depends
from schemas.modelos import Ricks,Poke
from .rick_and_morty import RickAndMorty,BadContent,FindException
from .pokemon import Pokemon,BadContent,FindException
import urllib3


service1 = APIRouter()

@service1.get("/rick_and_morty")
async def root1(name:Ricks = Depends()):
    """ ruta para rick and morty """
    try:
        newrick = RickAndMorty(name.nombres)
        results = {
            "name": name,
            "origin": newrick.get_origin(),
            "gender": newrick.get_gender(),
            "status": newrick.get_status(),
        }
        # if not(all(results.values())):
        #     raise FindException()
        obj = {"status": 200, "results": results, "msg": "Peticion correcta"}
        return obj
    except ValueError:
        return {"status":400, "results":{} ,"msg":"Formato incorrecto"}
    except BadContent as exc:
        return {"status": exc.code, "results":{} ,"msg": exc.msg}
    except FindException as exc:
        return {"status": exc.code, "results":{} ,"msg": exc.msg}


@service1.get("/pokemon")
async def root2(name:Poke = Depends()):
    """ ruta para pokemons """
    try:
        newpoke = Pokemon(name.nombre)
        results = {
            "nameP": name.nombre,
            "abilities": newpoke.get_abilities(),
            "weight": newpoke.get_weight(),
            "height": newpoke.get_height(),
        }
        obj = {"status": 200, "results": results, "msg": "Peticion correcta"}
        return obj
    except ValueError:
        return {"status": 400, "results":{} ,"msg": "Formato incorrecto"}
    except BadContent as exc:
        return {"status": exc.code, "results":{} ,"msg": exc.msg}
    except FindException as exc:
        return {"status": exc.code, "results":{} ,"msg": exc.msg}
    
    