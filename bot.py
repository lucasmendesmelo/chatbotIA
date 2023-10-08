from selenium import webdriver
import time
import os
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import requests
import openai



# Obtém o diretório atual
dir_path = os.getcwd()

# Configura as opções do ChromeDriver com o perfil de usuário
chrome_options = Options()
chrome_options.add_argument(f'user-data-dir={dir_path}/profile/zap')

# Inicializa o navegador com as opções configuradas
driver = webdriver.Chrome(options=chrome_options)


driver.get('https://web.whatsapp.com/')


time.sleep(10)



####   

def bot():

    try:
       
        notificacao = driver.find_element(By.CLASS_NAME,"_2H6nH")
        notificacao= driver.find_elements(By.CLASS_NAME,"_2H6nH")
        clica_notificacao = notificacao[-1]
        acao_notificacao =  webdriver.common.action_chains.ActionChains(driver)
        acao_notificacao.move_to_element_with_offset(clica_notificacao,0,-20)
        acao_notificacao.click()
        acao_notificacao.perform()
        acao_notificacao.click()
        acao_notificacao.perform()

       
        todas_as_msg = driver.find_elements(By.CLASS_NAME,"_21Ahp")
        todas_as_msg_texto = [e.text for e  in todas_as_msg]
        msg = todas_as_msg_texto[-1]
        


        cliente = 'mensagem do cliente:'
        texto2 = 'Responda a mensagem do cliente com base no proximo texto'
        texto = 'explique tudo sobre A Agência Digital MaxResults é especializada em marketing digital e visa impulsionar o sucesso online das empresas. Com uma equipe experiente, oferecemos serviços abrangentes, desde otimização de mecanismos de busca (SEO) até campanhas de pagamento por clique (PPC) e marketing de conteúdo. Nossos casos de sucesso demonstram nosso compromisso em alcançar resultados impactantes. Para começar a transformar sua presença online, entre em contato conosco pelo telefone (11) 9876-5432 ou por email (info@agenciamaxresults.com). Seja qual for o seu objetivo de marketing digital, estamos aqui para ajudar a atingi-lo. Junte-se a nós e veja a diferença que podemos fazer para o seu negócio.'
        questao = cliente + msg + texto2 + texto
        ####PROCESSA A MENSAGEM NA API ia

        openai.api_key = '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'

        response = openai.Completion.create(
        model="text-davinci-003",
        prompt=questao,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
        )
        resposta = response['choices'][0]['text']
        
        time.sleep(3)


        #RESPONDE A MSG
        campo_de_texto = driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div[5]/div/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p")
        campo_de_texto.click()
        time.sleep(3)
        campo_de_texto.send_keys(resposta,Keys.ENTER)
        time.sleep(2)    




        #FECHA O CONTATO
        webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()         
  






    except:
        print('')

while True:

    bot()       

     


        


