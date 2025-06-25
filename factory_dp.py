

from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def drive(self):
        pass

    @abstractmethod
    def get_type(self):
        pass
class Car(Vehicle):
    def drive(self):
        return "Driving a car on four wheels."

    def get_type(self):
        return "Car"

class Motorcycle(Vehicle):
    def drive(self):
        return "Riding a motorcycle on two wheels."

    def get_type(self):
        return "Motorcycle"

class VehicleFactory:
    def create_vehicle(self, vehicle_type: str) -> Vehicle:
        if vehicle_type.lower() == "car":
            return Car()
        elif vehicle_type.lower() == "motorcycle":
            return Motorcycle()
        else:
            raise ValueError(f"Unknown vehicle type: {vehicle_type}")
if __name__ == "__main__":
    factory = VehicleFactory()

    try:
        car = factory.create_vehicle("car")
        print(f"Vehicle type: {car.get_type()}, Action: {car.drive()}")

        motorcycle = factory.create_vehicle("Motorcycle")
        print(f"Vehicle type: {motorcycle.get_type()}, Action: {motorcycle.drive()}")

    except ValueError as e:
        print(f"Error: {e}")