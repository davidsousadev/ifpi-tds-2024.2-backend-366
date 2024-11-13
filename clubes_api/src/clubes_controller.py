from fastapi import APIRouter, status, HTTPException
from src.database import get_engine
from src.models import Clube, RequestClube
from sqlmodel import Session, select


router = APIRouter()


@router.get('', status_code=status.HTTP_200_OK)
def lista_clubes(serie: str | None = None, uf: str | None = None):
  session = Session(get_engine())
  
  statement = select(Clube)
  
  if serie:
    statement = statement.where(Clube.serie == serie)

  if uf:
    statement = statement.where(Clube.uf == uf) 

  clubes = session.exec(statement).all()

  return clubes


@router.get('/{clube_id}')
def detalhes_clube(clube_id: int):
  with Session(get_engine()) as session:
    sttm = select(Clube).where(Clube.id == clube_id)
    clube = session.exec(sttm).one_or_none()
    if clube:
      return clube

  # nao localizou
  raise HTTPException(
    status_code=status.HTTP_404_NOT_FOUND,
    detail=f'Clube não localizado com id = {clube_id}'
    )



@router.post('', status_code=status.HTTP_201_CREATED)
def criar_clube(request_clube: RequestClube):
  clube = Clube(
    nome=request_clube.nome, 
    serie=request_clube.serie)
  
  session = Session(get_engine())
  session.add(clube)
  session.commit()
  session.refresh(clube)

  return clube

@router.put('/{clube_id}')
def alterar_clube(clube_id: int, dados: RequestClube):
  with Session(get_engine()) as session:
    sttm = select(Clube).where(Clube.id == clube_id)
    clube = session.exec(sttm).one_or_none()
    
    if clube:
      clube.nome = dados.nome
      clube.serie = dados.serie
      session.add(clube)
      session.commit()
      session.refresh(clube)
      return clube
  
  raise HTTPException(
    status_code=status.HTTP_404_NOT_FOUND,
    detail=f'Clube não localizado com id = {clube_id}'
  )

@router.delete('/{clube_id}', status_code=status.HTTP_204_NO_CONTENT)
def remover_clube(clube_id: int):
  with Session(get_engine()) as session:
    sttm = select(Clube).where(Clube.id == clube_id) 
    clube = session.exec(sttm).one_or_none()
    if clube:
      session.delete(clube)
      session.commit()
      return

  raise HTTPException(
    status_code=status.HTTP_404_NOT_FOUND,
    detail=f'Clube não localizado com id = {clube_id}'
  )
