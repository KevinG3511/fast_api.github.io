"""Iniciar flask"""

# import requests
# import os
import json
import urllib3



class FindException(Exception):
    """Exception"""

    def __init__(self, code=500, msg="error"):
        self.code = code
        self.msg = msg


class BadContent(Exception):
    """Exception"""

    def __init__(self, code=500, msg="error"):
        self.code = code
        self.msg = msg


URLR = 'https://rickandmortyapi.com/api/character'
# URLR = os.getenv("URLR")


class RickAndMorty:
    """Start class"""

    def __init__(self, namep=""):
        self.namep = namep
        self.validation()
        # self.nameU = nameU

    @staticmethod
    def __getdata__(url, args=""):
        http = urllib3.PoolManager()
        resp1 = http.request("GET", url + args)
        data = resp1.data.decode("utf-8")
        return json.loads(data)  # return obj in json

    def validation(self):
        """Validar si existe"""
        try:
            if self.namep == "" or URLR == "":
                raise BadContent()
            datap = self.__getdata__(URLR)
            pers = []
            for name in datap["results"]:
                if name["name"] == self.namep:
                    pers.append(name)
            if len(pers) < 1:
                raise FindException()
            print("EXIST =>", pers[0]["name"])
            # return {"Nombre":pers[0]['name'],
            # "Status":pers[0]['status'],"Species":pers[0]['species']}
        except ValueError as exc:
            raise ValueError() from exc
        except BadContent as exc:
            raise BadContent(code=400, msg="Datos incorrectos o incompletos") from exc
        except FindException as exc:
            raise FindException(code=404, msg="La operacion solicitada fallo") from exc
        # except Exception as exc:
        #     return "ERROR A => ", exc

    def __origin_gender___(self, searchs=""):
        """Obtener origen o genero o estado"""
        try:
            if URLR == "" or self.namep == "" or searchs == "":
                raise BadContent()
            datap = ""
            try:
                datap = self.__getdata__(URLR)
            except Exception as exc:
                raise FindException() from exc
            else:
                res = ""
                for item in datap["results"]:
                    if item["name"] == self.namep:
                        if str(searchs) == "status" or searchs == "gender":
                            res = item[searchs]
                        elif str(searchs) == "origin":
                            res = item[searchs]["name"]
                        break
                if len(res) < 1 or res == "" or len(res) == 0:
                    raise FindException()
                return res
        except ValueError as exc:
            raise ValueError() from exc
        except BadContent as exc:
            raise BadContent(code=400, msg="Datos incorrectos o incompletos") from exc
        except FindException as exc:
            raise FindException(code=404, msg="La operacion solicitada fallo") from exc

    def get_origin(self):
        """Obtener peso"""
        return self.__origin_gender___("origin")

    def get_gender(self):
        """Obtener altura"""
        return self.__origin_gender___("gender")

    def get_status(self):
        """Obtener altura"""
        return self.__origin_gender___("status")
