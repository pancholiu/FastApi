from .models import Shipment
from sqlalchemy import create_engine
from sqlmodel import SQLModel, Session

# To create a connection with the database
engine = create_engine(
    url="sqlite:///../sqlite.db",
    echo=True,
    connect_args={"check_same_thread": False}
)


def create_db_tables():
    SQLModel.metadata.create_all(bind=engine)


def get_session():
    with Session(bind=engine) as session:
        yield session
