
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# URL de conexão com o PostgreSQL
SQLALCHEMY_DATABASE_URL = "postgresql+psycopg2://postgres:150525@localhost:5432/clinica_medica"

# Cria o engine de conexão
engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    echo=True  # Mostra no terminal os comandos SQL executados (opcional)
)

# Cria a sessão para interagir com o banco
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Classe base para os modelos
Base = declarative_base()

# Função para obter a sessão (use em dependências do FastAPI)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
