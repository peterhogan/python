class List(object):
	
	def __init__(self, number):
		self.number = number

	def write_numbers(self):
		for i in self.number:
			print i

x = [1,2,3,4,5,6]
y = [6,6,6,6,6,6]

x.write_numbers()
y.write_numbers()
