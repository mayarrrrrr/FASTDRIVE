from fdmodels import Client,Driver,Trip,client_driver,desc
from seed import mysession

def add_client():
    client_name = input("Input your name: ")
    client_location = input("Input your current location: ")
    client_phone =input("Input your phone number: ")
    client =  Client(name= client_name, location = client_location,phone = client_phone)
    mysession.add(client)
    mysession.commit()
    
def list_drivers():
    
    drivers = mysession.query(Driver).all()
    # return drivers
    for driver in drivers:
        print([driver.name,driver.location])
        
def get_client_id_by_name(client_name):
    client = mysession.query(Client).filter_by(name=client_name).first()
    if client:
        return client.id
    else:
        return None  # Handle case where client with the given name doesn't exist

def get_driver_id_by_name(driver_name):
    driver = mysession.query(Driver).filter_by(name=driver_name).first()
    if driver:
        return driver.id
    else:
        return None  # Handle case where driver with the given name doesn't exist        
        
def confirm_trip():
    current_location = input("Input your current location: ")
    destination = input("Input your desired destination: ")
    
    # Prompt for client's name
    client_name = input("Input your name: ")
    
    # Prompt for driver's name
    driver_name = input("Input the driver's name: ")
    
    # Obtain client and driver IDs
    client_id = get_client_id_by_name(client_name)
    driver_id = get_driver_id_by_name(driver_name)
    print(client_id)
    
    if client_id is None:
        print("Client not found.You would want to make sure the name matches the logged name.Please try again.")
        return
    elif driver_id is None:
        print("Driver not found.You would want to make sure the name matches the listed drivers.Please try again.")
        return
    
    # Create a new Trip instance with obtained IDs
    trip = Trip(customer_id=client_id, driver_id=driver_id, start_location=current_location, end_location=destination,Price =  250.00)
    
    
    
    # Add the trip to the session and commit changes
    mysession.add(trip)
    mysession.commit()
    
    
def delete_trip():
    # Query for the most recent trip based on its creation timestamp
    delete_trip = mysession.query(Trip).order_by(desc(Trip.start_time)).first()
    
    # Check if a trip was found
    if delete_trip:
        # Delete the last trip from the session
        mysession.delete(delete_trip)
        mysession.commit()
        print("Last trip deleted successfully.")
    else:
        print("No trips found in the database.")
        

         
    
    
    
    
    
            
    
 
        