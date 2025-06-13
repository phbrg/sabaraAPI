# SabaraAPI - Sprint Python
Este projeto é uma API feita exclusivamente para o hospital Sabará, com o objetivo de automatizar diversos processos, entre eles:
- Prontuarios
- Recepção
- Salas médicas
E muito mais!

## Video Sprint
> Em desenvolvimento...

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
SECRET_KEY = "SUASECRETKEY"
ALGORITHM = "HS256"
```
>Substitua as variaveis USER, PASSWORD, DB e SUASECRETKEY pelas suas variaveis
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

## Futuro
No futuro pretendemos expandir mais a API, trazendo mais segurança e clareza nos dados e em seu uso, melhorando algumas praticas e adicionando novos conteudos e utilidades.

## Como funciona o projeto?
O projeto atualmente conta com diversas rotas dinamicas (listadas abaixo) que buscam melhorar a eficiencia do hospital, dentre elas rotas de registros de medicos e equipe do hospital, registro de pacientes, consultas e prontuarios, assim como o armazenamento, e edição destes dados.

## End points:

### Users:

#### Create User
Route: `/user/create/`
Method: `POST`
Body:
```json
  {
      "name": "username",
      "email": "email@sabara.com",
      "password": "password",
      "role": "medico" // admin, medico, recepcao
  }
```
Response:
```json
  {
    "id": 1,
    "name": "username",
    "email": "email@sabara.com",
    "role": "admin",
    "createdAt": "2000-00-00T00:00:00.0000"
  }
```
> OBS: Todos dados são ficticios

#### Login
Route: `/user/login/`
Method: `POST`
Body:
```json
  {
      "email": "email@sabara.com",
      "password": "password"
  }
```
Response:
```json
  {
    "token": "JWTTOKEN",
  }
```
> OBS: Todos dados são ficticios

#### Me
Route: `/user/me/`
Method: `GET`
Response:
```json
  {
    "id": "1",
    "role": "RoleEnum.ADMIN"
  }
```
> OBS: Todos dados são ficticios

#### Update user
Route: `/user/update/{{ID}}`
Method: `PUT`
Body:
```json
  {
      "email": "admin@admin.com",
      ...
  }
```
Response:
```json
  {
    "id": 1,
    "name": "admin",
    "email": "admin@admin.com",
    "role": "admin",
    "createdAt": "2000-00-00T00:00:00.0000"
  }
```
> OBS: Todos dados são ficticios

#### Delete User
Route: `/user/delete/{{ID}}`
Method: `DELETE`
Response:
```json
  { 
    "message": "User deleted."
  }
```

#### Get User(s)
Route: `/user/{{?param=value}}`
Method: `GET`
Params:
- `id`
- `name`
- `email`
Response:
```json
  [
    {
        "id": 1,
        "name": "admin",
        "email": "admin@admin.com",
        "role": "admin",
        "createdAt": "2000-00-00T00:00:00.0000"
    },
    ...
  ]
```
> OBS: Todos dados são ficticios

### Patient:

#### Create Patient
Route: `/patient/create/`
Method: `POST`
Body:
```json
{
    "full_name": "Name Surname",
    "birth_date": "01-01-2001",
    "cpf": "999.999.999-99",
    "phone": "(11) 99999-9999",
    "email": "paciente@email.com",
    "allergies": ["Allergie 1",...], // can be null
    "notes": ["Note 1",...] // can be null
}
```
Response:
```json
  {
    "id": 1,
    "full_name": "Name Surname",
    "birth_date": "01-01-2001",
    "cpf": "999.999.999-99",
    "phone": "(11) 99999-9999",
    "email": "paciente@email.com",
    "allergies": ["Allergie 1",...],
    "notes": ["Note 1",...],
    "createdAt": "2000-00-00T00:00:00.0000"
  }
```
> OBS: Todos dados são ficticios

#### Update Patient
Route: `/patient/update/{{ID}}`
Method: `PUT`
Body:
```json
  {
      "email": "paciente@email.com",
      ...
  }
```
Response:
```json
  {
    "id": 1,
    "full_name": "Name Surname",
    "birth_date": "01-01-2001",
    "cpf": "999.999.999-99",
    "phone": "(11) 99999-9999",
    "email": "paciente@email.com",
    "allergies": ["Allergie 1",...],
    "notes": ["Note 1",...],
    "createdAt": "2000-00-00T00:00:00.0000"
  }
```
> OBS: Todos dados são ficticios

#### Delete Patient
Route: `/patient/delete/{{ID}}`
Method: `DELETE`
Response:
```json
  { 
    "message": "Patient deleted."
  }
```

#### Get Patient(s)
Route: `/patient/{{?param=value}}`
Method: `GET`
Params:
- `id`
- `full_name`
- `email`
- `phone`
- `cpf`
Response:
```json
  [
    {
        "id": 1,
        "full_name": "Name Surname",
        "birth_date": "01-01-2001",
        "cpf": "999.999.999-99",
        "phone": "(11) 99999-9999",
        "email": "paciente@email.com",
        "allergies": ["Allergie 1",...],
        "notes": ["Note 1",...],
        "createdAt": "2000-00-00T00:00:00.0000"
    },
    ...
  ]
```
> OBS: Todos dados são ficticios

### Appointment:

#### Create Appointment
Route: `/appointment/create/`
Method: `POST`
Body:
```json
  {
    "patient_id": 1,
    "patient_name": "Name Surname",
    "medic_id": 1,
    "medic_name": "Name Surname",
    "date": "01-01-2001",
    "appointmentType": "SUS" // sus, convenio, particular
  }
```
Response:
```json
  {
    "id": 1,
    "patient_id": 1,
    "patient_name": "Name Surname",
    "medic_id": 1,
    "medic_name": "Name Surname",
    "date": "01-01-2001",
    "appointmentType": "SUS",
    "createdAt": "2000-00-00T00:00:00.0000"
  }
```
> OBS: Todos dados são ficticios

#### Update Appointment
Route: `/appointment/update/{{ID}}`
Method: `PUT`
Body:
```json
  {
      "patient_name": "Name Surname",
      ...
  }
```
Response:
```json
  {
    "id": 1,
    "patient_id": 1,
    "patient_name": "Name Surname",
    "medic_id": 1,
    "medic_name": "Name Surname",
    "date": "01-01-2001",
    "appointmentType": "SUS",
    "createdAt": "2000-00-00T00:00:00.0000"
  }
```
> OBS: Todos dados são ficticios

#### Delete Appointment
Route: `/appointment/delete/{{ID}}`
Method: `DELETE`
Response:
```json
  { 
    "message": "Appointment deleted."
  }
```

#### Get Appointment(s)
Route: `/appointment/{{?param=value}}`
Method: `GET`
Params:
- `id`
- `patient_id`
- `medic_id`
- `medic_name`
- `patient_name`
Response:
```json
  [
    {
      "id": 1,
      "patient_id": 1,
      "patient_name": "Name Surname",
      "medic_id": 1,
      "medic_name": "Name Surname",
      "date": "01-01-2001",
      "appointmentType": "SUS",
      "createdAt": "2000-00-00T00:00:00.0000"
    },
    ...
  ]
```
> OBS: Todos dados são ficticios

### Prontuario:

#### Create Prontuario
Route: `/prontuario/create/`
Method: `POST`
Body:
```json
  {
    "patient_id": 1,
    "patient_name": "Name Surname",
    "medic_id": 1,
    "medic_name": "Name Surname",
    "description": "Description"
  }
```
Response:
```json
  {
    "id": 1,
    "patient_id": "1",
    "patient_name": "Name Surname",
    "medic_id": "1",
    "medic_name": "Name Surname",
    "description": "Description",
    "createdAt": "2000-00-00T00:00:00.0000"
  }
```
> OBS: Todos dados são ficticios

#### Update Prontuario
Route: `/prontuario/update/{{ID}}`
Method: `PUT`
Body:
```json
  {
      "patient_name": "Name Surname",
      ...
  }
```
Response:
```json
  {
    "id": 1,
    "patient_id": "1",
    "patient_name": "Name Surname",
    "medic_id": "1",
    "medic_name": "Name Surname",
    "description": "Description",
    "createdAt": "2000-00-00T00:00:00.0000"
  }
```
> OBS: Todos dados são ficticios

#### Delete Prontuario
Route: `/prontuario/delete/{{ID}}`
Method: `DELETE`
Response:
```json
  { 
    "message": "Prontuario deleted."
  }
```

#### Get Prontuario(s)
Route: `/prontuario/{{?param=value}}`
Method: `GET`
Params:
- `id`
- `patient_id`
- `medic_id`
- `medic_name`
- `patient_name`
Response:
```json
  [
    {
      "id": 1,
      "patient_id": "1",
      "patient_name": "Name Surname",
      "medic_id": "1",
      "medic_name": "Name Surname",
      "description": "Description",
      "createdAt": "2000-00-00T00:00:00.0000"
    },
    ...
  ]
```
> OBS: Todos dados são ficticios