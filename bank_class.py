class Customer(object):
	"""A customer of the ABC bank with an account.
	Every customer has a name and a balance."""

	def __init__(self, name, balance=0.0):
		self.name = name
		self.balance = balance

	def withdraw(self, amount):
		if amount > self.balance:
			raise RuntimeError("Amount greater than current balance.")
		self.balance -= amount
		return self.balance

	def deposit(self, amount):
		self.balance += amount
		return self.balance


me = Customer("Peter")

me.deposit(3000)

print me.balance

print "Withdraw some cash."

me.withdraw(1234)

print me.balance

print "Withdraw some more?"

me.withdraw(9999)



