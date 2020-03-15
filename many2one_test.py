from sqlalchemy import Column, Integer, String, ForeignKey, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

engine = create_engine('sqlite:///many2one_test.db')
Base = declarative_base()


class Tevas(Base):
    __tablename__ = "tevas"
    id = Column(Integer, primary_key=True)
    vardas = Column("Vardas", String)
    pavarde = Column("Pavardė", String)
    vaikas_id = Column(Integer, ForeignKey('vaikas.id'))
    vaikas = relationship("Vaikas")


class Vaikas(Base):
    __tablename__ = "vaikas"
    id = Column(Integer, primary_key=True)
    vardas = Column("Vardas", String)
    pavarde = Column("Pavardė", String)
    mokymo_istaiga = Column("Mokymo įskaita", String)

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

# Crud
# Kaip įrašyti tėvą ir jo vaiką
# vaikas = Vaikas(vardas="Vaikas", pavarde="Tevaika", mokymo_istaiga = "Čiurlionio gimnazija")
# tevas = Tevas(vardas="Tevas", pavarde="Tevaika", vaikas=vaikas)
# session.add(tevas)
# session.commit()

# cRUd
# Pakeisti tėvo ar vaiko duomenis
# Priskirti kitą vaiką:
# vaikas = Vaikas(vardas="Naujas vaikas", pavarde="Tevaika")
# tevas = session.query(Tevas).get(1)
# tevas.vaikas = vaikas
# session.commit()

# Pakeisti tėvo vaiko duomenis
# tevas = session.query(Tevas).get(1)
# tevas.vaikas.pavarde = "Naujapavardaitis"
# session.commit()

# cruD
# Kaip ištrinti tėvų ir vaikų įrašus
tevas = session.query(Tevas).get(1)
session.delete(tevas)
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