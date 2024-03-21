from sqlalchemy.orm import declarative_base,sessionmaker
from sqlalchemy import create_engine,Column,Integer,String


Base = declarative_base()

class Client(Base):
    __tablename__ = "clients"
    
    id = Column(Integer(),primary_key=True)
    name = Column(String())
    phone = Column(Integer())
    location = Column(String())
    
    def __repr__(self):
        return f"<Client(name={self.name}, phone={self.phone}, location={self.location})>"
    
    # @property
    # def phone(self):
    #     return self._phone 
    
    # @phone.setter
    # def phone(self,phone):
    #     if isinstance(phone,str) and len(str(phone)) == 10:
    #         self._phone = phone 
    #     else:
    #         return "The phone number should be 10 digits and should start with 07 or 01"    
    
class Driver(Base):
    __tablename__ = "drivers"
    
    id = Column(Integer(),primary_key=True)
    name = Column(String())
    phone = Column(Integer())
    location = Column(Integer())
    
    
    def __repr__(self):   
        return f"<Client(name={self.name}, phone={self.phone}, location={self.location})>"
    
    
    
    
        

    
   
    
