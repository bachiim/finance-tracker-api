from fastapi import FastAPI
from .endpoints import accounts

app = FastAPI()

app.include_router(accounts.router)

@app.get('/')
def root():
  return "API is working now 😎"