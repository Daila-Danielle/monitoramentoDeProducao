#blibioteacs 
from flask_restx import Resource
from flask import request
from M340.Main.Unity_com import Unity_Read

# API usuario
class valores (Resource):

    def get(self,):
        lista=Unity_Read("%MW300",9)
        return lista

 