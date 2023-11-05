import pandas as pd
from json import load
from sqlalchemy import create_engine, Column, Float, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


with open('services\pg_config.json', 'r') as json_file:
    data = load(json_file)
    usuario = data["user"]
    password = data["password"]
    database = data["database"]
    server = data["server"]

db_url = f"postgresql://{usuario}:{password}@{server}/{database}"
Base = declarative_base()

#Creacion de tabla

class Predicciones(Base):
    __tablename__ = "predicciones"

    id = Column(Integer, primary_key=True)
    GDP_per_capita = Column("GDP_per_capita", Float)
    life_expectancy = Column("life_expectancy", Float)
    freedom = Column("freedom", Float)
    perceptions_corruption = Column("perceptions_corruption", Float)
    generosity = Column("generosity", Float)
    happiness_score = Column("happiness_score", Float)
    happiness_score_prediction = Column("happiness_score_predction", Float)

#Function to Create Engine
def creating_engine():
    engine = create_engine(db_url)
    return engine

#Function to create the sessions
def creating_session(engine):
    Session = sessionmaker(bind=engine)
    session = Session()
    return session

#Function to close the session
def closing_session(session):
    session.close()

#Function to Dispose Engine
def disposing_engine(engine):
    engine.dispose()
    print("engine cerrado")