#blibiotecas
from M340.Main.Unity_com  import Unity_Write
from pathlib import Path
from flask_restx import Resource
from flask import request,session
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

        session['idprod']=Curent_prodID
        
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

        for x in range(9):
            Unity_Write(f"%MW10"+str(x),int(request.json["materiais"][x]))
        Unity_Write("%MW200",1)
        Unity_Write("%MW200",0)

        return 'Producao iniciada com sucesso',201
    
    #metodo DELETE
    def delete(self):
        id = request.json ['id']

        values=(id,)    
        sql = "DELETE FROM materiais_producao WHERE id_prod = %s"
        Database.execute(sql,values)
        sql = "DELETE FROM producao WHERE id_prod = %s"
        Database.execute(sql,values)
        
        return "Producao Deletada com sucesso",201   