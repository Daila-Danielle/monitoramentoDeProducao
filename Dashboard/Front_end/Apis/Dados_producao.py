# blibiotecas 
import requests
import json  
# importa o link do arquivo de confuguraçao                 
from.Apis_config import APIServer_Name

#API para buscar dodos de cadastro 
def get_Dados_producao(dt_inicial,dt_final):
    dados = requests.get(APIServer_Name['Dados_producao']+"?&dt_inicial="+dt_inicial+"&dt_final="+dt_final)
    return json.loads(dados.content)


def delete_Producao(valor):
    valores={
        'id':valor
    }
    retorno= requests.delete(APIServer_Name['Producao'],json=valores)
    print(retorno)
    