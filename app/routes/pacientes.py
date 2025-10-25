
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, schemas, database

# Cria o roteador da API para pacientes
router = APIRouter(
    prefix="/pacientes",
    tags=["Pacientes"]
)

# Função para obter a sessão do banco
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Rota para criar um novo paciente
@router.post("/", response_model=schemas.Paciente)
def criar_paciente(paciente: schemas.PacienteCreate, db: Session = Depends(get_db)):
    return crud.criar_paciente(db, paciente)

# Rota para listar todos os pacientes
@router.get("/", response_model=list[schemas.Paciente])
def listar_pacientes(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.listar_pacientes(db, skip=skip, limit=limit)

# Rota para buscar um paciente pelo ID
@router.get("/{paciente_id}", response_model=schemas.Paciente)
def buscar_paciente(paciente_id: int, db: Session = Depends(get_db)):
    paciente = db.query(crud.models.Paciente).filter(crud.models.Paciente.id == paciente_id).first()
    if not paciente:
        raise HTTPException(status_code=404, detail="Paciente não encontrado")
    return paciente
