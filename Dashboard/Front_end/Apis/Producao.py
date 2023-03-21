# blibiotecas 
import requests
import json
# importa o link do arquivo de confuguraçao 
from .Apis_config import APIServer_Name

#API para buscar dados das produçoes
def get_Production():
    dados = requests.get(APIServer_Name['Producao'])
    return json.loads(dados.content)
        
#API para iniciar uma produção    
def post_Production(mat=[],id=[]):
   
    values = {
        "materiais":mat,
        "mat_ids":id 
    }

    print(values)
    resposta = requests.post(APIServer_Name['Producao'],json=values) 

        
#API para Finalizar uma produção 
def put_Production(op):
    values = {   
        "comando":op , 
        "qtd":20 ,  
        "id_mat":3256     
    }
    resposta = requests.put(APIServer_Name['Producao'],json=values) 

        
#API para Deletar uma produção     
def delete_Production(id):
    values = {
        "id":id           
    }
    resposta = requests.delete(APIServer_Name['Producao'],json=values) 
   
   