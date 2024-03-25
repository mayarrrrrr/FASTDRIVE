from fdmodels import create_engine,Base,sessionmaker,Driver
from faker import Faker

engine = create_engine("sqlite:///fastdrive.db")
Base.metadata.create_all(engine)
    
session = sessionmaker(bind=engine)
mysession = session()

fakedata = Faker()

print("Seeding drivers")

# clearing data before seeding
mysession.query(Driver).delete()

location = ["Westlands",
    "Kasarani",
    "Embakasi East",
    "Embakasi West",
    "Embakasi Central",
    "Embakasi North",
    "Embakasi South",
    "Starehe",
    "Lang'ata",
    "Kibra",
    "Dagoretti North",
    "Dagoretti South",
    "Mathare",
    "Roysambu",
    "Ruaraka",
    "Makadara"]

for i in range(30):
    driver = Driver(name=fakedata.name(),phone = fakedata.phone_number(), location=fakedata.random_element(location))
    mysession.add(driver)
    mysession.commit()
    
print("All drivers have been seeded")    
    
    
    

