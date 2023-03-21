from ..Utils.ModbusDriver import driver

M340=driver()
def Unity_Read():
    print("Reading")



def Unity_Write(addr,valor):
    M340.Write(addr,valor)
    