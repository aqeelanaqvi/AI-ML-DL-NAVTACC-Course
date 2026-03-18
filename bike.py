from vehicle import Vehicle

class Bike(Vehicle):
    def __init__(self, vehicle_id, brand, model, rental_price_per_day, engine_cc, bike_type):
        super().__init__(vehicle_id, brand, model, rental_price_per_day, True)
        self.engine_cc = engine_cc
        self.bike_type = bike_type

    def display_info(self):
        print(f"[Bike] {self.brand} {self.model} | Engine: {self.engine_cc} | Type: {self.bike_type} | Price/day: {self.rental_price_per_day} PKR | Available: {self.is_available}")
    