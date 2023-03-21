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



