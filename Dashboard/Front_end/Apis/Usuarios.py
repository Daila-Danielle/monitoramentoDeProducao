# blibiotecas
import requests
import json
# importa o link do arquivo de confuguraçao
from .Apis_config import APIServer_Name

#API para buscar dodos de um usuario
def get_usuario(nome):
    dados = requests.get(f""+APIServer_Name['Usuario']+"?&nome="+nome)
    return json.loads(dados.content)

#API para adicionar um usuario
def post_usuario(nome,senha,cargo,grupo,img_name):
    valores = {  
        "nome":nome,
        "senha":senha,
        "cargo":cargo,
        "grupo":grupo,
        "img_nome":img_name,
    }
    return requests.post(APIServer_Name['Usuario'],json=valores)