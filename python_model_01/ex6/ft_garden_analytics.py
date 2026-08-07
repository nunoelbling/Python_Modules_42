class Plant:
    @staticmethod
    def check_year_old(days: int) -> bool:
        return days > 365
    @classmethod
    def anonymous_plant(cls):
        return cls("Unknown plant", 0.0, 0)

    class Stats:
        def __init__(self):
            self.grow_calls = 0
            self.age_calls = 0
            self.show_calls = 0

        def display(self):
            print(f"Stats: {self.grow_calls} grow, {self.age_calls} age, {self.show_calls} show")

    def __init__(self, name: str, height: float, age: int, *args, **kwargs):
        self.name = name
        self._height = height
        self._age = age
        self.stats = self.Stats()

    def show(self):
            self.stats.show_calls += 1
            print(f"{self.name}: {self._height}cm, {self._age} days old")

    def grow(self, amount: float):
            self.stats.grow_calls += 1
            self._height += amount

    def age_plant(self, days: int = 1):
            self.stats.age_calls += 1
            self._age += days

class Flower(Plant):
    def __init__(self, name: str, height: float, age: int, color: str):
        super().__init__(name, height, age)
        self.color = color
        self.is_bloomed = False

    def bloom(self):
        self.is_bloomed = True

    def show(self):
        self.stats.show_calls += 1
        print(f"{self.name}: {self._height}cm, {self._age} days old")
        print(f"Color: {self.color}")
        if self.is_bloomed:
            print(f"{self.name} is blooming beautifully!")
        else:
            print(f"{self.name} has not bloomed yet")

class Tree(Plant):
    class TreeStats(Plant.Stats):
        def __init__(self):
            super().__init__()
            self.shade_calls = 0

        def display(self):
            print(f"Stats: {self.grow_calls} grow, {self.age_calls} age, {self.show_calls} show")
            print(f"{self.shade_calls} shade")

    def __init__(self, name: str, height: float, age: int, trunk_diameter: float):
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter
        self.stats = self.TreeStats()

    def produce_shade(self):
        self.stats.shade_calls += 1
        print(f"Tree {self.name} now produces a shade of {self._height}cm long and {self.trunk_diameter}cm wide.")

    def show(self):
        self.stats.show_calls +=1
        print(f"{self.name}: {self._height}cm, {self._age} days old")
        print(f"Trunk diameter: {self.trunk_diameter}cm")

class Seed(Flower):
    def __init__(self, name: str, height: float, age: int, color: str):
        super().__init__(name, height, age, color)
        self.seeds = 0

    def bloom(self):
        super().bloom()
        self.seeds = 42

    def show(self):
        super().show()
        print(f"Seeds: {self.seeds}")

def display_statistics(plant: Plant):
    plant.stats.display()


if __name__ == "__main__":
    print("=== Garden statistics ===")

    print("Check year-old")
    print(f"Is 30 days more than a year? -> {Plant.check_year_old(30)}")
    print(f"Is 400 days more than a year? -> {Plant.check_year_old(400)}")

    print("\nFlower")
    rose = Flower("Rose", 15.0, 10, "red")
    rose.show()
    print("[statistics for Rose]")
    display_statistics(rose)

    print("[asking the rose to gtrow and bloom]")
    rose.grow(8.0)
    rose.bloom()
    rose.show()
    print("[statistics for Rose]")
    display_statistics(rose)

    print("\nTree")
    oak = Tree("Oak", 200.0, 365, 5.0)
    oak.show()
    print("[statistics for Oak]")
    display_statistics(oak)

    print("[asking the oak to produce shade]")
    oak.produce_shade()
    print("[statistics for Oak]")
    display_statistics(oak)

    print("\n=== Seed")
    sunflower = Seed("Sunflower", 80.0, 45, "yellow")
    sunflower.show()
    print("[make sunflower grow, age and bloom]")
    sunflower.grow(30.0)
    sunflower.age_plant(20)
    sunflower.bloom()
    sunflower.show()
    print("[statistics for Sunflower]")
    display_statistics(sunflower)

    print("\nAnonymous")
    anon = Plant.anonymous_plant()
    anon.show()
    print("[statistics for Unknown plant]")
    display_statistics(anon)