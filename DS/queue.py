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


class Queue:
	"""first in first out"""
	def __init__(self):
		self.items: list = []

	def dequeue(self):
		# ternary operator
		return self.items.pop() if not self.isEmpty() else print("No data in stack")
		
	def enqueue(self, ele):
		self.items.insert(0, ele)

	def isEmpty(self):
		return self.items == []

	def size(self):
		return len(self.items)


class QueueChecker(Queue):
	def __init__(self):
		super().__init__()

	def add_ele(self):
		self.enqueue(12)
		self.enqueue(13)
		self.enqueue(14)
		self.enqueue(15)
		print(f"stack : {self.items}")
		self.dequeue()
		print(self.items)
		self.dequeue()
		self.dequeue()
		print(self.items)
		self.enqueue(17)
		print(self.items)
		self.dequeue()
		print(self.items)
		self.dequeue()

if __name__ == '__main__':
	c = QueueChecker()
	c.add_ele()