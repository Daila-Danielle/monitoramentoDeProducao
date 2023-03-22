#blibiotecas
from flask_restx import Api
#iMporta a classe dos arquivos de APIS criados

from .Dados_cadastro.resources import Dados_Cadastro
from .Login.resources import Login
from .Producao.resources  import Producao
from .Usuario.resources import usuario 
from .Dados_producao.resources import Dados_Producao,Dados_Producao_Detalhar
from .Valores.resources import valores

# gera instancia do app para nao causar circular inport
def init_App(App):

    #cria rotas para as APIs 
    Api_Routes = Api(App)
    Api_Routes.add_resource(Dados_Cadastro,"/Dados_Cadastro")
    Api_Routes.add_resource(Dados_Producao,"/Dados_Producao")
    Api_Routes.add_resource(Dados_Producao_Detalhar,"/Dados_Producao_Detalhar")
    Api_Routes.add_resource(Login,"/Login")
    Api_Routes.add_resource(Producao,"/Producao")
    Api_Routes.add_resource(usuario,"/Usuario")
    Api_Routes.add_resource(valores,"/Valores")
   