class Point:
	def __init__(self, x, y):
		self.x = x
		self.y = y

class Circle:
	def __init__(self, center, radius):
		self.center = Point(*center)
		self.radius = radius

	def __str__(self):
		return f"Circle of center ({self.center.x}, {self.center.y}) and radius {self.radius}"

def main():
	circle = Circle((150, 100), 75)
	print(circle)

if __name__ == "__main__":
	main()
