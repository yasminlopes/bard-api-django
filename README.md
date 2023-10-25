# Chatbot com IA utilizando Django e Google Bard API

Este é um projeto de chatbot desenvolvido com uma API REST em Django utilizando a biblioteca [Google Bard](https://pypi.org/project/bardapi/). O chatbot é capaz de responder perguntas de forma precisa, permitindo também a continuação da conversa através do ID da conversa. Além disso, o projeto possui um histórico de conversas armazenado em memória.

## Funcionalidades

- Perguntas e Respostas (QA): Faça perguntas e obtenha respostas precisas da inteligência artificial.
- Histórico: Visualize o histórico de conversas identificado pelo ID da conversa.
- Continuação da conversa: Continue a conversa fazendo novas perguntas com base no ID da conversa.

## Como executar o projeto

Siga as instruções abaixo para executar o projeto em sua máquina local:

1. Clone este repositório para sua máquina local.
2. Certifique-se de ter o Python 3.x instalado em seu ambiente.
3. Instale o Django executando o seguinte comando:
```
pip install django
```
4. Ative o ambiente virtual com os seguintes comandos:
```
python -m venv myvenv
.\venv\Scripts\activate
```
5. Instale as dependências do projeto:
```
pip install -r requirements.txt
```
6. Substitua as variaveis de ambiente
   - Acesse https://bard.google.com/. Pressione F12 para abrir o console do navegador.
   - Vá em "Application" > "Cookies"
   - Procure pelos cookies "__Secure-1PSID" e "__Secure-1PSID_TS", copie o valor desses cookies
   - Crie um arquivo .env e adicione o valor nas variaveis obtidas pelo arquivo .env.sample
8. Navegue até a pasta "bard_api" e inicie o servidor com o seguinte comando:
```
cd bard_api
python manage.py runserver
```
O servidor será iniciado na porta 8000.

## Front-end

Além disso, criei a parte visual da aplicação utilizando o framework Angular. Por enquanto, a aplicação possui apenas a funcionalidade de Perguntas e Respostas.

Você pode encontrar o código do front-end [aqui](https://github.com/yasminlopes/chatbot-angular).
