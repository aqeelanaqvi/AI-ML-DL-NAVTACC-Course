class RentalService:
    def __init__(self):
        self.vehicles = []
        self.customers = []

    def add_vehicle(self, vehicle):
        self.vehicles.append(vehicle)
        
    def register_customer(self, customer):
        self.customers.append(customer)
         
    def show_available_vehicles(self):
        print("Available Vehicles:")
        for v in self.vehicles:
            if v.is_available:
                v.display_info()
    
    def rent_vehicle(self, customer_id, vehicle_id, days):
        customer = None
        vehicle = None
        
        for c in self.customers:
            if c.customer_id == customer_id:
                customer = c
        
        for v in self.vehicles:
            if v.vehicle_id == vehicle_id:
                vehicle = v
        
        if customer and vehicle and vehicle.is_available:
            cost = vehicle.calculate_rental_cost(days)
            vehicle.rent()
            customer.rent_vehicle(vehicle)
            
            print("Vehicle rented successfully")
            print("Total cost:", cost, "PKR")
        else:
            print("Vehicle not available or wrong ID")
            
    def return_vehicle(self, customer_id):
        for c in self.customers:
            if c.customer_id == customer_id:
                if c.rented_vehicle:
                    c.rented_vehicle.return_vehicle()
                    c.return_vehicle()
                    print("Vehicle returned successfully")
                else:
                    print("Customer has not rented a vehicle")