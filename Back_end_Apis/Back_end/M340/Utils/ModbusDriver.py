
from pyModbusTCP.client import ModbusClient

cliente = ModbusClient('10.62.1.70',502,1,0.1)

class driver:
   
   def Read(self,addr="",qtd=1):
      if cliente.open():
            addr=addr.removeprefix("%MW")
            addr=int(addr)
            Dados=cliente.read_holding_registers(addr,qtd) 
            cliente.close() 
            return Dados
      else:
            cliente.close()
            print("server não encontrado")
      
        


   def Write(self,addr="",dados=0):
       
      if cliente.open():
            addr=addr.removeprefix("%MW")
            addr=int(addr)
            cliente.write_single_register(addr,dados) 
            cliente.close() 
         
      else:
            cliente.close()
            print("server não encontrado")
      



   


   
















        
   




