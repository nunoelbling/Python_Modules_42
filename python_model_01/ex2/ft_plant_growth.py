class Plant:
	def __init__(self, name: str, height: float, age: int):
		self.name = name
		self.height = height
		self.age = age
	
	def show(self):
		print(f"{self.name}: {self.height}cm, {self.age} days old")
	
	def grow(self, amount: float):
		self.height += amount
	
	def age_plant(self, days: int = 1):
		self.age += days

if __name__ == "__main__":
	print("=== Garden Plant Growth ===")

	rose = Plant("Rose", 25.0, 30)
	rose.show()
	initial_height = rose.height

	for day in range(1, 8):
		print(f"=== Day {day} ===")
		rose.grow(0.8)
		rose.age_plant(1)
		print(f"{rose.name}: {round(rose.height, 1)}cm, {rose.age} days old")
	total_growth = rose.height - initial_height
	print(f"Growth this week: {round(total_growth, 1)}cm")
