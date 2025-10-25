
from sqlalchemy import Column, Integer, String, Date, Time, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class Paciente(Base):
    __tablename__ = "pacientes"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    email = Column(String, unique=True, index=True)
    telefone = Column(String)
    consultas = relationship("Consulta", back_populates="paciente")

class Medico(Base):
    __tablename__ = "medicos"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    especialidade = Column(String)
    consultas = relationship("Consulta", back_populates="medico")

class Consulta(Base):
    __tablename__ = "consultas"
    id = Column(Integer, primary_key=True, index=True)
    paciente_id = Column(Integer, ForeignKey("pacientes.id"))
    medico_id = Column(Integer, ForeignKey("medicos.id"))
    data = Column(Date)
    horario = Column(Time)
    observacoes = Column(String)
    paciente = relationship("Paciente", back_populates="consultas")
    medico = relationship("Medico", back_populates="consultas")
