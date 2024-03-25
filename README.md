# FASTDRIVE PROJECT

- This is a CLI project that is about making trip orders.

# Problem statement

- Online ordered trips have a downside of not letting client choose the drivers of their choice.

# Problem solution

- This app enables clients to see a list of drivers with their location and chose from there.



# Implementation

- Creating a python file(fdmodels) to store all the model classes. 

- The model classes are: CLient, Trip and Order.

- Client class and Driver class have name,phone and location  attributes.

- Trip class has customer_id,driver_id,start_location,end_location,start_time and price as attributes

- The relationship between Client and Driver (individually) with Trip is one-to-many.

- Meanwhile Client and Driver have a many-to-many relationship.

- Connect the database using SQLAlchemy...This creates tables for the instantiated classes.


# Command Line Interface(CLI)

- Create a crud file to handle the functionalities of the cli which are:

    -Adding a new client(add_client).
    
    -Displaying a list of drivers(list_drivers).

    -Confirm trip(finds the driver and client by name then adds trip to the database).

    - Cancel trip(delete_trip).

    - Exit

- Create a cli file to incorporate crud functionalities in the terminal.