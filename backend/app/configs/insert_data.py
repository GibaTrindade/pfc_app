from sqlalchemy.orm import Session
from sqlalchemy import create_engine, MetaData, orm
from sqlalchemy.ext import declarative
import datetime
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Boolean
from sqlalchemy.orm import relationship
#from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy_utils import EmailType

# Insert data
SQLALCHEMY_DATABASE_URL = f"postgresql://postgres:post1234@localhost/pfc"

#engine = create_engine(f"mysql+pymysql://{user}:{password}@{host}:{port}/{database}")
engine = create_engine(SQLALCHEMY_DATABASE_URL)
meta = MetaData()
conn = engine.connect()
SessionLocal = orm.sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative.declarative_base()


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
    cursos_externos = relationship("CursoExterno", back_populates="participante")

class CursoExterno(Base):
    __tablename__ = 'curso_externo'
    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)
    ch_curso = Column(Integer, nullable=False)
    ch_valida = Column(Integer, nullable=True, default=0)
    inst_promotora = Column(String, nullable=False)
    data_inicio = Column(DateTime, default=datetime.datetime.utcnow)
    data_fim = Column(DateTime, default=datetime.datetime.utcnow)
    modalidade = Column(String, nullable=False)

    participante_id = Column(Integer, ForeignKey('participantes.id'))

    participante = relationship("Participante", back_populates="cursos_externos")



with Session(bind=engine) as session:
    curso1 = Curso(nome = "Estruturação de dados",
                    competencia = "nao sei",
                    categoria_acao = "Teste",
                    data_inicio = None,
                    data_fim = None,
                    inst_certificadora = "SEPLAG" ,
                    inst_promotora = "SEPLAG" ,
                    vagas = 20,
                    ch_curso = 20,
                    modalidade = "PRESENCIAL",
                    tipo_reconhecimento = "CARGA HORARIA"
                    )
    
    curso2 = Curso(  nome = "Pão e Circo",
                    competencia = "nao sei",
                    categoria_acao = "Dados",
                    data_inicio = None,
                    data_fim = None,
                    inst_certificadora = "SEPLAG" ,
                    inst_promotora = "SEPLAG" ,
                    vagas = 20,
                    ch_curso = 20,
                    modalidade = "PRESENCIAL",
                    tipo_reconhecimento = "CARGA HORARIA")

    participante1 = Participante(cpf = "04284624482",
                                nome = "Gilberto Trindade",
                                email = "g.trindade@gmail.com",
                                cargo = "GGOV",
                                lotacao = "IG",
                                origem = "SEPLAG",
                                is_ativo = True,
                                role = "admin")
    participante2 = Participante(cpf = "00991496485",
                                nome = "Mirella Cavalcanti",
                                email = "mirellaclm@gmail.com",
                                cargo = "GGOV",
                                lotacao = "IG",
                                origem = "SEPLAG",
                                is_ativo = True,
                                role = "admin")
    participante3 = Participante(cpf = "5548844521",
                                nome = "Beatriz Lins",
                                email = "beatriz.lins@gmail.com",
                                cargo = "GGOV",
                                lotacao = "IG",
                                origem = "SEPLAG",
                                is_ativo = True,
                                role = "admin")

    session.add_all([curso1, curso2, participante1, participante2, participante3])
    session.commit()

    curso_participante1 = CursoParticipante(curso_id=curso1.id, participante_id=participante1.id, 
                                            status="FINALIZADO",
                                            condicao_acao="DOCENTE",
                                            ch_valida=20,
                                            inscricao=True)
    curso_participante2 = CursoParticipante(curso_id=curso1.id, participante_id=participante2.id, 
                                            status="ABANDONADO",
                                            condicao_acao="DISCENTE",
                                            ch_valida=20,
                                            inscricao=True)
    curso_participante3 = CursoParticipante(curso_id=curso2.id, participante_id=participante3.id, 
                                            status="ABANDONADO",
                                            condicao_acao="DISCENTE",
                                            ch_valida=20,
                                            inscricao=True)
    curso_participante4 = CursoParticipante(curso_id=curso2.id, participante_id=participante1.id, 
                                            status="FINALIZADO",
                                            condicao_acao="DISCENTE",
                                            ch_valida=20,
                                            inscricao=True)

    session.add_all([curso_participante1, curso_participante2, curso_participante3, curso_participante4])
    session.commit()

    curso_externo = CursoExterno(
        nome = "FastAPI do Básico ao Avançado",
        ch_curso = 40,
        inst_promotora = "Udemy",
        modalidade = "EAD",

        participante_id = 1,
    )

    session.add(curso_externo)
    session.commit()
    