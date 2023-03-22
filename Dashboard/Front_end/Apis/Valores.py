# blibiotecas 
import requests
import json  
# importa o link do arquivo de confuguraçao                 
from.Apis_config import APIServer_Name

#API para buscar dodos de cadastro 
def get_Valores():
    dados = requests.get(APIServer_Name['Valores'])
    return json.loads(dados.content)