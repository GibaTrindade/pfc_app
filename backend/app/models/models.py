import datetime
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Boolean
from sqlalchemy.orm import relationship
#from sqlalchemy.ext.associationproxy import association_proxy
from ..services import Base
from sqlalchemy_utils import EmailType



# Declare Classes / Tables
class CursoParticipante(Base):
    __tablename__ = 'curso_participante'
    curso_id = Column(ForeignKey('cursos.id'), primary_key=True)
    participante_id = Column(ForeignKey('participantes.id'), primary_key=True)
    status = Column(String, nullable=False)
    condicao_acao = Column(String, nullable=False)
    ch_valida = Column(Integer, nullable=False)
    inscricao = Column(Boolean, nullable=True)
    curso = relationship("Curso", back_populates="participantes")
    participante = relationship("Participante", back_populates="cursos")

    # proxies
    #participante_name = association_proxy(target_collection='author', attr='name')
    #book_title = association_proxy(target_collection='book', attr='title')

class Curso(Base):
    __tablename__ = 'cursos'
    id = Column(Integer, primary_key=True)
    nome = Column(String, index=True, nullable=False)
    competencia = Column(String, nullable=False)
    categoria_acao = Column(String, nullable=False)
    data_inicio = Column(DateTime, default=datetime.datetime.utcnow)
    data_fim = Column(DateTime, default=datetime.datetime.utcnow)
    inst_certificadora = Column(String, nullable=False)
    inst_promotora = Column(String, nullable=False)
    vagas = Column(Integer, nullable=False)
    ch_curso = Column(Integer, nullable=False)
    modalidade = Column(String, nullable=False)
    tipo_reconhecimento = Column(String, nullable=False)
    participantes = relationship("CursoParticipante", back_populates="curso")

class Participante(Base):
    __tablename__ = 'participantes'
    id = Column(Integer, primary_key=True)
    cpf = Column(String, index=True, unique=True, nullable=False)
    nome = Column(String, index=True, nullable=False)
    email = Column(EmailType)
    cargo = Column(String, nullable=False)
    lotacao = Column(String, nullable=False)
    origem = Column(String, nullable=False)
    is_ativo = Column(Boolean, nullable=False)
    role = Column(String, nullable=False)
    cursos = relationship("CursoParticipante", back_populates="participante")
