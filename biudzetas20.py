from sqlalchemy import Column, Integer, String, Float, ForeignKey, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

engine = create_engine('sqlite:///biudzetas.db')
Base = declarative_base()


class Biudzetas(Base):
    __tablename__ = "biudzetas"
    id = Column(Integer, primary_key=True)
    name = Column("Pavadinimas", String)
    irasai_ids = relationship("Irasas", backref="biudzetas")


class Irasas(Base):
    __tablename__ = "irasas"
    id = Column(Integer, primary_key=True)
    suma = Column("Suma", Float)
    biudzetas_id = Column(Integer, ForeignKey('biudzetas.id'))


Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

# Įdėti biudžetą
# biudzetas1 = Biudzetas(name="Antras biudžetas")
# session.add(biudzetas1)
# session.commit()

# Gauti biudžetą ir pridėti įrašą
# biudzetas2 = session.query(Biudzetas).get(1)
# print(biudzetas2.name)
# irasas1 = Irasas(suma=20.0, biudzetas=biudzetas2)
# session.add(irasas1)
# session.commit()

# Gauti biudžeto įrašus:
# biudzetas2 = session.query(Biudzetas).get(1)
# print(biudzetas2.irasai_ids)
