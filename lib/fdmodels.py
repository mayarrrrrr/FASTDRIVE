from sqlalchemy.orm import declarative_base,sessionmaker,relationship
from sqlalchemy import create_engine,Column,Integer,String,ForeignKey,DateTime,Float,Table,func,desc


Base = declarative_base()

client_driver = Table(
    "client_drivers",
    Base.metadata,
    
    Column('client_id',ForeignKey('clients.id'),primary_key=True),
    # Column('client_name',ForeignKey('clients.name')),
    # Column('driver_name',ForeignKey('drivers.name')),
      
    Column("driver_id",ForeignKey('drivers.id'),primary_key=True),
    extend_existing= True
  
    
)

class Client(Base):
    __tablename__ = "clients"
    
    id = Column(Integer(),primary_key=True)
    name = Column(String())
    phone = Column(Integer())
    location = Column(String())
    
    # one-to-many relationship(one client has many trips)
    trips = relationship('Trip',backref='client')
    
    # many-to-many relations between the clients and drivers
    drivers = relationship('Driver',secondary=client_driver, back_populates='clients')
    
    def __repr__(self):
        return f"<Client(name={self.name}, phone={self.phone}, location={self.location})>"
    
      
    
class Driver(Base):
    __tablename__ = "drivers"
    
    id = Column(Integer(),primary_key=True)
    name = Column(String())
    phone = Column(Integer())
    location = Column(String())
    
    # one-to-many relationship(one driver has many trips)
    trips = relationship('Trip',backref='driver')
    
    # many-to-many relationship between the drivers and clients
    clients = relationship("Client",secondary=client_driver, back_populates="drivers")
    
    def __repr__(self):   
        return f"<Client(name={self.name}, phone={self.phone}, location={self.location})>"
    
class Trip(Base):
    
    __tablename__ = "trips"
    
    id = Column(Integer(),primary_key=True)
    customer_id = Column(Integer(), ForeignKey('clients.id'))
    driver_id = Column(Integer(),ForeignKey("drivers.id"))
    start_location = Column(String, nullable=False)
    end_location = Column(String, nullable=False)
    start_time = Column(DateTime(), server_default=func.now())
    end_time = Column(DateTime(), server_default=func.now())
    
   
    Price = Column(Float)
    
    def __repr__(self):
        return f"<Trip(start_location={self.start_location}, end_location={self.end_location}, fare={self.price})>"

    @property
    def duration(self):
        if self.end_time:
            return (self.end_time - self.start_time).seconds / 60  # Duration in minutes
        else:
            return None
    
    
        
    
    
    
    
        

    
   
    
