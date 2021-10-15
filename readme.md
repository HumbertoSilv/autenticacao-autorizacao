# Manual da API

Aplicação capaz de realizar um CRUD completo de um usuário usando SQLAlchemy, Dataclass, Blueprint, Migrations e Padrão Flask Factory.

1. Clone o repositório e em um ambiente virtual instale todas as dependências que 
estão no arquivo "requirements.txt".

2. Rode o Migrate.

3. Inicie a aplicaçao com o comando:
<!-->
    $ flask run
<!-->

# Rotas
## Cadastrar usuário:
POST http://{BASE_URL}/api/signup

```json
{
    "name": "John",
    "last_name": "Wick",
    "email": "johnwick@gmail.com",
    "password": "BabaYaga"
}
```
#

## Login de usuário:
POST http://{BASE_URL}/api/signin

```json
{
    "email": "johnwick@gmail.com",
    "password": "BabaYaga"
}
```
#

## Ver dados do usuário:
GET http://{BASE_URL}/api

```json
Não possui corpo na requisição.
```
#

## Atualizar os dados do usuário:
PUT http://{BASE_URL}/api

```json
{
    "name": "John",
    "last_name": "Wick II",
    "email": "johnwick@gmail.com",
    "password": "Matrix"
}
```
#

## Deletar um usuário:
DELETE http://{BASE_URL}/api

```json
Não possui corpo na requisição.
```
#