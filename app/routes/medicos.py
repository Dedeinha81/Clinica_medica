
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, schemas, database

# Cria o roteador da API para médicos
router = APIRouter(
    prefix="/medicos",
    tags=["Médicos"]
)

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Rota para criar um novo médico
@router.post("/", response_model=schemas.Medico)
def criar_medico(medico: schemas.MedicoCreate, db: Session = Depends(get_db)):
    return crud.criar_medico(db, medico)

# Rota para listar todos os médicos
@router.get("/", response_model=list[schemas.Medico])
def listar_medicos(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.listar_medicos(db, skip=skip, limit=limit)

# Rota para buscar um médico pelo ID
@router.get("/{medico_id}", response_model=schemas.Medico)
def buscar_medico(medico_id: int, db: Session = Depends(get_db)):
    medico = db.query(crud.models.Medico).filter(crud.models.Medico.id == medico_id).first()
    if not medico:
        raise HTTPException(status_code=404, detail="Médico não encontrado")
    return medico
