# blibiotecas 
import requests
import bcrypt
# importa o link do arquivo de confuguraçao
from .Apis_config import APIServer_Name

#API para varificar os dados de login
def post_login(nome,senha):
    valores = {  
        "nome":nome,       
    }
    resp=requests.post(APIServer_Name['Login'],json=valores)
        
    if resp.status_code == 204:
        return 0
    else:
        hash=resp.content
        hash=hash.decode()
        hash=hash.removeprefix('"')
        hash=hash.removesuffix('"\n')
        hash = hash.encode()
        if bcrypt.checkpw(senha.encode('utf-8'),hash):
            return 1
        else:
            return 2