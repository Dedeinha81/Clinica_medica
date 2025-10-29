# 🏥 Clínica Médica API

API RESTful desenvolvida em **Python (FastAPI)** para o gerenciamento de pacientes, médicos e consultas de uma clínica médica.  
O projeto foi hospedado gratuitamente na nuvem com **Render**, utilizando **CI/CD** para deploy automático a cada atualização no GitHub.

---

## ✨ Funcionalidades

✅ Cadastro, listagem, atualização e exclusão de **Pacientes**  
✅ Cadastro, listagem, atualização e exclusão de **Médicos**  
✅ Agendamento e gerenciamento de **Consultas**  
✅ Integração com **Banco de Dados PostgreSQL**  
✅ Documentação automática com **Swagger UI**  
✅ Deploy automático com **Render (CI/CD)**  
✅ **Testes Unitários Automatizados** com **Pytest** 

---

## 🛠️ Tecnologias Utilizadas

🐍 **Python 3.13**  
⚡ **FastAPI**  
🧱 **SQLAlchemy**  
🧩 **Pydantic**  
🔥 **Uvicorn**  
🗄️ **PostgreSQL**  
☁️ **Render (Deploy na Nuvem com CI/CD)** 

🧪 **Pytest (Testes Unitários)**  



---

## 🚀 Como Acessar

A aplicação está online!  
Acesse diretamente o Swagger da API para testar os endpoints interativamente 👇  

👉 **[https://clinica-medica-xuvt.onrender.com/docs](https://clinica-medica-xuvt.onrender.com/docs)**

---

## 🔁 CI/CD - Deploy Automático

Toda vez que um **push** é feito no repositório do GitHub, o **Render** realiza automaticamente o **deploy** da nova versão.  
Assim, o projeto fica sempre **online e atualizado** 🌍✨  

---

## 🧩 Estrutura do Projeto

Clinica_medica/

│── app/

│ │── main.py - 🚀 Ponto de entrada da aplicação FastAPI

│ │── models.py - 🧱 Modelos do banco de dados (SQLAlchemy)

│ │── schemas.py - 🧩 Schemas Pydantic (validação e resposta)

│ │── database.py - 🗄️ Configuração do banco de dados PostgreSQL

│ │── crud.py - ⚙️ Funções CRUD (Create, Read, Update, Delete)

│ └── routes/

│ │── pacientes.py - 👩‍⚕️ Rotas de Pacientes

│ │── medicos.py - 🩺 Rotas de Médicos

│ └── consultas.py - 📅 Rotas de Consultas

│── tests/

│ │── test_consultas.py - 🧪 Testes unitários para Consultas

│ │── test_medicos.py - 🧪 Testes unitários para Médicos

│ │── test_pacientes.py - 🧪 Testes unitários para Pacientes

│── requirements.txt - 📦 Dependências do projeto

│── Procfile - ⚡ Arquivo de inicialização para deploy no Render

---

## 🧪 Testes Unitários

O projeto possui **testes unitários automatizados** com **[Pytest]** para garantir que todas as rotas e funcionalidades da API estejam funcionando corretamente.

### 📋 Como Rodar os Testes

Na raiz do projeto, execute:


python -m pytest -v


---

## 👩‍💻 Autora

**Andréa Cruz**  
Estudante de **Desenvolvimento Back-End**, apaixonada por tecnologia e em constante aprendizado sobre **APIs, Python e Bancos de Dados**.  

🌐 [LinkedIn](https://www.linkedin.com/in/andrea-cruz-leonardo/)  

---

⭐ Se este projeto te inspirou, deixe uma **estrela** no repositório! 🌟


