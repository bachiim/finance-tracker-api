from sqlmodel import create_engine, Session

DATABASE_URL = "mysql+mysqlconnector://root:@127.0.0.1:3306/finance-track"
engine = create_engine(DATABASE_URL)

def get_db():
  with Session(engine) as session:
    yield session