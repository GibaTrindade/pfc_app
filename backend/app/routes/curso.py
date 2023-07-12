from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import orm
from sqlalchemy.orm import joinedload
from sqlalchemy import desc
from typing import List
from ..services import get_db
from ..models.models import Curso
from ..schemas.schemas import CursoSchema


curso = APIRouter()

@curso.get("/cursos/{id}", response_model=CursoSchema,
         response_model_exclude={'blurb'}, response_model_by_alias=False)
async def get_book(id: int, db: orm.Session = Depends(get_db)):
    db_curso = db.query(Curso).options(joinedload(Curso.participantes)).\
        where(Curso.id == id).one()
    #return db_curso
    list_participantes = []
    for participante in db_curso.participantes:
        participante_data = {
            "id": participante.participante.id,
            "nome": participante.participante.nome,
            "email": participante.participante.email,
            "cpf": participante.participante.cpf,
            "is_ativo": participante.participante.is_ativo,
            "role": participante.participante.role,
            "status": participante.status,
            "condicao_acao": participante.condicao_acao,
            "ch_valida": participante.ch_valida,
            "inscricao": participante.inscricao

        }
        list_participantes.append(participante_data)
    curso_data = {
        "id": db_curso.id,
        "nome": db_curso.nome,
        "competencia": db_curso.competencia,
        "categoria_acao": db_curso.categoria_acao,
        "data_inicio": db_curso.data_inicio,
        "data_fim": db_curso.data_fim,
        "inst_certificadora": db_curso.inst_certificadora,
        "inst_promotora": db_curso.inst_promotora,
        "vagas": db_curso.vagas,
        "ch_curso": db_curso.ch_curso,
        "modalidade": db_curso.modalidade,
        "tipo_reconhecimento": db_curso.tipo_reconhecimento,
        "participantes": list_participantes
    }
    return curso_data


@curso.get("/cursos", response_model=List[CursoSchema],
         response_model_exclude={'blurb'}, response_model_by_alias=False)
async def get_books(db: orm.Session = Depends(get_db)):
    db_cursos = db.query(Curso).order_by(desc(Curso.data_fim)).options(joinedload(Curso.participantes)).all()
    #return db_cursos
    lista_cursos=[]
    
    for curso in db_cursos:
        participantes = curso.participantes
        lista_participantes=[]
        for participante in participantes:
            data_participante = {
                "id": participante.participante.id,
                "nome": participante.participante.nome,
                "email": participante.participante.email,
                "cpf": participante.participante.cpf,
                "is_ativo": participante.participante.is_ativo,
                "role": participante.participante.role,
                "status": participante.status,
                "condicao_acao": participante.condicao_acao,
                "ch_valida": participante.ch_valida,
                "inscricao": participante.inscricao
            }
            lista_participantes.append(data_participante)
        data_curso = {
            "id": curso.id,
            "nome": curso.nome,
            "competencia": curso.competencia,
            "categoria_acao": curso.categoria_acao,
            "data_inicio": curso.data_inicio,
            "data_fim": curso.data_fim,
            "inst_certificadora": curso.inst_certificadora,
            "inst_promotora": curso.inst_promotora,
            "vagas": curso.vagas,
            "ch_curso": curso.ch_curso,
            "modalidade": curso.modalidade,
            "tipo_reconhecimento": curso.tipo_reconhecimento,
            "participantes": lista_participantes
        }
        lista_cursos.append(data_curso)
    return lista_cursos

@curso.get("/concluintes/{id_curso}")#, response_model=ParticipanteSchema,
         #response_model_exclude={'blurb'}, response_model_by_alias=False)
async def get_author(id_curso: int, db: orm.Session = Depends(get_db)):
    db_curso= db.query(Curso).options(joinedload(Curso.participantes)).\
        where(Curso.id == id_curso).one()
    count = 0
    for participante in db_curso.participantes:
        if (participante.status == "FINALIZADO" and participante.condicao_acao=="DISCENTE"):
            count = count+1

    concluintes = len(db_curso.participantes)
    return count
