from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def root():
  return "API is working now 😎"
