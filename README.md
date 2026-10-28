# Agenda de Contatos

Projeto da disciplina **Projeto de Software** (Impacta). Entrega atual: **2ª AC**.

Aplicação web com **front-end** (templates Django), **back-end** (Django/Python) e **banco de dados** (SQLite) para cadastrar, listar, buscar, editar e excluir contatos.

## Funcionalidades

### 1ª AC — Cadastro e listagem

- Cadastrar contato (nome, telefone, e-mail)
- Listar contatos salvos no banco SQLite

### 2ª AC — Editar, excluir e busca

- Buscar por nome, telefone ou e-mail
- Editar um contato já cadastrado
- Excluir um contato, com tela de confirmação

## Requisitos

- Python 3.12+ (testado com 3.13)
- pip

## Como rodar

```bash
# 1. Criar e ativar o ambiente virtual (Windows PowerShell)
python -m venv .venv
.\.venv\Scripts\Activate.ps1

# 2. Instalar dependências
pip install -r requirements.txt

# 3. Aplicar migrations
python manage.py migrate

# 4. Subir o servidor
python manage.py runserver
```

Abra no navegador: http://127.0.0.1:8000/

- Lista e busca: http://127.0.0.1:8000/
- Novo contato: http://127.0.0.1:8000/novo/
- Editar: http://127.0.0.1:8000/<id>/editar/
- Excluir: http://127.0.0.1:8000/<id>/excluir/

## Estrutura

```
projeto_impacta/
  config/          # settings e URLs do projeto
  contatos/        # app (model, forms, views)
  templates/       # HTML
  static/css/      # estilos
  manage.py
  requirements.txt
```

## Board do projeto

Veja as instruções em [BOARD.md](BOARD.md) para montar o GitHub Projects (ou Trello) com as funcionalidades das entregas.

## Entrega Classroom

Modelo de texto e roteiro de vídeo em [ENTREGA_AC1.md](ENTREGA_AC1.md).

## Próximas ACs (planejado)

- 3ª AC: login / autenticação
- Final: categorias / favoritos + polish
