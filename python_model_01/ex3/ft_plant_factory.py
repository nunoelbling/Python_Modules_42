class Plant:
	def __init__(self, name: str, height: float, age: int):
		self.name = name
		self.height = height
		self.age = age

	def show(self):
		print(f"Created: {self.name}: {self.height}cm, {self.age} days old")

if __name__ == "__main__":

	rose = Plant("Rose", 25, 30)
	rose.show()

	oak = Plant("Oak", 200, 365)
	oak.show()

	cactus = Plant("Cactus", 5, 90)
	cactus.show()

	sunflower = Plant("Sunflower", 80, 45)
	sunflower.show()

	fern = Plant("Fern", 15, 120)
	fern.show()