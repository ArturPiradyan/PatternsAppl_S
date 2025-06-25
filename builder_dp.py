
class House:
    def __init__(self):
        self.parts = []

    def add_part(self, part):
        self.parts.append(part)

    def display(self):
        print("House parts:", ', '.join(self.parts))

from abc import ABC, abstractmethod

class Builder(ABC):
    @abstractmethod
    def build_walls(self): pass

    @abstractmethod
    def build_roof(self): pass

    @abstractmethod
    def build_doors(self): pass

    @abstractmethod
    def build_windows(self): pass

    @abstractmethod
    def get_house(self): pass

class SimpleHouseBuilder(Builder):
    def __init__(self):
        self.house = House()

    def build_walls(self):
        self.house.add_part("Simple walls")

    def build_roof(self):
        self.house.add_part("Simple roof")

    def build_doors(self):
        self.house.add_part("Simple doors")

    def build_windows(self):
        self.house.add_part("Simple windows")

    def get_house(self):
        return self.house

class FancyHouseBuilder(Builder):
    def __init__(self):
        self.house = House()

    def build_walls(self):
        self.house.add_part("Fancy walls with decorative patterns")

    def build_roof(self):
        self.house.add_part("Elaborate roof with skylights")

    def build_doors(self):
        self.house.add_part("Grand entrance doors with intricate carvings")

    def build_windows(self):
        self.house.add_part("Large windows with stained glass")

    def get_house(self):
        return self.house

class Director:
    def construct(self, builder):
        builder.build_walls()
        builder.build_roof()
        builder.build_doors()
        builder.build_windows()

if __name__ == "__main__":
    director = Director()

    simple_builder = SimpleHouseBuilder()
    director.construct(simple_builder)
    simple_house = simple_builder.get_house()
    print("Simple House:")
    simple_house.display()

    fancy_builder = FancyHouseBuilder()
    director.construct(fancy_builder)
    fancy_house = fancy_builder.get_house()
    print("\nFancy House:")
    fancy_house.display()
