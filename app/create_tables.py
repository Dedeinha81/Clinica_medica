
from app.database import engine, Base
import app.models  # importa os modelos para que o SQLAlchemy saiba quais tabelas criar

print("⏳ Criando tabelas no banco...")
Base.metadata.create_all(bind=engine)
print("✅ Tabelas criadas com sucesso!")
