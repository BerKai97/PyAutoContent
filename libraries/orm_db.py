from sqlmodel import create_engine, Session
from models import PublicMeta

sqlite_file = "databese.db"
engine = create_engine(f"sqlite:///{sqlite_file}", echo=True)

# PublicMeta.create_all(engine)