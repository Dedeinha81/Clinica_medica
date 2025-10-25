
from pydantic import BaseModel
from datetime import date, time

class PacienteBase(BaseModel):
    nome: str
    email: str
    telefone: str | None = None

class PacienteCreate(PacienteBase):
    pass

class Paciente(PacienteBase):
    id: int
    class Config:
        orm_mode = True

# Mesma lógica para Medico
class MedicoBase(BaseModel):
    nome: str
    especialidade: str

class MedicoCreate(MedicoBase):
    pass

class Medico(MedicoBase):
    id: int
    class Config:
        orm_mode = True

# Mesma lógica para Consulta
class ConsultaBase(BaseModel):
    paciente_id: int
    medico_id: int
    data: date
    horario: time
    observacoes: str | None = None

class ConsultaCreate(ConsultaBase):
    pass

class Consulta(ConsultaBase):
    id: int
    class Config:
        orm_mode = True
