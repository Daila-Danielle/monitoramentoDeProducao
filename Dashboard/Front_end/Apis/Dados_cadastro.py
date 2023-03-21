# blibiotecas 
import requests
import json  
# importa o link do arquivo de confuguraçao                 
from.Apis_config import APIServer_Name

#API para buscar dodos de cadastro 
def get_Dados_cadastro():
    dados = requests.get(APIServer_Name['Dados_cadastro'])
    return json.loads(dados.content)