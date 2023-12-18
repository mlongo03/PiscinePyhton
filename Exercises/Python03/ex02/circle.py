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

	def contains(self, point):
		distance_squared = (point.x - self.center.x)**2 + (point.y - self.center.y)**2
		return distance_squared <= self.radius**2

def main():
	import sys
	center = Point(float(sys.argv[1]), float(sys.argv[2]))
	circle = Circle((0, 0), 1)
	if (circle.contains(center)) == True:
		print(f"The Point ({center.x}, {center.y}) lies in the Circle of center (0, 0) and radius 1")
	else:
		print(f"The Point ({center.x}, {center.y}) lies out the Circle of center (0, 0) and radius 1")

if __name__ == "__main__":
	main()
