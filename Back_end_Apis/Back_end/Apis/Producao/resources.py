#blibiotecas
from M340.Main.Unity_com  import Unity_Write
from pathlib import Path
from flask_restx import Resource
from flask import request
from .Db_Querys import Querys
from datetime import datetime
from Database.Database import DB
import json
import time

Db_source = Path(__file__).parent/"Db_source.json"

with open(Db_source,encoding='utf-8') as my_json:
    dados = json.load(my_json)
    setings = dados["Setings"]["MySQL"]
    
#Inicializa a isstancia do bando de dados
Database = DB(setings)

#pega os segundos para gerar o id da produção

Curent_prodID = 0

# API Produçao
class Producao (Resource):

    #metodo POST
    def post(self):
        global Curent_prodID

        initial_date = datetime.now().strftime("%Y-%m-%d, %H:%M:%S")
        Curent_prodID = int(time.time())
        values = (Curent_prodID,initial_date)
        sql= "insert into producao (id_prod,initial_date)values(%s,%s)"
        Database.execute(sql,values)

        materiais =[]
        ids=[]

        iteracao=0
        for mats in request.json["materiais"]:
            if mats !="0":
                materiais.append(mats)
                ids.append(request.json["mat_ids"][iteracao])
                values = (Curent_prodID,request.json["mat_ids"][iteracao])
                Database.execute(Querys["Add_materiais"],values)
            iteracao+=1

        Unity_Write()
        return 'Producao iniciada com sucesso',201
    
    #metodo PUT
    def put(self):

        global Curent_prodID

        if request.json["comando"] == "fechar":
            final_date = datetime.now().strftime("%Y-%m-%d, %H:%M:%S")
        
            valores=(Curent_prodID,)
            sql= "SELECT id_prod FROM producao WHERE id_prod = %s"
            Database.execute_select (sql,valores)
            
            if Database.rowcount >= 1 :
                valores = (final_date,Curent_prodID)
                sql = "UPDATE producao SET final_date = %s WHERE producao.id_prod = %s"
                Database.execute(sql,valores)
                Curent_prodID = 0

                return "Producao Fechada Com Sucesso",200
            else:
                return "Nenhuma Producao foi iniciada",404
            
        elif request.json["comando"] == "atualizar":
            
            qtd=request.json["qtd"]
            id_mat=request.json["id_mat"]
           
            valores=(qtd,Curent_prodID,id_mat)
            print(valores)
             
            sql = "UPDATE materiais_producao SET quantidade = %s WHERE id_prod = %s AND id_mat = %s"
            Database.execute(sql,valores)

            return "",200

        
        else:
            pass
  

    #metodo DELETE
    def delete(self):
        id = request.json ['id']

        values=(id,)    
        sql = "DELETE FROM materiais_producao WHERE id_prod = %s"
        Database.execute(sql,values)
        sql = "DELETE FROM producao WHERE id_prod = %s"
        Database.execute(sql,values)
        
        return "Producao Deletada com sucesso",201   