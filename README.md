# 🏥 Clínica Médica API

API RESTful desenvolvida em **Python com FastAPI** para o gerenciamento de **pacientes, médicos e consultas** em uma clínica médica.

O objetivo do projeto é simular um **cenário real de backend**, aplicando boas práticas de arquitetura, regras de negócio, testes automatizados e deploy contínuo em nuvem.

A aplicação está hospedada no **Render**, com **CI/CD**, garantindo atualização automática a cada push no GitHub.

---

## 🎯 Problema que o projeto resolve
Clínicas médicas precisam de um sistema confiável para:
- Organizar pacientes e médicos
- Controlar agendamentos
- Garantir integridade dos dados
- Facilitar a manutenção e evolução do sistema

Esta API centraliza essas operações de forma segura, escalável e bem estruturada.

---

## ✨ Funcionalidades
- Cadastro, listagem, atualização e exclusão de **Pacientes**
- Cadastro, listagem, atualização e exclusão de **Médicos**
- **Agendamento e gerenciamento de Consultas**
- Persistência de dados com **PostgreSQL**
- Documentação automática com **Swagger UI**
- **Testes unitários automatizados** com Pytest
- **Deploy automático** via CI/CD

---

## 🧠 Regras de Negócio
- Cada consulta está associada a **um paciente e um médico**
- Não é possível criar consultas sem vínculos válidos
- Os dados seguem validação rigorosa com **Pydantic**
- As operações seguem o padrão CRUD com separação de responsabilidades

---

## 🛠️ Tecnologias Utilizadas
- Python 3.13
- FastAPI
- SQLAlchemy
- Pydantic
- Uvicorn
- PostgreSQL
- Pytest
- Render (Deploy em Nuvem com CI/CD)

---

## 🏗️ Arquitetura do Projeto
O projeto foi estruturado seguindo boas práticas de organização e manutenção:

Clinica_medica/

│── app/

│ │── main.py - Ponto de entrada da aplicação

│ │── models.py - Modelos do banco de dados (SQLAlchemy)

│ │── schemas.py - Validação e serialização de dados (Pydantic)

│ │── database.py - Configuração do banco de dados

│ │── crud.py - Regras de acesso aos dados

│ └── routes/

│ │── pacientes.py

│ │── medicos.py

│ └── consultas.py

│── tests/

│ │── test_pacientes.py

│ │── test_medicos.py

│ │── test_consultas.py

│── requirements.txt

│── Procfile



---

## 🚀 Acesso à Aplicação
A API está online e pode ser testada diretamente pelo Swagger:

👉 https://clinica-medica-xuvt.onrender.com/docs

---

## ⚙️ Como Executar Localmente


# Clone o repositório

git clone https://github.com/Dedeinha81/Clinica_medica.git

# Acesse a pasta

cd Clinica_medica

# Crie e ative um ambiente virtual

python -m venv venv

source venv/bin/activate  - Windows: venv\Scripts\activate


# Instale as dependências

pip install -r requirements.txt


# Execute a aplicação

uvicorn app.main:app --reload

---

🧪 Testes Unitários

Os testes garantem que as rotas e regras principais da API funcionem corretamente.

Para executar:

python -m pytest -v

---
👩‍💻 Autora

Andrea Cruz
Desenvolvedora Back-End em formação, com foco em Python, APIs REST, testes automatizados e boas práticas de desenvolvimento.



⭐ Se este projeto te ajudou ou te inspirou, deixe uma estrela no repositório!


