from .configs.db import SessionLocal, Base, engine
from .models.models import *


def create_database():
    return Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()