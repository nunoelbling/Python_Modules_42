class Plant:
    def __init__(self, name: str, height:float , age: int):
        self.name = name
        self._height = height if height >= 0 else 0.0
        self._age = age if age >= 0 else 0

    def show(self):
        print(f"{self.name}: {self._height}cm, {self._age} days old")

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age

    def set_height(self, height: float):
        if height < 0:
            print(f"{self.name}: Error, height can't be negative")
            print("Height update rejected")
        else:
            self._height = height
            print(f"Height updated: {int(height)}cm" if height.is_integer() else f"Height updated: {height}cm")

    def set_age(self, age: int):
        if age < 0:
            print(f"{self.name}: Error, age can't be negative")
            print("Age update rejected")
        else:
            self._age = age
            print(f"Age update: {age} days")

if __name__ == "__main__":
    print("=== Garden Security System ===")
    
    rose = Plant("Rose", 15.0, 10)
    print(f"Plant created: Rose: {rose.get_height()}cm, {rose.get_age()} days old")

    rose.set_age(30)
    rose.set_height(25.0)

    rose.set_height(-5.0)
    rose.set_age(-2)

    print(f"Current state: Rose: {rose.get_height()}cm,{rose.get_age()} days old")