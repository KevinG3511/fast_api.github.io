from fastapi import APIRouter, Depends
from schemas.modelos import Poke
from .pokemon import Pokemon,BadContent,FindException
import urllib3

service1 = APIRouter()

@service1.get("/pokemon")
async def root1(name:Poke = Depends()):
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
    except urllib3.exceptions.MaxRetryError:  # try error
        return {"status": 500, "msg": "La solicitud falló debido a un error interno"}
    except BadContent as exc:
        return {"status": exc.code, "results":{} ,"msg": exc.msg}
    except FindException as exc:
        return {"status": exc.code, "results":{} ,"msg": exc.msg}
    