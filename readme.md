# Manual da API

API capaz de realizar um CRUD completo de um usuário usando Flask-SQLAlchemy, Blueprint, Migrations e Design Patterns – Factory.

A aplicação é dividida em duas versões marcadas com Tags v1 e v2 onde a v1 tem rotas protegidas com credenciais de acesso usando API keys, enquanto na v2 foi implementado Jwt.


1. Clone o repositório e em um ambiente virtual instale todas as dependências que 
estão no arquivo "requirements.txt". Caso esteja usando pip use:
<!-->
    $ pip install -r requeriments.txt
<!-->

2. Rode o Migrate.
<!-->
    $ flask db init
    $ flask db migrate
    $ flask db upgrade
<!-->

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
#### *Rota protegida.
GET http://{BASE_URL}/api

```json
Não possui corpo na requisição.
```
#

## Atualizar os dados do usuário:
#### *Rota protegida.
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
#### *Rota protegida.
DELETE http://{BASE_URL}/api

```json
Não possui corpo na requisição.
```
#