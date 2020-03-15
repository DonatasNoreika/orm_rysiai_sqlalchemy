from sqlalchemy import Column, Integer, String, Float, ForeignKey, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

engine = create_engine('sqlite:///one2many_test.db')
Base = declarative_base()


class Tevas(Base):
    __tablename__ = "tevas"
    id = Column(Integer, primary_key=True)
    vardas = Column("Vardas", String)
    pavarde = Column("Pava  rdė", String)
    vaikai = relationship("Vaikas")


class Vaikas(Base):
    __tablename__ = "vaikas"
    id = Column(Integer, primary_key=True)
    vardas = Column("Vardas", String)
    pavarde = Column("Pavardė", String)
    mokymo_istaiga = Column("Mokymo įskaita", String)
    tevas_id = Column(Integer, ForeignKey("tevas.id"))
    tevas = relationship("Tevas")


Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

# Nustatyti vaiką
# vaikas = Vaikas(vardas="Vaikas", pavarde="Vaikaitis")
# vaikas2 = Vaikas(vardas="Vaikas 2", pavarde="Vaikaitis 2")
# tevas = Tevas(vardas="Tevas", pavarde="Vaikaitis")
# tevas.vaikai.append(vaikas)
# tevas.vaikai.append(vaikas2)
# session.add(tevas)
# session.commit()

# Kaip nuskaityti tėvo vaikus
# tevas = session.query(Tevas).get(1)
# for vaikas in tevas.vaikai:
#     print(vaikas.vardas, vaikas.pavarde)

# Pakeisti tėvo vaiko duomenis
# tevas = session.query(Tevas).get(1)
# tevas.vaikai[0].vardas = "Vaikas 1"
# session.commit()

# Gauti vaiko tėvą
# vaikas = session.query(Vaikas).get(1)
# print(vaikas.tevas.vardas)

# Kaip ištrinti tėvo vaiką
tevas = session.query(Tevas).get(1)
vaikas1 = tevas.vaikai[0]
tevas.vaikai.remove(vaikas1)
session.commit()

# while True:
#     pasirinkimas = int(input("Pasirinkti veiksmą: 1 - įvesti tėvą su vaiku, 2 - išeiti iš programos"))
#     if pasirinkimas == 1:
#         tevo_vardas = input("Įveskite tėvo vardą ")
#         tevo_pavarde = input("Įveskite tėvo pavardę ")
#         vaiko_vardas = input("Įveskite vaiko vardą ")
#         vaiko_pavarde = input("Įveskite vaiko pavardę ")
#         vaikas = Vaikas(vardas=vaiko_vardas, pavarde=vaiko_pavarde)
#         tevas = Tevas(vardas=tevo_vardas, pavarde=tevo_pavarde, vaikas=vaikas)
#         session.add(tevas)
#         session.commit()
#     if pasirinkimas == 2:
#         break
