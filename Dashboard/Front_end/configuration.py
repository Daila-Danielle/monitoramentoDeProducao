# blibiotecas
from importlib import import_module
import os
from dynaconf import FlaskDynaconf


#função para iniciar o daynaconf
def init_app(App):
    FlaskDynaconf(App) 

#função para gerar a secretKey
def secretkey(App):
    App.secret_key = os.urandom(16)


#função para carregar as estenções presentes no arquivo do daynaconf (settings.toml)
def load_extensions(App):
    for extension in App.config.EXTENSIONS:
        module_name, factory = extension.split(":")
        ext = import_module(module_name)
        getattr(ext,factory)(App)

   


        











