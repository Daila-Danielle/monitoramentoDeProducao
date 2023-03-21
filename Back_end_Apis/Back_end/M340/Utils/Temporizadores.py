import time
class Timer:
    def __init__(self) :
        self.tempo = time.time()
        self.Q = False
        self.R = False

    def Ton (self,IN):
        if time.time() > (self.tempo + IN):
            self.tempo = time.time()
            self.Q = True
        else: 
            self.Q = False

    def TonR (self,IN):
        if time.time() > (self.tempo + IN):
            self.tempo = time.time()
            self.Q = True
        if self.R == True :
            self.Q = False
            self.R = False

       