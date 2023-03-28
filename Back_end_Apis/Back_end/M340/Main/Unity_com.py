from ..Utils.ModbusDriver import driver

M340=driver()
def Unity_Read(addr,qtd):
    return(M340.Read(addr,qtd))


def Unity_Write(addr,valor):
    M340.Write(addr,valor)
    