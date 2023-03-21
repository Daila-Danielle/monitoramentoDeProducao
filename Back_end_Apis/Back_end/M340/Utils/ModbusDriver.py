
from pyModbusTCP.client import ModbusClient
import json


cliente = ModbusClient('192.168.100.122',502,1,0.05)

class driver:
   def __init__(self,source):
      self.source = source
      pass


   def Read(self):
      with open(self.source,'r') as Tags_Json:
         Tags = json.load(Tags_Json)
      if cliente.open():
         for Equipamento in Tags:
            addr=int(Tags[Equipamento]["Adrres"]["ADDR"].removeprefix("%MW"))
            read = cliente.read_holding_registers(addr,len(Tags[Equipamento]["Tags"])) 
            cliente.close()
            interacao=0
            for itens in Tags[Equipamento]["Tags"]:
               Tags[Equipamento]["Tags"][itens] = read[interacao]
               interacao =+1
         with open(self.source,'w') as Tags_Json:
            json.dump(Tags,Tags_Json) 
      else:
         cliente.close()
         print("server não encontrado")
      return Tags
               


   def Write(self,dados):
      Tags = dados
      if cliente.open():
         for Equipamento in Tags:
            addr=int(Tags[Equipamento]["Adrres"]["ADDR"].removeprefix("%MW"))
            interacao =0
            for itens in Tags[Equipamento]["Tags"]:
               cliente.write_single_register(addr+interacao,Tags[Equipamento]["Tags"][itens]) 
               interacao =+1
               cliente.close() 
         with open(self.source,'w') as Tags_Json:
            json.dump(dados,Tags_Json)
      else:
            cliente.close()
            print("server não encontrado")
      



   


   
















        
   




