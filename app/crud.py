
from sqlalchemy.orm import Session
from . import models, schemas

# PACIENTES
def criar_paciente(db: Session, paciente: schemas.PacienteCreate):
    db_paciente = models.Paciente(**paciente.dict())
    db.add(db_paciente)
    db.commit()
    db.refresh(db_paciente)
    return db_paciente

def listar_pacientes(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Paciente).offset(skip).limit(limit).all()

# MÉDICOS
def criar_medico(db: Session, medico: schemas.MedicoCreate):
    db_medico = models.Medico(**medico.dict())
    db.add(db_medico)
    db.commit()
    db.refresh(db_medico)
    return db_medico

def listar_medicos(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Medico).offset(skip).limit(limit).all()

# CONSULTAS
def criar_consulta(db: Session, consulta: schemas.ConsultaCreate):
    db_consulta = models.Consulta(**consulta.dict())
    db.add(db_consulta)
    db.commit()
    db.refresh(db_consulta)
    return db_consulta

def listar_consultas(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Consulta).offset(skip).limit(limit).all()
