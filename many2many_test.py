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


# Kaip pridėti daug tėvų su daug vaikų
# tevas1 = Tevas(vardas="Tėvas", pavarde="Tėvaika")
# tevas2 = Tevas(vardas="Motina", pavarde="Tevienė")
# vaikas1 = Vaikas(vardas="Vaikas", pavarde="Tėvaika")
# vaikas2 = Vaikas(vardas="Vaikė", pavarde="Tėvaikytė")
#
# tevas1.vaikai.append(vaikas1)
# tevas2.vaikai.append(vaikas1)
# tevas2.vaikai.append(vaikas2)
#
# session.add(tevas1)
# session.add(tevas2)
# session.commit()

# Kaip gauti visus tėvo vaikus:

# tevas = session.query(Tevas).get(2)
# for vaikas in tevas.vaikai:
#     print(vaikas.vardas, vaikas.pavarde)

# Kaip gauti visus vaiko tėvus:

# vaikas = session.query(Vaikas).get(1)
# for tevas in vaikas.tevai:
#     print(tevas.vardas, tevas.pavarde)

# Kaip pakeisti tėvo vaiko įrašą:
tevas = session.query(Tevas).get(2)
tevas.vaikai[0].vardas = "Vaikas 1"
session.commit()

# Kaip ištrinti tėvo vaiko įrašą:

tevas = session.query(Tevas).get(2)
vaikas1 = tevas.vaikai[0]
tevas.vaikai.remove(vaikas1)
session.commit()

tevas = session.query(Tevas).get(2)
for vaikas in tevas.vaikai:
    print(vaikas.vardas, vaikas.pavarde)