
# Ponto de entrada da aplicação FastAPI

from fastapi import FastAPI
from app.database import Base, engine
from app.routes import pacientes, medicos, consultas

# Cria todas as tabelas do banco (se ainda não existirem)
Base.metadata.create_all(bind=engine)

# Inicializa a aplicação FastAPI
app = FastAPI(
    title="Clínica Médica API",
    description="API para gerenciar pacientes, médicos e consultas de uma clínica",
    version="1.0.0"
)

# Inclui os routers da aplicação
app.include_router(pacientes.router)  # Rotas de pacientes
app.include_router(medicos.router)    # Rotas de médicos
app.include_router(consultas.router)  # Rotas de consultas

# Rota inicial para teste
@app.get("/")
def root():
    return {"message": "API da Clínica Médica está funcionando!"}
