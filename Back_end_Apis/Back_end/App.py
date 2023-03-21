#blibiotecas
from M340.Utils.Temporizadores import Timer
from M340.Main.Unity_com import Unity_Read,Unity_Write
from flask import Flask
import threading
import configuration


App = Flask(__name__)
configuration.init_app(App)
configuration.load_extensions(App)


def M340():
    ton1=Timer()
    while True:
        ton1.Ton(5)
        if ton1.Q:
            Unity_Read()


        
                       
threading.Thread(target=M340).start()



App.run(port=5001)








    