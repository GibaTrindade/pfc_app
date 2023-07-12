from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import orm
from sqlalchemy.orm import joinedload
from typing import List
from ..services import get_db
from ..models.models import Participante
from ..schemas.schemas import ParticipanteSchema

participante = APIRouter()

@participante.get("/participantes/{id}", response_model=ParticipanteSchema,
         response_model_exclude={'blurb'}, response_model_by_alias=False)
async def get_author(id: int, db: orm.Session = Depends(get_db)):
    db_participante = db.query(Participante).options(joinedload(Participante.cursos)).\
        where(Participante.id == id).one()
    return db_participante


@participante.get("/participantes")#, response_model=List[ParticipanteSchema],
         #response_model_exclude={'blurb'}, response_model_by_alias=False)
async def get_authors(db: orm.Session = Depends(get_db)):
    db_participantes = db.query(Participante).options(joinedload(Participante.cursos)).all()
    return db_participantes
    
    lista_autores=[]
    
    for autor in db_authors:
        books = autor.books
        lista_books=[]
        for book in books:
            data_book = {
                'id': book.book.id,
                'title': book.book.title,
                'blurb': book.blurb
            }
            lista_books.append(data_book)
        data_autor = {
            'id': autor.id,
            'name': autor.name,
            'blurb': None,
            'books': lista_books
        }
        lista_autores.append(data_autor)
    return lista_autores