# blibiotecas
from flask import render_template,session,url_for,redirect,request
#importa a API Dados_cadastro e seus metodos
from Apis import Dados_cadastro,Dados_producao,Dados_producao_detalhar,Producao,Valores
from datetime import datetime

# gera a instancia do app para não causar circular inport
formInicioProducao = 'block'
formFimProducao ='none'
ultimasProducao = 'block'
def init_App(App):


#rotas tipo GET
#rota pagina de Login
    @App.route('/')
    def login():
        return render_template('login.html')

#rota pagina inicial
    @App.route('/dashboard')
    def index():
        val=[]
        msg=""
        if 'username' in session:
            user_dados = session['userdados']
            
            status = request.args.get('status')  
            caixa = Valores.get_Valores()

            if caixa[9] == 0:
                msg="Produçao Finalizada"
            
            if status == '1':
                formInicioProducao= request.args.get('formInicioProducao')
                formFimProducao= request.args.get('formFimProducao')
                ultimasProducao= request.args.get('ultimasProducao')
            else:
                formInicioProducao ='block'
                formFimProducao ='none'
                ultimasProducao ='block'
            status = '0'
            valores=Dados_producao.get_Dados_producao("","")

            iteracao = len(valores)
            if iteracao > 4:
                iteracao = 4
           
            for x in range(iteracao):
                    val.append(valores[x])
            
            return render_template('index.html',user_nome=user_dados[0]['nome'],img_nome = user_dados[0]['img_nome'],user_tipo = user_dados[0]['tipo'],valores=val, formInicioProducao = formInicioProducao, formFimProducao = formFimProducao,ultimasProducao = ultimasProducao,caixa = caixa,mensagem=msg)
        else:
            return redirect(url_for('login'))
        
#rota para logout
    @App.route('/logout')
    def logout(): 
        session.pop('username')
        return redirect(url_for('login'))
    
#rota para pagina de cadastro de usuarios 
    @App.route('/dashboard/cadastrar_usuario')
    def cadastro_usuario():
        if 'username' in session:
            Cad_dados = Dados_cadastro.get_Dados_cadastro()
            return render_template('cadastro_usuario.html',cargos=Cad_dados[0]["cargos"],grupos=Cad_dados[1]["grupos"])
        else:
            return redirect(url_for('login'))
        
#rota para pagina de edição do perfil
    @App.route('/dashboard/perfil')
    def perfil_usuario():
        if 'username' in session:
            Cad_dados = Dados_cadastro.get_Dados_cadastro()
            return render_template('perfil_usuario.html',cargos=Cad_dados[0]["cargos"],grupos=Cad_dados[1]["grupos"])
        else:
            return redirect(url_for('login'))

#rota para pagina de graficos
    @App.route('/dashboard/graficos')
    def graficos():
        if 'username' in session:
           
            return render_template('graficos.html')
        else:
            return redirect(url_for('login'))
    
#rota para pagina de relatorios
    @App.route('/dashboard/relatorios') 
    def relatorios():
        if 'username' in session:
    
            return render_template('relatorios.html',valores=Dados_producao.get_Dados_producao("",""))
        else:
            return redirect(url_for('login'))
    
    @App.route('/dashboard/finalizar') 
    def finalizar_prod():
        if 'username' in session:

            Producao.put_Production("atualizar")


            return redirect(url_for('index'))
        else:
            return redirect(url_for('login'))


    @App.route('/dashboard/relatorio/detalhar')
    def detalhar_producao():

        if 'username' in session:
            id = request.args.get('prod_id')
            return render_template('relatorios_detalhar.html',valores=Dados_producao_detalhar.get_dados_producao_detalhar(id),valorTotal=Dados_producao.get_Dados_producao("",""))
        else:
            return redirect(url_for('login'))
 
    @App.template_filter('to_date')
    def format_datetime(value):
        if value == 'None':
            return '-'
        dt = datetime.strptime(value, '%Y-%m-%d %H:%M:%S')
        return dt.strftime("%d/%m/%Y %H:%M:%S" )