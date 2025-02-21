from fastapi import APIRouter, HTTPException
from app.core.database import SessionDep
from app.schemas.AccountSchema import *
from app.models.Accounts import *

router = APIRouter(prefix='/accounts')

# create
@router.post('/', response_model=AccountRead)
def create(account: AccountCreate, session: SessionDep):
  accounts = Accounts(**account.model_dump())
  session.add(accounts)
  session.commit()
  session.refresh(accounts)
  return accounts

# read
@router.get('/', response_model=list[AccountRead])
def read(session: SessionDep):
  return session.query(Accounts).all()

# show
@router.get('/{id}', response_model=AccountRead)
def show(id: int, session: SessionDep):
  account = session.query(Accounts).filter(Accounts.id == id).first()
  if account is None:
    raise HTTPException(status_code=404, detail='Account not found')
  return account
