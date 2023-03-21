# blibiotecas 
import requests
import json  
# importa o link do arquivo de confuguraçao                 
from.Apis_config import APIServer_Name

#API para buscar dodos de cadastro 
def get_dados_producao_detalhar(id):
    dados = requests.get(f""+APIServer_Name['Dados_producao_detalhar']+"?&prod_id="+id)
    return json.loads(dados.content)