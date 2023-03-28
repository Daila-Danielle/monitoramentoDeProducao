#blibiotecas
from M340.Utils.Temporizadores import Timer
from M340.Main.Unity_com import Unity_Read,Unity_Write
from Functions.Produção import Atualiza,Fechar
from flask import Flask,session
import threading
import configuration
import os

App = Flask(__name__)
configuration.init_app(App)
configuration.load_extensions(App)
App.secret_key = os.urandom(16)
def M340():
    ton1=Timer()
    while True:
        ton1.Ton(5)
        if ton1.Q:
            if Unity_Read("%MW203",1) != "erro" :

                if Unity_Read("%MW203",1)[0]==1:
                    Atualiza(Unity_Read("%MW300",9))
                elif Unity_Read("%MW204",1)[0]==1:
                    Atualiza(Unity_Read("%MW300",9))
                    Fechar()
                    Unity_Write("%MW202",1)
                    Unity_Write("%MW202",0)
    
threading.Thread(target=M340).start()
App.run(port=5001)









    