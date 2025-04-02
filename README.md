Aplicativo de Lista de Tarefas

Este projeto consiste em uma aplicação para gerenciamento de tarefas, estruturada de forma modular para promover a reutilização e organização do código.

Tecnologias Utilizadas

Backend: FastAPI

Banco de Dados: OracleDB

Frontend: HTML5

Como Executar o Projeto

Para executar o projeto localmente, siga as instruções abaixo:

Criar um ambiente virtual

python -m venv venv

Ativar o ambiente virtual

venv\Scripts\activate  # No Windows
source venv/bin/activate  # No Linux/Mac

Instalar as dependências

pip install -r requirements.txt

O arquivo requirements.txt contém todas as bibliotecas necessárias para o funcionamento da aplicação.

Criar o arquivo .env
Dentro do diretório raiz do projeto, crie um arquivo chamado .env e adicione as seguintes informações:

ORACLE_USER=seu_usuario
ORACLE_PASSWORD=sua_senha
ORACLE_DSN=seu_host

Exemplo de ORACLE_DSN: localhost:1234/xepdb1 ou xe.

Iniciar o projeto

python main.py

Esse comando iniciará a API, tornando o sistema disponível para uso.

Estrutura do Projeto

.
├── main.py                # Arquivo principal para execução da aplicação
├── models/                # Definição das tabelas e conexão com o banco de dados
├── routes/                # Configuração das rotas do FastAPI
├── templates/             # Arquivos HTML utilizados no frontend
├── controller/            # Lógica de interação com os modelos de dados
└── .env                   # Credenciais do banco de dados (não incluído no repositório por segurança)

Observação Importante

Para utilizar este projeto, é necessário possuir uma conta no Oracle Database e configurar corretamente o arquivo .env.
