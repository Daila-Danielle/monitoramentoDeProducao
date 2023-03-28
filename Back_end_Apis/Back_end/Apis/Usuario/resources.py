#blibioteacs 
from pathlib import Path
from flask_restx import Resource
from flask import request
import bcrypt
from Database.Database import DB
import json

Db_source = Path(__file__).parent/"Db_source.json"

with open(Db_source,encoding='utf-8') as my_json:
    dados = json.load(my_json)
    setings = dados["Setings"]["MySQL"]
    


#Inicializa a isstancia do bando de dados
Database = DB(setings)
#gera chave para cryptografia
chave = bcrypt.gensalt()

# API usuario
class usuario (Resource):

    #metodo post
    def post(self):
        
        nome = request.json["nome"]
        senha = request.json["senha"]
        cargo = request.json["cargo"]
        grupo = request.json["grupo"]
        img_name = request.json["img_nome"]
       
        sql= "insert into usuarios (nome,senha,cargo,grupo,img_name)values(%s,%s,%s,%s,%s)"
        valores = (nome,senha,cargo,grupo,img_name)
        Database.execute(sql,valores)

        return 'criado',201
    
    #metodo GET
    def get(self,):
       
        nome=request.args.get('nome')
        
        lista=[]
        valores=(nome,)
        sql1 ="select id,nome,cargo,grupo,img_name from usuarios where binary nome like %s"
        Database.execute_select(sql1,valores)

        for dados in Database.query:
            dict={}
            
            dict={  "id":dados[0],
                    "nome":dados[1],
                    "cargo":dados[2],
                    "tipo":dados[3],
                    "img_nome":dados[4],
            }
            lista.append(dict)

        return lista

    #metodo PUT
    def put(self):

        id = request.json ['id']
        nome= request.json["nome"]
        senha= request.json["senha"].encode('utf-8')
        cargo= request.json["cargo"]
       
        hash = bcrypt.hashpw(senha,chave)

        valores=(id,)
        sql= "SELECT id FROM usuarios WHERE id =%s"
        Database.execute_select (sql,valores)
        
        if Database.rowcount >= 1 :
            valores = (nome,hash,cargo,id)
            sql = "UPDATE usuarios SET nome = %s, senha = %s, cargo = %s WHERE usuarios.id = %s"
            Database.execute(sql,valores)
            return "Atualizado",200
        else:
            return"Erro registro não existe",404

    #metodo DELETE
    def delete(self):

        id = request.json ['id']
        valores=(id,)    
        sql = "DELETE FROM usuarios WHERE id = %s"
        Database.execute(sql,valores)

        return "",204