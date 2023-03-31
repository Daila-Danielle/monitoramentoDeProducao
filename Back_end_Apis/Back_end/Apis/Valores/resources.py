#blibioteacs 
from flask_restx import Resource
from flask import request
from M340.Main.Unity_com import Unity_Read

# API usuario
class valores (Resource):

    def get(self,):
        lista = [0,0,0,0,0,0,0,0,0,0]
        if Unity_Read("%MW203",1) != "erro":
            lista=Unity_Read("%MW300",9)
            status = Unity_Read("%MW203",1)[0]

            if status != "erro":
                lista.append(status)
            else:
                lista.append(0)


            return lista
        else:
            return lista 

 