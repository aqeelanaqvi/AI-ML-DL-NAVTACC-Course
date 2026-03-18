from rental_service import RentalService
from customer import Customer
from bike import Bike
from car import Car

service = RentalService()

# Add vehicles
bike1 = Bike("B101", "Honda", "CG125", 1000, "125cc", "Standard")
car1 = Car("C201", "Toyota", "Corolla", 4000, 4, "Petrol")
car2 = Car("C301", "Honda", "Civic", 6000, 4, "Petrol")

service.add_vehicle(bike1)
service.add_vehicle(car1)
service.add_vehicle(car2)

# Register customer
customer1 = Customer("CU1", "Ali")
customer2 = Customer("CU2", "Hassan")
service.register_customer(customer1)

while True:
    print("\n====== Vehicle Rental System ======")
    print("1. Show Available Vehicles")
    print("2. Rent Vehicle")
    print("3. Return Vehicle")
    print("4. View Customer Details")
    print("5. Exit")
    
    choice = input("Enter choice: ")
    
    if choice == "1":
        service.show_available_vehicles()
        
    elif choice == "2":
        cid = input("Enter Customer ID: ")
        vid = input("Enter Vehicle ID: ")
        days = int(input("Enter Number of Days: "))
        service.rent_vehicle(cid, vid, days)
        
    elif choice == "3":
        cid = input("Enter Customer ID: ")
        service.return_vehicle(cid)
        
    elif choice == "4":
        customer1.view_rented_vehicle()
        
    elif choice == "5":
        print("Exiting Program")
        break
        
    else:
        print("Invalid Choice")
    
    
    
        
    
        