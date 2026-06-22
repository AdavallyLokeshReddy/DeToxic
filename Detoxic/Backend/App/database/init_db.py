from ..models.base import Base
from ..models import user, submission, prediction
from .connection import engine


def create_tables():
    Base.metadata.create_all(bind=engine)


if __name__ == "__main__":
    create_tables()
    print("Database tables created.")
