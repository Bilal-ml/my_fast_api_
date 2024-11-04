from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import psycopg2
from psycopg2.extras import RealDictCursor
from .confih import settings
while True:
    try:
        conn = psycopg2.connect(host='localhost', database='fastapi', user='postgres', password='api123', cursor_factory=RealDictCursor )
        cursor = conn.cursor()
        print("successfully connected")
        break
    except Exception as err:
        print("failed to connect to db")
        print(f"error: {err}")
sqlalchemy_db_url = f"postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}"
engine = create_engine(sqlalchemy_db_url)
sessionLocal = sessionmaker(autoflush=False, autocommit=False, bind=engine)
Base = declarative_base()

def get_db():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()