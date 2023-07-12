from ..models.models import Curso, CursoParticipante, Participante
from ..services import engine
from sqlalchemy.orm import Session

# Insert data

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

    #session.add_all([curso1, curso2, participante1, participante2, participante3])
    #session.commit()

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

    #session.add_all([curso_participante1, curso_participante2, curso_participante3, curso_participante4])
    #session.commit()