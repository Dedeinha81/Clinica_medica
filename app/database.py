
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# URL do banco no Render
SQLALCHEMY_DATABASE_URL = "postgresql://clinica_medica_edyk_user:R931zzEtWFr9VEBimGYS5VKiEGXWfzk5@dpg-d3ul5eodl3ps73f806d0-a.oregon-postgres.render.com/clinica_medica_edyk"

# Cria o engine de conexão
engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True)

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