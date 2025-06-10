# SabaraAPI - Sprint Python
Este projeto é uma API feita exclusivamente para o hospital Sabará, com o objetivo de automatizar diversos processos, entre eles:
- Prontuarios
- Recepção
- Salas médicas
E muito mais!

## Video Sprint
[Youtube](https://www.youtube.com/watch?v=_TzUiP4WutM)

## Equipe:

- Pedro Henrique, 559443 - Desenvolvedor BackEnd
- Evandro Kaibara, 559274 - Reponsavel pelo FrontEnd
- Ícaro de Oliveira, 559950 - Ideias e ajuda
- Mateus Mallet, 560491 - Ideias e ajuda

## Como rodar o projeto?
Para rodar o projeto você precisa seguir alguns passos!
1. Instalar o [Python](https://www.python.org/downloads/).
2. Instalar o [PostgreSQL](https://www.postgresql.org/download/).
>Desativado nesta primeira versão
3. Clonar o projeto com:
```
https://github.com/phbrg/sabaraAPI.git
```
4. Criar um arquivo `.env` com a seguinte variavel:
```
DATABASE_URL=postgresql://USER:PASSWORD@localhost:5432/DB
```
>Substitua as variaveis USER, PASSWORD e DB pelas suas variaveis
5. Instalar o venv em sua maquina com:
```
pip install venv
```
6. Rodar o venv com:
```
python -m venv venv
```
7. Iniciar o ambiente venv com:
```
venv\Scripts\activate
```
8. Instalar os requirementes no ambiente venv com:
```
pip install -r requirements.txt
```
9. Rodar o projeto com:
```
uvicorn app.main:app --reload
```
10. Ter um arduino conectado em sua maquina com o codigo disponivel [Aqui](https://github.com/phbrg/sabaraAPI/tree/edge) rodando.

## Como funciona o projeto?
Atualmente o nosso projeto tem apenas um endpoint dinamico, que recebe os dados direto dos sensores disponiveis no arduino e os envia para o usuario.

## End points:

### Mostrar todos dados do arduino:
GET `/data`
Response:
```json
  [
      "{\"temperatura\": 00.0, \"umidade\": 00.0, \"luz\": 000}",
      "{\"temperatura\": 00.0, \"umidade\": 00.0, \"luz\": 000}",
      ...
  ]
```

### Mostrar o ultimo registro do arduino:
GET `/data/?current=True`
Response:
```json
  "{\"temperatura\": 30.7, \"umidade\": 42.1, \"luz\": 446}"
```
