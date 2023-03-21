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

# API Dados cadastro
class Dados_Cadastro (Resource):
    
    #metodo GET
    def get( self):

        lista=[]
        sql ="select nome,id from cargos " 
        Database.execute_select(sql)
        Database.query = [tuple(row) for row in Database.query]

        dict={}
        dict={  
                "cargos":Database.query    
        }
        lista.append(dict)
        
        sql ="select nome,id from grupos " 
        Database.execute_select(sql)
        Database.query = [tuple(row) for row in Database.query]
       
        dict={}
        dict={  
                "grupos":Database.query          
        }

        lista.append(dict)
        return lista