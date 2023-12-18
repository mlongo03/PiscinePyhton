class Person:
	def __init__(self, name, last_name):
		self.name = name
		self.last_name = last_name

	def __str__(self):
		return f"{self.name} {self.last_name}"

class Student(Person):
	def __init__(self, name, last_name, degree=None):
		super().__init__(name, last_name)
		self.degree = degree

	def __str__(self):
		if (self.degree == None):
			return f"{super().__str__()} is not registered to any course"
		return f"{super().__str__()} is registered to {self.degree}"


def main():
	name = input("Insert first name: ")
	last_name = input("Insert last name: ")
	answer = input("Are you a student? (y/n)")
	while answer != "y" and answer != "n":
		answer = input("Please type \"y\" or \"n\": ")
	if answer == "y":
		degree = input("Please insert your degree course: ")
		print(Student(name, last_name, degree))
	else:
		print(Person(name, last_name))

if __name__ == "__main__":
	main()
