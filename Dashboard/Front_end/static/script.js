var id = 0

'Função para trocar a classe no item do  menu lateral para destacar o munu ativo'
function trocaClasse(elemento,nova) 
{
    teste=document.getElementById(elemento);
    teste.classList.add(nova);
} 



'Função guardas os dados do login no navegador para ser usado em outra pagina'
function User_dados_gavar(name,tipo,img) 
{
    localStorage.setItem('user_nome',name);
    localStorage.setItem('user_tipo',tipo);
    localStorage.setItem('user_img',img);   
    if (tipo!= 45) {document.getElementById('adm').style.display = 'none';} 
    document.getElementById("user_img").src = img;
} 



'Função Le os dados do login no navegador para ser usado na pagina'    
function User_dados_ler() 
{
    document.getElementById("user").textContent = localStorage.getItem('user_nome');
    document.getElementById("user_img").src = localStorage.getItem('user_img');
    if(localStorage.getItem('user_tipo')!= 45) {document.getElementById('adm').style.display = 'none';}
}

    

function modal_delete_block(id_)
{
    id=id_
    document.getElementById("modal_id").innerText = id;
    document.getElementById("modal_delete").style.display="block";
} 


function modal_delete_none()
{
    document.getElementById("modal_delete").style.display="none";
} 


function modal_delete_ok()
{
    document.getElementById("id_del").value = id
    document.getElementById("form_delete").submit();
} 

function iniciaProducao() {
    var selecionaProducao = document.getElementById('selecionaProducao');
    var producao = document.getElementById('producao');
    var form = document.getElementById('form');
    selecionaProducao.style.display = "none";
    form.submit();
    producao.style.display = "block";
}


function toggleTheme() {
    const body = document.querySelector('body');
    const button = document.querySelector('#theme-toggle');
  
    if (body.classList.contains('dark-mode')) {
      body.classList.remove('dark-mode');
      body.classList.add('light-mode');
      button.textContent = 'Modo noturno';
      localStorage.setItem('theme', 'light');
    } else {
      body.classList.remove('light-mode');
      body.classList.add('dark-mode');
      button.textContent = 'Modo claro';
      localStorage.setItem('theme', 'dark');
    }
  }
  
  // Verifica o tema atual ao carregar a página
  function checkTheme() {
    const body = document.querySelector('body');
    const button = document.querySelector('#theme-toggle');
    const theme = localStorage.getItem('theme');
    if (theme === 'dark') {
      body.classList.remove('light-mode');
      body.classList.add('dark-mode');
      button.textContent = 'Modo claro';
    } else {
      body.classList.remove('dark-mode');
      body.classList.add('light-mode');
      button.textContent = 'Modo noturno';
    }
  }
function confirmaSenha() {
  var senha = document.getElementById("senha").value;
  var confirmacaoSenha = document.getElementById("confirmar-senha").value;
  var mensagemErro = document.querySelector("#confirmar-senha + .invalid-feedback");
  if(senha !== confirmacaoSenha){
    mensagemErro.style.display = "block";
  } else {
    mensagemErro.style.display = "none";
  }
}

function formatarData(dataString) {
  const data = new Date(dataString);
  const dia = String(data.getDate()).padStart(2, '0');
  const mes = String(data.getMonth() + 1).padStart(2, '0');
  const ano = data.getFullYear();
  const hora = String(data.getHours()).padStart(2, '0');
  const minuto = String(data.getMinutes()).padStart(2, '0');
  const segundo = String(data.getSeconds()).padStart(2, '0');
  return `${dia}/${mes}/${ano} ${hora}:${minuto}:${segundo}`;
}