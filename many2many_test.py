from sqlalchemy import Column, Integer, String, Float, ForeignKey, create_engine, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

engine = create_engine('sqlite:///many2many_test.db')
Base = declarative_base()

association_table = Table('association', Base.metadata,
    Column('tevas_id', Integer, ForeignKey('tevas.id')),
    Column('vaikas_id', Integer, ForeignKey('vaikas.id'))
)

class Tevas(Base):
    __tablename__ = 'tevas'
    id = Column(Integer, primary_key=True)
    vardas = Column("Vardas", String)
    pavarde = Column("Pavardė", String)
    vaikai = relationship("Vaikas", secondary=association_table, back_populates="tevai")

class Vaikas(Base):
    __tablename__ = 'vaikas'
    id = Column(Integer, primary_key=True)
    vardas = Column("Vardas", String)
    pavarde = Column("Pavardė", String)
    tevai = relationship("Tevas", secondary=association_table, back_populates="vaikai")

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

tevas1 = Tevas(vardas="Tėvas", pavarde="Tėvaika")
tevas2 = Tevas(vardas="Motina", pavarde="Tevienė")
vaikas1 = Vaikas(vardas="Vaikas", pavarde="Tėvaika")
vaikas2 = Vaikas(vardas="Vaikė", pavarde="Tėvaikytė")

# Kaip pridėti tėvus ir vaikus
# tevas1.vaikai.append(vaikas1)
# tevas2.vaikai.append(vaikas1)
# tevas2.vaikai.append(vaikas2)
# session.add(tevas1)
# session.add(tevas2)
# session.commit()