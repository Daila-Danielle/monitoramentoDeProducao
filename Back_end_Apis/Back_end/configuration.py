from importlib import import_module
from dynaconf import FlaskDynaconf


def init_app(App):
    FlaskDynaconf(App) 


def load_extensions(App):
    for extension in App.config.EXTENSIONS:
        module_name,factory = extension.split(":")
        ext = import_module(module_name)
        getattr(ext,factory)(App)

   


        











