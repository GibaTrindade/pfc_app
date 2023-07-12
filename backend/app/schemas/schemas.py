from typing import List, Optional
from pydantic import BaseModel, Field
import datetime

class ParticipanteBase(BaseModel):
    id: int# = Field(alias='author_id')
    nome: str# = Field(alias='author_name')
    email: str
    cargo: Optional[str]
    lotacao: Optional[str]
    origem: Optional[str]
    is_ativo: Optional[bool]
    role: Optional[str]


    class Config:
        orm_mode = True
        allow_population_by_field_name = True

#Classe criada apenas para fins de response_model
class ParticipanteCurso(BaseModel):
    id: int
    nome: str
    email:str
    cpf: str
    is_ativo: bool
    role: str
    status: str
    condicao_acao: str
    ch_valida: int
    inscricao: bool


class CursoBase(BaseModel):
    id: int# = Field(alias='book_id')
    nome: str# = Field(alias='book_title')
    competencia: Optional[str]
    categoria_acao: Optional[str]
    data_inicio: Optional[datetime.datetime]
    data_fim: Optional[datetime.datetime]
    inst_certificadora: Optional[str]
    inst_promotora: Optional[str]
    vagas: Optional[int]
    ch_curso: Optional[int]
    modalidade: Optional[str]
    tipo_reconhecimento: Optional[str]

    class Config:
        orm_mode = True
        allow_population_by_field_name = True


class CursoSchema(CursoBase):
    participantes: List[ParticipanteCurso]

class ParticipanteSchema(ParticipanteBase):
    cursos: List[CursoBase]