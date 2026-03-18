from vehicle import Vehicle

class Car(Vehicle):
    def __init__(self, vehicle_id, brand, model, rental_price_per_day, num_doors, fuel_type):
        super().__init__(vehicle_id, brand, model, rental_price_per_day, True)
        self.num_doors = num_doors
        self.fuel_type = fuel_type
    
    def display_info(self):
        print(f"[Car] {self.brand} {self.model} | Doors: {self.num_doors} | Fuel: {self.fuel_type} | Price/day: {self.rental_price_per_day} PKR | Available: {self.is_available}")
              
        
          