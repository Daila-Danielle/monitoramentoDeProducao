from datetime import datetime
from flask import session
from Database.Database import DB
from pathlib import Path
import json

Db_source = Path(__file__).parent/"Db_source.json"

with open(Db_source,encoding='utf-8') as my_json:
    dados = json.load(my_json)
    setings = dados["Setings"]["MySQL"]
    
#Inicializa a isstancia do bando de dados
Database = DB(setings)

def Atualiza(dados):
    
    sql= "SELECT id_prod FROM producao ORDER BY id_prod DESC LIMIT 1 "
    Database.execute_select (sql)
    Curent_prodID = Database.query[0]

    print("ok")
    mat_id=[3256,5698,6328,4568,9746,3265,9864,9875,6548]
    qtd=0
    id_mat=0
    for x in range(9):
        if dados[x]!= 0:
            qtd=dados[x]
            id_mat=mat_id[x]
            valores=(qtd,Curent_prodID[0],id_mat)
            sql = "UPDATE materiais_producao SET quantidade = %s WHERE id_prod = %s AND id_mat = %s"
            Database.execute(sql,valores)
    print("FIM")

def Fechar():
    final_date = datetime.now().strftime("%Y-%m-%d, %H:%M:%S")

    sql= "SELECT id_prod FROM producao ORDER BY id_prod DESC LIMIT 1 "
    Database.execute_select (sql)
    Curent_prodID = Database.query[0]

    valores = (final_date,Curent_prodID[0])
    sql = "UPDATE producao SET final_date = %s WHERE producao.id_prod = %s"
    Database.execute(sql,valores)
    Curent_prodID = 0

    