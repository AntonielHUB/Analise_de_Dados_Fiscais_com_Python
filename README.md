# Projeto de Extensão - Tópicos de Big Data em Python.

## Objetivo
- Aplicação criada para um projeto de extensão da Faculdade UNESA (Universidade Estácio de Sá). O tema aborda a criação de uma aplicação que faz uso de algumas bibliotecas em Python para buscar dados fiscais na Fazenda e pegar os resultados das notas fiscais, bem como gerar um PDF do conteúdo adquirido.

## Funcionalidades
- Aplicação feita em um projeto Python utilizando bibliotecas como Selenium, Requests e PyreCAPTCHA.
- Gerenciar, de forma eficiente, os dados obtidos.
- Exercer controle avançado sobre recursos de automação em funções repetitivas.
- Manipular aspectos técnicos fundamentais na aquisição de dados de terceiros.
- Regular detalhes técnicos essenciais, como o que fazer com os dados obtidos, bem como a forma de armazenar tais dados.

## bibliotecas
 1 Selenium
- 	Propósito: Selenium é uma ferramenta de automação de navegador que permite controlar navegadores web (como Chrome, Firefox, Safari) através de scripts escritos em Python (ou outras linguagens suportadas). Isso é útil para automação de tarefas repetitivas no navegador, como preenchimento de formulários, navegação entre páginas, e extração de dados de sites.
- 	Motivo da Instalação: No contexto do seu script, o Selenium é usado para abrir o navegador, navegar até a página desejada, interagir com elementos da página (como campos de texto, botões etc.), e extrair informações.

 2 Requests
- 	Propósito: A biblioteca Requests é uma interface simplificada para fazer requisições HTTP em Python. Ela permite enviar solicitações GET, POST, PUT, DELETE, entre outras, facilitando a comunicação com APIs web ou o download de arquivos.
- 	Motivo da Instalação: No seu script, o Requests é utilizado para enviar dados coletados (como informações da nota fiscal) para um servidor externo via API. Também pode ser usado para baixar arquivos diretamente do servidor.

 3  PyreCAPTCHA
- 	Propósito: PyreCAPTCHA é uma biblioteca Python que ajuda a resolver CAPTCHAs, especificamente o reCAPTCHA, que é uma forma popular de proteger sites contra bots e spam. Ela pode ser usada para automatizar a resolução desses desafios, o que é crucial em situações em que a interação manual com CAPTCHAs não é viável.
- 	Motivo da Instalação: No seu script, o PyreCAPTCHA é utilizado para resolver o reCAPTCHA presentes nas páginas que você está acessando com o Selenium. Isso permite que o script prossiga sem interrupções manuais, mantendo a automação eficiente.

## Importações e Configuração Inicial
- Importações: O código importa as bibliotecas necessárias para realizar a automação web com Selenium, manipulação de tempo com time, requisições HTTP com requests, e a solução de reCAPTCHA com reCAPTCHA.
- Configuração inicial: Define o caminho para o driver do navegador (ChromeDriver neste caso), que é necessário para que o Selenium possa controlar o navegador.

 <p align="center">
  <img src="https://cdn.discordapp.com/attachments/1046815809227468832/1266379573352992840/Screenshot_2024-07-25_at_16.27.32.png?ex=66a4ef62&is=66a39de2&hm=1c6bac31bcaed7710264ba03e1493ba6508ed5d3e2cc54eb879cedccfdc8c633&" alt="Descrição da imagem">
</p>

## Função para resolver o reCAPTCHA
- Esta função é responsável por resolver o reCAPTCHA presente na página da SEFAZ. Ela obtém o token do reCAPTCHA, resolve-o usando a biblioteca reCAPTCHA, e então atualiza o elemento HTML do reCAPTCHA com o token resolvido.

## Execução Principal
- Abertura da página: O script abre a página de consulta da SEFAZ usando o Selenium WebDriver.
-	Resolução do reCAPTCHA: Chama a função resolve_recaptcha para resolver o reCAPTCHA automaticamente.
-	Inserção da chave de acesso: Localiza o campo de entrada da chave de acesso e insere a chave fornecida.
-	Envio da consulta: Simula o pressionamento de tecla Enter para enviar a consulta.

## Verificação da Validade da Nota Fiscal
- Verificação da validade: Tenta encontrar uma mensagem na página que indique se a nota fiscal é válida. Se a nota for válida, o script continua; caso contrário, ele encerra a execução.

## Coleta de Dados
- Extrai informações relevantes da nota fiscal, como emitente, destinatário e valor total.

## Inserção de Dados no Sistema da Empresa
-  Faz uma requisição POST para a API da empresa, enviando os dados coletados da nota fiscal.

## Download da Nota Fiscal
-  Localiza o link de download da nota fiscal, realiza o download e salva o arquivo no sistema local.

## Finalização
-  Fecha o navegador controlado pelo Selenium, finalizando a execução do script.
 <p align="center">
  <img src="https://cdn.discordapp.com/attachments/1046815809227468832/1266379610174783518/Screenshot_2024-07-25_at_16.27.56.png?ex=66a4ef6b&is=66a39deb&hm=0407c277477eb36f33430a46ba435ae3c22d4b42f11adf6e5455de2d2fdaa3f1&" alt="Descrição da imagem">
</p>
