# API de Times e Jogadores

Trabalho da CP4 de Python. API feita com FastAPI e SQLite, com uma página em
HTML, CSS e JavaScript para usar a API.

Um time tem vários jogadores. O jogador guarda o `time_id`, que é a chave
estrangeira apontando para o time.

## Como rodar

Instalar as dependências:

```bash
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

Subir a API, de dentro da pasta `backend`:

```bash
cd backend
```

```bash
..\.venv\Scripts\python.exe -m uvicorn main:app --reload
```

A API fica em `http://localhost:8000` e a documentação em
`http://localhost:8000/docs`.

Com a API rodando, abra o arquivo `frontend/index.html` no navegador.

## Rotas

```
GET    /times           GET    /jogadores
GET    /times/{id}      GET    /jogadores/{id}
POST   /times           POST   /jogadores
PUT    /times/{id}      PUT    /jogadores/{id}
DELETE /times/{id}      DELETE /jogadores/{id}
```

## Organização

O backend é dividido em duas camadas: o `controller.py` cuida das rotas e o
`service.py` cuida do SQL.

```
backend/
  main.py         aplicação FastAPI
  database.py     conexão e criação das tabelas
  times/          models.py, service.py, controller.py
  jogadores/      models.py, service.py, controller.py
frontend/
  index.html
  css/style.css
  js/script.js
```
