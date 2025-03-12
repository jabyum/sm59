from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
# подключение к базе данных на sqlite
SQLALCHEMY_DATABASE_URI = "sqlite:///data.db"
# подключение к базе данных на postgre
# SQLALCHEMY_DATABASE_URI = "postgresql://postgres:admin@localhost/social_media"
engine = create_engine(SQLALCHEMY_DATABASE_URI)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

# Создание сессии
def get_db():
    db = SessionLocal()
    try:
        yield db
    except Exception:
        db.rollback()
        raise
    finally:
        db.close()
