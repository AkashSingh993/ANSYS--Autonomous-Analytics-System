# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker

# DATABASE_URL = "sqlite:///../chinook.db"

# engine = create_engine(
#     DATABASE_URL,
#     connect_args={"check_same_thread": False}
# )

# SessionLocal = sessionmaker(
#     autocommit=False,
#     autoflush=False,
#     bind=engine
# )

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

DATABASE_PATH = BASE_DIR / "chinook.db"

DATABASE_URL = f"sqlite:///{DATABASE_PATH}"

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)