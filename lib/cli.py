from crud import add_client,list_drivers,confirm_trip,delete_trip

def app():
    while True:
        
        print("1.Initiate a trip")
        print("2.Display available drivers")
        print("3.Confirm trip")
        print("4.Cancel trip")
        print("5.Exit")
        userinput = input("How can we help you?: ")
        
        if userinput == "1":
            add_client()
            input("Press enter to continue")
            
        elif userinput == "2":
            
            list_drivers()
        
        elif userinput == "3":
            confirm_trip() 
            
        elif userinput == "4":
             delete_trip()
        
        elif userinput =="5":
            return 0   
            
if __name__ == '__main__':
    app()                