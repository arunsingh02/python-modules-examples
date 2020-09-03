"""
1. class name should be in camle case
2. def name should be in snake case
3. class and def should have google style docstrirng
4. typing is required for parameters, return, and variables
5. don't use so more than 100 char in a single line
6. proper log required
7. proper use of if-else
8. file name match with the class name
"""


class Stack:
	"""Last in first out"""
	def __init__(self):
		self.items: list = []

	def pop(self):
		# ternary operator
		return self.items.pop() if self.items else print("No data in stack")

	def peak(self):
		return self.items[len(self.items) - 1]
		
	def push(self, ele):
		self.items.append(ele)

	def isEmpty(self):
		return self.items == []

	def size(self):
		return len(self.items)


class StackChecker(Stack):
	def __init__(self):
		super().__init__()

	def add_ele(self):
		self.push(12)
		self.push(13)
		self.push(14)
		self.push(15)
		print(f"stack : {self.items}")
		self.pop()
		print(self.peak())
		print(self.items)
		self.pop()
		print(self.peak())
		self.pop()
		self.pop()
		self.pop()

if __name__ == '__main__':
	c = StackChecker()
	c.add_ele()