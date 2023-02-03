

import json
import urllib3


URL = "https://pokeapi.co/api/v2/pokemon/"
# URLU = "https://jsonplaceholder.typicode.com/users"

# URL = os.getenv("URL")
# URLU = os.getenv("URLU")


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
                raise BadContent()
            datav = ""
            try:
                datav = self.__getdata__(URL)
            except Exception as exc:
                raise FindException() from exc
            else:
                valor = ""
                for item in datav["results"]:
                    if self.namep in item["name"]:
                        valor = self.namep
                if len(valor) < 1:
                    print(f"DON'T EXIST {self.namep}")
                    raise FindException()
                print(f"EXIST {self.namep}")
        except ValueError as exc:
            raise ValueError() from exc
        except BadContent as exc:
            raise BadContent(code=400, msg="Datos incorrectos o incompletos") from exc
        except FindException as exc:
            raise FindException(
                code=404, msg="La operacion solicitada fallo - pokemon"
            ) from exc
        '''
        # try:
        #     if self.nameu == "" or URLU == "":
        #         raise BadContent()
        #     datav = ""
        #     try:
        #         datav = self.__getdata__(URLU)
        #     except Exception as exc:
        #         raise FindException() from exc
        #     else:
        #         username = []
        #         for names in datav:
        #             if names["name"] == self.nameu:
        #                 username.append(names["name"])
        #         if len(username) < 1:
        #             raise FindException()
        #         print("USER EXIST =>", username[0])
        # except ValueError as exc:
        #     raise ValueError() from exc
        # except BadContent as exc:
        #     raise BadContent(code=400, msg="Datos incorrectos o incompletos") from exc
        # except FindException as exc:
        #     raise FindException(
        #         code=404, msg="La operacion solicitada fallo - user"
        #     ) from exc
        '''

    def get_abilities(self):
        """Obtener habilidades"""
        print("habilidades")
        try:
            if self.namep == "" or URL == "":
                raise BadContent()
            datap = ""
            try:
                datap = self.__getdata__(URL, self.namep)
            except Exception as exc:
                raise FindException() from exc
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
        except BadContent as exc:
            raise BadContent(code=400, msg="Datos incorrectos o incompletos") from exc
        except FindException as exc:
            raise FindException(
                code=404, msg="La operacion solicitada fallo - ability"
            ) from exc

    def __height_weight__(self, urlp="", searchs=""):
        """Obtener pero o altura"""
        print("sdfghjkl")
        try:
            if self.namep == "" or urlp == "" or searchs == "":
                raise BadContent()
            datap = ""
            try:
                datap = self.__getdata__(urlp, self.namep)
            except Exception as exc:
                raise FindException() from exc
            else:
                if datap[searchs] == "" or datap[searchs] == "undefined":
                    raise FindException()
                return datap[searchs]
        except ValueError as exc:
            raise ValueError() from exc
        except BadContent as exc:
            raise BadContent(code=400, msg="Datos incorrectos o incompletos") from exc
        except FindException as exc:
            raise FindException(code=404, msg="La operacion solicitada fallo") from exc

    def get_weight(self):
        """Obtener peso"""
        return self.__height_weight__(URL, "weight")

    def get_height(self):
        """Obtener altura"""
        return self.__height_weight__(URL, "height")
