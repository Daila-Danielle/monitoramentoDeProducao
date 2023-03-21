# blibiotecas
from flask import flash,request,session,url_for,redirect,render_template
from werkzeug.utils import secure_filename
from pathlib import Path
import os
import bcrypt
#importa as APIs Usuarios,Login e seus metodos
from Apis import Usuarios,Login,Producao,Dados_producao

#gera chave para cryptografia
chave = bcrypt.gensalt()

 
#caminho padrão para imagens do prefil

UPLOAD_FOLDER = Path(__file__).parent.parent/"static\imagens\Perfil"
print(UPLOAD_FOLDER)

# gera a instancia do app para não causar circular inport
def init_App(App):

#rotas tipo POST
#rota recebe os dados da paginha de login e verifica se estão corretos
    @App.route('/logar',methods=["POST"])
    def logar():
        nome = request.form['nome']
        senha = request.form['senha']

        resp=Login.post_login(nome,senha)

        if  resp== 1:
            session['username'] = nome
            session['userdados'] = Usuarios.get_usuario(session['username'])
            return redirect(url_for('index'))

        elif  resp== 2:
            print('nao ok')
            flash('Senha incorreta')
            return  redirect(url_for('login'))

        elif  resp== 0:
            flash('Usuario nao encontrado')
            return  redirect(url_for('login')) 


#rota recebe os dados da paginha de cadastro de usuarios e adiciona 
    @App.route('/dashboard/Add_usuario',methods=["POST"])
    def add_usuario():

        nome = request.form['nome']
        senha= request.form['senha'].encode('utf-8')
        cargo=request.form['cargo']
        grupo= request.form['grupo']
        arquivo = request.files['imagem']
            
        if arquivo.filename == "":
            arquivo.filename = "padrao.jpeg"
            filename = secure_filename(arquivo.filename)
        else:    
            filename = secure_filename(arquivo.filename) 
            arquivo.save(os.path.join(UPLOAD_FOLDER,filename))

        hash = bcrypt.hashpw(senha,chave)
        Usuarios.post_usuario(nome,hash.decode(),cargo,grupo,filename)
            
        flash('Usuario Cadastrado')
        return  redirect(url_for('login'))
    
    @App.route('/dashboard/Inicia_producao',methods=["POST"])
    def inicia_producao():

        material=[]
        material.append(request.form['mat1'])
        material.append(request.form['mat2'])
        material.append(request.form['mat3'])
        material.append(request.form['mat4'])
        material.append(request.form['mat5'])
        material.append(request.form['mat6'])
        material.append(request.form['mat7'])
        material.append(request.form['mat8'])
        material.append(request.form['mat9'])

        mat_id=[3256,5698,6328,4568,9746,3265,9864,9875,6548]
       
       
        Producao.post_Production(material,mat_id)

        return  redirect(url_for('index',formInicioProducao ='none',formFimProducao ='block',ultimasProducao ='none',status = '1'))
    

    @App.route('/dashboard/delete_producao',methods=["POST"])
    def delete_producao():

        id = request.form['id']
        print(id)
        Producao.delete_Production(id)   
        return  redirect(url_for('relatorios'))
    

    @App.route('/dashboard/filtar',methods=["POST"])
    def filtar_producao():

        dt_inicial = request.form['dt_inicial']
        dt_final = request.form['dt_final']

        return render_template('relatorios.html',valores=Dados_producao.get_Dados_producao(dt_inicial,dt_final))
        
    





    
   

    
    
        
                    
