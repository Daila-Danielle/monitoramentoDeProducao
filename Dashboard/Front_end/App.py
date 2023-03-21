# blibiotecas
from flask import Flask
# inporta arquivo de configuração
import configuration

#cria a instancia do app
App = Flask(__name__)

# funçoes para inicialização das dependencias 
configuration.init_app(App)
configuration.secretkey(App)
configuration.load_extensions(App)

#inicia o aplicativo
App.run()  