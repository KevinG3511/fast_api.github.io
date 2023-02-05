

import json
import urllib3


URL = "https://pokeapi.co/api/v2/pokemon/"
# URLU = "https://jsonplaceholder.typicode.com/users"

# URL = os.getenv("URL")
# URLU = os.getenv("URLU")


class FindExceptions(Exception):
    """Exception"""

    def __init__(self, code=500, msg="error"):
        self.code = code
        self.msg = msg


class BadContents(Exception):
    """Exception"""

    def __init__(self, code=500, msg="error"):
        self.code = code
        self.msg = msg


class Pokemon:
    """Start class"""

    def __init__(self, namep=""):
        self.namep = namep
        # self.nameu = nameu
        self.validation()

    @staticmethod
    def __getdata__(url, args=""):
        http = urllib3.PoolManager()
        resp1 = http.request("GET", url + args)
        data = resp1.data.decode("utf-8")
        return json.loads(data)  # return obj in json

    def validation(self):
        """Validar si existe"""
        try:
            if self.namep == "" or URL == "":
                raise BadContents()
            datav = ""
            try:
                datav = self.__getdata__(URL)
            except Exception as exc:
                raise FindExceptions() from exc
            else:
                valor = ""
                for item in datav["results"]:
                    if self.namep in item["name"]:
                        valor = self.namep
                if len(valor) < 1:
                    print(f"DON'T EXIST {self.namep}")
                    raise FindExceptions()
                print(f"EXIST {self.namep}")
        except ValueError as exc:
            raise ValueError() from exc
        except BadContents as exc:
            raise BadContents(code=400, msg="Datos incorrectos o incompletos") from exc
        except FindExceptions as exc:
            raise FindExceptions(
                code=404, msg="La operacion solicitada fallo - pokemon"
            ) from exc
        '''
        # try:
        #     if self.nameu == "" or URLU == "":
        #         raise BadContents()
        #     datav = ""
        #     try:
        #         datav = self.__getdata__(URLU)
        #     except Exception as exc:
        #         raise FindExceptions() from exc
        #     else:
        #         username = []
        #         for names in datav:
        #             if names["name"] == self.nameu:
        #                 username.append(names["name"])
        #         if len(username) < 1:
        #             raise FindExceptions()
        #         print("USER EXIST =>", username[0])
        # except ValueError as exc:
        #     raise ValueError() from exc
        # except BadContents as exc:
        #     raise BadContents(code=400, msg="Datos incorrectos o incompletos") from exc
        # except FindExceptions as exc:
        #     raise FindExceptions(
        #         code=404, msg="La operacion solicitada fallo - user"
        #     ) from exc
        '''

    def get_abilities(self):
        """Obtener habilidades"""
        print("habilidades")
        try:
            if self.namep == "" or URL == "":
                raise BadContents()
            datap = ""
            try:
                datap = self.__getdata__(URL, self.namep)
            except Exception as exc:
                raise FindExceptions() from exc
            else:
                dic = {}
                for ability in datap["abilities"]:
                    print(ability["ability"]["name"])
                    habilidad = self.__getdata__(
                        ("https://pokeapi.co/api/v2/ability/"),
                        ability["ability"]["name"],
                    )
                    dic[ability["ability"]["name"]] = (
                        habilidad["effect_entries"][-1]["effect"],
                        habilidad["generation"]["name"],
                    )
                return dic
        except ValueError as exc:
            raise ValueError() from exc
        except BadContents as exc:
            raise BadContents(code=400, msg="Datos incorrectos o incompletos") from exc
        except FindExceptions as exc:
            raise FindExceptions(
                code=404, msg="La operacion solicitada fallo - ability"
            ) from exc

    def __height_weight__(self, urlp="", searchs=""):
        """Obtener pero o altura"""
        print("sdfghjkl")
        try:
            if self.namep == "" or urlp == "" or searchs == "":
                raise BadContents()
            datap = ""
            try:
                datap = self.__getdata__(urlp, self.namep)
            except Exception as exc:
                raise FindExceptions() from exc
            else:
                if datap[searchs] == "" or datap[searchs] == "undefined":
                    raise FindExceptions()
                return datap[searchs]
        except ValueError as exc:
            raise ValueError() from exc
        except BadContents as exc:
            raise BadContents(code=400, msg="Datos incorrectos o incompletos") from exc
        except FindExceptions as exc:
            raise FindExceptions(code=404, msg="La operacion solicitada fallo") from exc

    def get_weight(self):
        """Obtener peso"""
        return self.__height_weight__(URL, "weight")

    def get_height(self):
        """Obtener altura"""
        return self.__height_weight__(URL, "height")
