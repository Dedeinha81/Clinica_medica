
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, schemas, database

# Cria o roteador da API para consultas
router = APIRouter(
    prefix="/consultas",
    tags=["Consultas"]
)

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Rota para criar uma nova consulta
@router.post("/", response_model=schemas.Consulta)
def criar_consulta(consulta: schemas.ConsultaCreate, db: Session = Depends(get_db)):
    # Aqui você pode adicionar validações extras, por exemplo:
    # checar se o paciente e médico existem antes de criar a consulta
    return crud.criar_consulta(db, consulta)

# Rota para listar todas as consultas
@router.get("/", response_model=list[schemas.Consulta])
def listar_consultas(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.listar_consultas(db, skip=skip, limit=limit)

# Rota para buscar uma consulta pelo ID
@router.get("/{consulta_id}", response_model=schemas.Consulta)
def buscar_consulta(consulta_id: int, db: Session = Depends(get_db)):
    consulta = db.query(crud.models.Consulta).filter(crud.models.Consulta.id == consulta_id).first()
    if not consulta:
        raise HTTPException(status_code=404, detail="Consulta não encontrada")
    return consulta
