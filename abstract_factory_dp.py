

from abc import ABC, abstractmethod


class Chair(ABC):
    @abstractmethod
    def sit_on(self) -> str:
        pass

class Sofa(ABC):
    @abstractmethod
    def lie_on(self) -> str:
        pass

class CoffeeTable(ABC):
    @abstractmethod
    def use(self) -> str:
        pass


class ModernChair(Chair):
    def sit_on(self) -> str:
        return "Sitting on a modern chair."

class ModernSofa(Sofa):
    def lie_on(self) -> str:
        return "Lying on a modern sofa."

class ModernCoffeeTable(CoffeeTable):
    def use(self) -> str:
        return "Using a modern coffee table."


class VictorianChair(Chair):
    def sit_on(self) -> str:
        return "Sitting on a Victorian chair."

class VictorianSofa(Sofa):
    def lie_on(self) -> str:
        return "Lying on a Victorian sofa."

class VictorianCoffeeTable(CoffeeTable):
    def use(self) -> str:
        return "Using a Victorian coffee table"


class FurnitureFactory(ABC):
    @abstractmethod
    def create_chair(self) -> Chair:
        pass

    @abstractmethod
    def create_sofa(self) -> Sofa:
        pass

    @abstractmethod
    def create_coffee_table(self) -> CoffeeTable:
        pass


class ModernFurnitureFactory(FurnitureFactory):
    def create_chair(self) -> Chair:
        return ModernChair()

    def create_sofa(self) -> Sofa:
        return ModernSofa()

    def create_coffee_table(self) -> CoffeeTable:
        return ModernCoffeeTable()

class VictorianFurnitureFactory(FurnitureFactory):
    def create_chair(self) -> Chair:
        return VictorianChair()

    def create_sofa(self) -> Sofa:
        return VictorianSofa()

    def create_coffee_table(self) -> CoffeeTable:
        return VictorianCoffeeTable()


def client_code(factory: FurnitureFactory) -> None:
    chair = factory.create_chair()
    sofa = factory.create_sofa()
    coffee_table = factory.create_coffee_table()

    print(chair.sit_on())
    print(sofa.lie_on())
    print(coffee_table.use())

if __name__ == "__main__":
    print("Client: Testing client code with ModernFurnitureFactory:")
    modern_factory = ModernFurnitureFactory()
    client_code(modern_factory)

    print("\nClient: Testing client code with VictorianFurnitureFactory:")
    victorian_factory = VictorianFurnitureFactory()
    client_code(victorian_factory)
