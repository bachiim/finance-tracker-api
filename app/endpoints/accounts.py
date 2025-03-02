from fastapi import APIRouter, HTTPException
from sqlmodel import select

from app.core.database import SessionDep
from app.models.Account import *

router = APIRouter(prefix='/accounts')

# create
@router.post('/', response_model=AccountPublic)
def create(account: AccountCreate, session: SessionDep):
  try:
    db_account = Account.model_validate(account)
  except ValueError as e:
    raise HTTPException(status_code=400, detail=str(e))
  
  session.add(db_account)
  session.commit()
  session.refresh(db_account)
  return db_account

# read
@router.get('/', response_model=list[AccountPublic])
def read(session: SessionDep):
  accounts = session.exec(select(Account))
  return accounts

# show
@router.get('/{id}', response_model=AccountPublicWithRelations)
def show(id: int, session: SessionDep):
  statement = select(Account).where(Account.id == id)
  account = session.exec(statement).first()
  if account is None:
    raise HTTPException(status_code=404, detail='Account not found')
  return account

# update
@router.put('/{id}', response_model=AccountPublic)
def update(id: int, account: AccountUpdate, session: SessionDep):
  db_account = session.get(Account, id)
  if not account:
    raise HTTPException(status_code=400, detail='Account not found')
  
  account_data = account.model_dump(exclude_unset=True)
  db_account.sqlmodel_update(account_data)
  session.add(db_account)
  session.commit()
  session.refresh(db_account)
  return db_account
