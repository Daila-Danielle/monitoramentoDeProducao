#blibiotecas
from pathlib import Path
from .Db_Querys import Querys
from flask_restx import Resource
from flask import request
from Database.Database import DB
import json

Db_source = Path(__file__).parent/"Db_source.json"

with open(Db_source, encoding='utf-8') as my_json:
    dados = json.load(my_json)
    Setings = dados["Setings"]["MySQL"]
    
    
#Inicializa a isstancia do bando de dados
Database = DB(Setings)

# API Dados cadastro
class Dados_Producao (Resource):
    #metodo GET
    def get(self):

        dt_inicial=request.args.get('dt_inicial')
        dt_final=request.args.get('dt_final')
    
        lista=[]

        if dt_inicial == '' and dt_final == '':
           
            Database.execute_select(Querys["producao"])
        else : 
            print("entrou else")
            valores=(dt_inicial.replace("T"," "),dt_final.replace("T"," "))  
            Database.execute_select(Querys["Producao_Dt"],valores)
       
        for row in Database.query:
            dict={}
            dict={  
                    "id_prod":row[0],
                    "total":str(row[3]),
                    "inicio":str(row[1]),
                    "fim":str(row[2])                       
            }
            lista.append(dict)
    
        return lista
    
class Dados_Producao_Detalhar(Resource):
    #metodo GET
    def get(self):

        prod_id=request.args.get('prod_id')
        valores=(prod_id,)
        lista=[]
        sql ="SELECT tb1.id_prod, tb1.id_mat, tb1.quantidade, tb2.nome, tb3.nome FROM materiais_producao tb1 INNER JOIN materiais tb2 INNER JOIN mat_tipo tb3 ON tb2.id_mat = tb1.id_mat AND tb2.tipo_id = tb3.tipo_id WHERE tb1.id_prod = %s and tb1.quantidade <> 0" 
     
        Database.execute_select(sql,valores)
        for row in Database.query:
            dict={}
            dict={  
                    "id_prod":row[0],
                    "id_mat":row[1],
                    "nome":row[3],
                    "qtd":row[2],
                    "tipo":row[4]                       
            }
            lista.append(dict)
    
        return lista