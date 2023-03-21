#blibiotecas
import mysql.connector

# classe para o banco de dados
class DB :
    # variaves para conexão e querys
    def __init__(self,Source={}):
        self._host = Source['host']
        self._user = Source['user']
        self._senha = Source['password']
        self._database = Source['database']
        self._debug = Source['debug']

        self.query = "Vazio"
        self.rowcount = 0
        self.erro =("Sem Erro")
     
    #funcão para executar uma query do tipo DML,DDL
    def execute(self,sql,valores):
        self.query = "Vazio"
        self.erro =("Sem Erro")

        DBcon = mysql.connector.connect(
        host = self._host,
        database = self._database,
        user = self._user,
        password= self._senha )

        cursor = DBcon.cursor()

        try:
            cursor.execute(sql,valores)
            DBcon.commit()
            self.query = cursor.fetchall()
            self.rowcount = cursor.rowcount
            cursor.close
            DBcon.close

        except Exception as er:
            self.erro = er
            DBcon.close

        if self._debug == "true":
            print("Query_Executada:",sql,valores)
            print("Query_RowCount:",self.rowcount)
            print("Query_Resultado:",self.query)
            print("Query_Erro:",self.erro)

    #funcão para executar uma query do tipo DQL (select)
    def execute_select(self,sql,valores=0):
        self.query = "Vazio"
        self.erro =("Sem Erro")
       

        DBcon = mysql.connector.connect(
        host = self._host,
        database = self._database,
        user = self._user,
        password= self._senha
            )
        
        cursor = DBcon.cursor()

        try:
            if valores == 0: 
                cursor.execute(sql)
                self.query = cursor.fetchall()
                self.rowcount = cursor.rowcount
                cursor.close
                DBcon.close
            else:
                cursor.execute(sql,valores)
                self.query = cursor.fetchall()
                self.rowcount = cursor.rowcount
                cursor.close
                DBcon.close

        except Exception as er:
            self.erro = er  
            DBcon.close

        if self._debug == "true":
            print("Query_Executada:",sql,valores)
            print("Query_RowCount:",self.rowcount)
            print("Query_Resultado:",self.query)
            print("Query_Erro:",self.erro)