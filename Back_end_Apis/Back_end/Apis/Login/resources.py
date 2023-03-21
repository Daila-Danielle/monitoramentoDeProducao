#blibiotecas
from pathlib import Path
from flask_restx import Resource
from flask import request
from Database.Database import DB

import json

Db_source = Path(__file__).parent/"Db_source.json"

with open(Db_source,encoding='utf-8') as my_json:
    dados = json.load(my_json)
    setings = dados["Setings"]["MySQL"]
    

#Inicializa a isstancia do bando de dados
Database = DB(setings)

#API Login
class Login (Resource):
    
    #metodo POST
    def post( self):

        nome = request.json["nome"]
        valores=(nome,)

        sql= "SELECT senha FROM usuarios WHERE binary nome like %s"
        Database.execute_select (sql,valores)

        if (Database.rowcount > 0):
            hash = Database.query[0][0]
            return hash,201
        else:
            return "",204
       

