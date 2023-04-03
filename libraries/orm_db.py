from sqlmodel import create_engine, Session
from models import PublicMeta
import os
# sqlite_file = "databese.db"
# engine = create_engine(f"sqlite:///{sqlite_file}", echo=True)

host= os.getenv("HOST")
user=os.getenv("USERNAME")
passwd= os.getenv("PASSWORD")
db= os.getenv("DATABASE")
ssl_mode = "VERIFY_IDENTITY"
ssl      = {"ca": "cert.pem"}


# mysql database aws
engine = create_engine(
    f"mysql+pymysql://{user}:{passwd}@{host}/{db}",
    echo=True,
    connect_args={"ssl": ssl},
)
