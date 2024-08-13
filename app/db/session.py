from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# SQLALCHEMY_DATABASE_URL = "postgresql://postgres:toor@127.0.0.1:5432/gymbro"  # 1
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:cJkQiRi7b7iFbK4LhU9m@containers-us-west-122.railway.app:7906/railway"
#! Implement sqlite in frontend to enable offline functionality (local database)
SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"

#engine = create_engine(
#    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
#)
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, 
)



# engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(
    autocommit=False, autoflush=False, bind=engine)  # 4

Base = declarative_base()
