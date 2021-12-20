# importar as bibliotecas
from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
# navegar até o whatsapp web
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://web.whatsapp.com/')
time.sleep(20)
#Definir contato que a menságem será enviada
contatos = ['CLAS -LAIANE CARINE DE SOUZA FLORIM',	'CLAS -LADY DAIANA RODRIGUES DE OLIVEIRA',	'CLAS -AMANDA JULIANA SALES',	'CLAS -LETICIA MARIA AMADO',	'CLAS -OTACILIO JUNIO MELO DE CARVALHO',	'CLAS -FELIPE BRUNO DE SOUZA',	'CLAS -FLÁVIA STÉPHANIE SIMÕES FARIA',	'CLAS -FRANCIELE CRISTINA MOURA CECÍLIO',	'CLAS -MAICON MELONI DA SILVA',	'CLAS -CARLOS EDUARDO NAGY',	'CLAS -LARISSA DOS SANTOS ROCHA',	'CLAS -GABRIEL DE OLIVEIRA PIO',	'CLAS -FRANCIANE FERNANDA BRUSCHI',	'CLAS -BETHANIA SIDHARTA GALVAO NICOLINI',	'CLAS -ELIZANDRA SANTOS BORGES',	'CLAS -BEATRIZ DE ALMEIDA DA ROCHA RIBEIRO',	'CLAS -THULIO JOSÉ PEREIRA',	'CLAS -LUIZ GUSTAVO FERREIRA ALVES DA SILVA',	'CLAS -PALOMA CASTRO OLIVEIRA DE SOUZA',	'CLAS -MATHEUS GASTALDI LIMA',	'CLAS -ALESSANDRA CORREA',	'CLAS -MARIA JOSE NORBERTO FECHETIA',	'CLAS -IVONE ANTUNES FERREIRA',	'CLAS -EDILAINE BRITO ARAÚJO DE OLIVEIRA',	'CLAS -MONIQUE DA SILVA SANTOS',	'CLAS -BEATRIZ CRISTINA ALVES DA SILVA',	'CLAS -ROBERTA SOARES DE OLIVEIRA BOTELHO',	'CLAS -APARECIDA MARIA DE OLIVEIRA MARTINS',	'CLAS -NEUSA DE ALENCAR CAETANO',	'CLAS -KAREN ALINE DE QUEIROZ SANTANA',	'CLAS -BRUNO COSTA MARTINS',	'CLAS -AMANDA ESPINOSSA CORREIA PORTO',	'CLAS -BARBARA GABRIELLE NESOTTO',	'CLAS -FABIANA PAES DE SOUZA',	'CLAS -FERNANDO PINHEIRO CREMONEZ',	'CLAS -ANDRÉ MARCELO RUIZ',	'CLAS -ERIZALDA MARIA DA SILVA SANTOS',	'CLAS -FABRIZIO PIETTRO DA SILVA MAGRO',	'CLAS -EVERTON PAULO DOS SANTOS',	'CLAS -BEATRIZ CRISTINA PEREIRA ALEXANDRE',	'CLAS -LUIZA FRANCO DOS SANTOS',	'CLAS -THIAGO ANDERSON SESSO CARDOSO DA SILVA',	'CLAS -ANA PAULA MIGUEL',	'CLAS -WILLIAN FELIPE TOMÉ',	'CLAS -MURILO VINICIUS OLIVEIRA CARVALHO',	'CLAS -DIEGO RAFAEL RODRIGUES',	'CLAS -SARA MIQUELINO CARVALHO',	'CLAS -RENATO DE OLIVEIRA DIAS',	'CLAS -JOSÉ FERNANDO SILVEIRA',	'CLAS -CLAUDIA DE ANDRADE BERNARDI',	'CLAS -STEFANIE CAROLINE MAYUMI MIZUNO',	'CLAS -GABRIEL SOARES CAIRES',	'CLAS -JOÃO PEDRO DINARDI',	'CLAS -LORENA BEATRIZ CORRÊA DE OLIVEIRA SOUZA',	'CLAS -SANDRA NOGUEIRA',	'CLAS -ADILSON THIEZERINI JUNIOR',	'CLAS -CRISTIANE APARECIDA ROSSATTI',	'CLAS -LUIZ PAULO BARONI JUNIOR',	'CLAS -MARIANA DA COSTA ZANIBONI',	'CLAS -DANIEL ANDRE DA SILVA',	'CLAS -TÁRIK AUGUSTO SILVA CORREA',	'CLAS -ISABELA MASSARO RODRIGUES SARGENTO',
]
mensagem = 'Boa tarde *Futuro Aluno* Espero que estejam bem e se cuidando ! \n Venho para saber se consigo te ajudar a concluir sua *matrícula*. Lembrando que é bem simples, basta acessar o portal: *https://estacio.br/candidato* \n Fazer o pagamento da *primeira mensalidade*, enviar os *documentos necessários*(CPF; RG e Declaração de Conclusão do Ensino Médio) e dar *Aceite no Contrato Educacional*, tudo isso através do site ! \n Fácil né? \n Caso esteja com alguma dificuldade, ou alguma dúvida, estou à disposição para te ajudar ! \n Aguardamos você !'
# buscar contatos
def buscar_contato(contato):
    campo_pesquisa = driver.find_element_by_xpath(
        '//div[contains(@class,"copyable-text selectable-text")]')
    time.sleep(3)
    campo_pesquisa.click()
    campo_pesquisa.send_keys(contato)
    campo_pesquisa.send_keys(Keys.ENTER)

def enviar_mensagem(mensagem):
    campo_mensagem = driver.find_elements_by_xpath(
        '//div[contains(@class,"_2_1wd copyable-text selectable-text")]')
    campo_mensagem[1].click()
    time.sleep(3)
    campo_mensagem[1].send_keys(mensagem)
    campo_mensagem[1].send_keys(Keys.ENTER)

for contato in contatos:
    buscar_contato(contato) 
    enviar_mensagem(mensagem)
    #campo de pesquisa 'copyable-text selectable-text'
# campo de mensagem privada 'copyable-text selectable-text'
# Enviar menssagem desejada 