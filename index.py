from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import requests
import reCAPTCHA

driver = webdriver.Chrome('seu_caminho_para_o_driver/chromedriver')

try:
    def resolve_recaptcha(driver):
        recaptcha_site_key = '6Lc_aTMTAAAAABk9zY8qyWf0IbFjRnMvQmHxPpU'
        recaptcha_url = 'https://www.google.com/recaptcha/api/siteverify'

        token = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, 'g-recaptcha-response'))
        ).get_attribute('value')

        recaptcha_response = reCAPTCHA.solve(token, recaptcha_url, recaptcha_site_key)

        driver.execute_script("""
            document.getElementById('g-recaptcha-response').innerHTML = '{}';
        """.format(recaptcha_response))

    driver.get("https://www.nfe.fazenda.gov.br/portal/consultaRecaptcha.aspx?tipoConsulta=resumo&tipoConteudo=7PhJ+gAVw2g=")
    
    resolve_recaptcha(driver)
    
    chave_acesso_input = driver.find_element_by_id('ctl00_ContentPlaceHolder1_txtChaveAcesso')
    chave_acesso_input.send_keys('SUA_CHAVE_DE_ACESSO')
    
    chave_acesso_input.send_keys(Keys.RETURN)
    
    time.sleep(5)
    
    try:
        mensagem_validade = driver.find_element_by_css_selector('seletor_para_mensagem_de_validade')
        if 'Nota Fiscal válida' in mensagem_validade.text:
            print("Nota Fiscal é válida.")
        else:
            print("Nota Fiscal inválida ou não encontrada.")
            #return  
    except Exception as e:
        print(f"Erro ao verificar validade da nota fiscal: {e}")
            #return
    
    dados_nota_fiscal = {}
    try:
        dados_nota_fiscal['emitente'] = driver.find_element_by_css_selector('seletor_para_emitente').text
        dados_nota_fiscal['destinatario'] = driver.find_element_by_css_selector('seletor_para_destinatario').text
        dados_nota_fiscal['valor_total'] = driver.find_element_by_css_selector('seletor_para_valor_total').text
    except Exception as e:
        print(f"Erro ao coletar dados da nota fiscal: {e}")
    
    url_api_sistema_empresa = 'http://api.sistemadaempresa.com/notas'
    headers = {'Content-Type': 'application/json', 'Authorization': 'Bearer SEU_TOKEN_API'}
    response = requests.post(url_api_sistema_empresa, json=dados_nota_fiscal, headers=headers)

    if response.status_code == 200:
        print("Dados inseridos com sucesso.")
    else:
        print(f"Erro ao inserir dados: {response.text}")
    
    try:
        link_download = driver.find_element_by_css_selector('seletor_para_link_de_download').get_attribute('href')
        nome_arquivo = link_download.split('/')[-1]
        
        resposta_download = requests.get(link_download)
        with open(nome_arquivo, 'wb') as f:
            f.write(resposta_download.content)
        
        print(f"Nota fiscal baixada com sucesso: {nome_arquivo}")
    except Exception as e:
        print(f"Erro ao baixar nota fiscal: {e}")

finally:
    driver.quit()
