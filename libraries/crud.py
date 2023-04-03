from orm_db import engine
from sqlmodel import Session
from models import (PublicMeta, Content, ContentCategory, ContentTopic)


def _create_db_and_tables():
    PublicMeta.create_all(engine)

def create_category(category: ContentCategory):
    with Session(engine) as session:
        session.add(category)
        session.commit()
        session.refresh(category)
        return category