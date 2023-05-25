# Projeto Projeto Análise de Dados com CRUD e Flask

Este é um projeto Flask que implementa operações CRUD (Create, Read, Update, Delete) em uma lista de clientes usando um banco de dados MySQL. Ele fornece uma interface web para visualizar, adicionar, atualizar e excluir clientes.

## Pré-requisitos

- Python 3.x
- Flask
- Flask-MySQLdb (ou outra biblioteca compatível com MySQL)
- MySQL Server
- Database northwind-data.sql

## Configuração

1. Clone o repositório para o seu ambiente local ou baixe o zip do projeto

2. Instale as dependências do projeto:
pip install -r requirements.txt

3. Configure o MySQL com o banco de dados e as informações do banco de dados no arquivo `app.py`. Certifique-se de fornecer as informações corretas do host, usuário, senha e banco de dados.

4. Execute o aplicativo:
python app.py

5. Acesse o aplicativo no seu navegador em `http://localhost:5000`.

## Funcionalidades

- Faça o login com a credenciais que deixei prontas (Usuário: guest / Senha: 1234) ou crie suas prórpias credencias e acesse para:

- Listagem de clientes: exibe todos os clientes cadastrados no banco de dados.
- Adição de cliente: permite adicionar um novo cliente ao banco de dados.
- Atualização de cliente: permite atualizar as informações de um cliente existente.
- Exclusão de cliente: permite excluir um cliente do banco de dados.

## Contribuição

Contribuições são bem-vindas! Se você quiser melhorar este projeto, sinta-se à vontade para enviar pull requests.

## Licença

Este projeto está licenciado sob a [EASIER License](LICENSE).