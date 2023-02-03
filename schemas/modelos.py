""" Modelos """

from pydantic import BaseModel

class Ricks(BaseModel):
    """Modelo de rick and morty"""
    nombres : str
class Poke(BaseModel):
    """Modelo de pokemon"""
    nombre : str
