from pdb import set_trace


class CreditCard:

	def __init__(self, customer, bank, acnt, limit):
		"""
		Create a new credit card instance. 
		The initial balance is zero.
		"""
		self._customer = customer
		self._bank = bank
		self._account = acnt
		self._limit = limit
		self._balance = 0

	def get_customer(self):
		"""Return the name of the customer"""
		return self._customer

	def get_bank(self):
		"""Return the bank's name"""
		return self._bank

	def get_account(self):
		"""Return the card identifying number (typically a str)"""
		return self._account

	def get_limit(self):
		"""Return current credit limit"""
		return self._limit

	def get_balance(self):
		"""Return current balance"""
		return self._balance

	def charge(self, price):
		"""
		Charge given price to the card, assuming sufficient credit limit.

		Return True if charge was processed, False if charge was denied
		"""
		if price + self._balance > self._limit:
			return False
		else:
			self._balance += price
			return True

	def make_payment(self, amount):
		"""Process customer payment that reduces the balance"""
		self._balance -= amount


class PredatoryCreditCard(CreditCard):
	"""An extension to CredicCard that compounds interest and fees"""
	def __init__(self, customer, bank, acnt, limit, apr):
		"""Create a new predatory credit cart instance."""

		super().__init__(customer, bank, acnt, limit)	#call super constructor
		self._apr = apr

	def charge(self, price):
		"""Charge given price to the card, assuming sufficient credit limit.
		Return True if charge was processed
		Return False and assess $5 fee if charge is denied"""

		success = super().charge(price)			#call inherited method
		if not success:
			self._balance += 5					#casses penalty
		return success

	def get_balance(self):
		return round(self._balance, 2)

	def process_month(self):
		"""Asses monthly interest on outstanding balance"""
		if self._balance > 0:
			monthly_factor = pow(1 + self._apr, 1/12)
			self._balance *= monthly_factor
			self._balance = round(self._balance, 2)
			# set_trace()

	def get_apr(self):
		return str(100*self._apr) + '%'




# if __name__ == '__main__':
# 	wallet = []
# 	wallet.append(PredatoryCreditCard('John Bowman', 'California Savings', '5391 0375 9387 5309', 2500, .195))
# 	wallet.append(PredatoryCreditCard('John Bowman', 'California Federal', '3485 1235 1235 1522', 3500, .20))
# 	wallet.append(PredatoryCreditCard('John Bowman', 'California Finance', '1524 5107 3587 2357', 5000, .21))

# 	for val in range(1, 17):
# 		wallet[0].charge(val)
# 		wallet[1].charge(2*val)
# 		wallet[2].charge(3*val)
# 		wallet[0].process_month()
# 		wallet[1].process_month()
# 		wallet[2].process_month()

# 	for c in range(3):
# 		print('Customer = ', wallet[c].get_customer())
# 		print('Bank = ', wallet[c].get_bank())
# 		print('Account = ', wallet[c].get_account())
# 		print('Limit = ', wallet[c].get_limit())
# 		print('Balance = ', wallet[c].get_balance())
# 		print('APR = ', wallet[c].get_apr())
# 		while wallet[c].get_balance()>100:
# 			wallet[c].make_payment(100)
# 			print('New balance = ', wallet[c].get_balance())
# 		print()
# if __name__ == '__main__':
# 	wallet = []
# 	wallet.append(CreditCard('John Bowman', 'California Savings', '5391 0375 9387 5309', 2500))
# 	wallet.append(CreditCard('John Bowman', 'California Federal', '3485 1235 1235 1522', 3500))
# 	wallet.append(CreditCard('John Bowman', 'California Finance', '1524 5107 3587 2357', 5000))

# 	for val in range(1, 17):
# 		wallet[0].charge(val)
# 		wallet[1].charge(2*val)
# 		wallet[2].charge(3*val)

# 	for c in range(3):
# 		print('Customer = ', wallet[c].get_customer())
# 		print('Bank = ', wallet[c].get_bank())
# 		print('Account = ', wallet[c].get_account())
# 		print('Limit = ', wallet[c].get_limit())
# 		print('Balance = ', wallet[c].get_balance())
# 		while wallet[c].get_balance()>100:
# 			wallet[c].make_payment(100)
# 			print('New balance = ', wallet[c].get_balance())
# 		print()


class Vector:
	"""Represent a vector in multidimensional space"""

	def __init__(self, d):
		"""Create d-dimensional vector of zeros"""
		self._coords = [0] * d

	def __len__(self):
		"""return the dimension of the vector"""
		return len(self._coords)

	def __getitem__(self, j):
		"""return the jth coordinate of vector"""
		return self._coords[j]

	def __setitem__(self,j,val):
		"""Set jth coordinate of vector to given value"""
		self._coords[j] = val

	def __add__(self, other):
		"""return sum of two vectors"""
		if len(self) != len(other):		#relies on __len__method
			raise ValueError('dimensions must agree')
		result = Vector(len(self))
		for j in range(len(self)):
			result[j] = self[j] + other[j]
		return result

	def __eq__(self, other):
		"""Return True if vector has same coordinates as other"""
		return self._coords == other._coords

	def __ne__(self, other):
		"""Return True if vectors differ from each other"""
		return not self == other		#relies on existing __eq__method

	def __str__(self):
		"""Produce string representation of vector."""
		return '<' + str(self._coords)[1:-1] + '>'		#adapt list representation

# if __name__ == '__main__':
# 	x = Vector(3)
# 	x[0] = 1
# 	x[1] = 2
# 	x[2] = 3
# 	y = Vector(3)
# 	y[0] = 4
# 	y[1] = 8
# 	y[2] = 10

# 	z= x + y

# 	print(z) #why does z have the <> notation printed on screen?
# 	print(str(z))


class SequenceIterator:
	"""An Iterator for any of python's sequence types"""
	def __init__(self, sequence):
		self._seq = sequence
		self._k = -1			#will increment to 0 on first call to next

	def __next__(self):
		"""Return the next element, or else raise StopIteration error."""
		self._k += 1
		if self._k < len(self._seq):
			return (self._seq[self._k])
		else:
			raise StopIteration()

	def __iter__(self):
		"""By convention, an iterator must return itself as an iterator"""
		return self


# if __name__ == "__main__":
# 	# y = SequenceIterator([3,2,4,5])
# 	# a = next(y)
# 	# print(y)

# 	# while True:
# 	# 	print(a)
# 	# 	a = next(y)
# 	r = range(8, 140, 5)
# 	print(len(r))
# 	print(next(r))

class Range:
	"""A class that mimics the built-in range class"""

	def __init__(self, start, stop=None, step=1):
		if step ==0:
			raise ValueError('step cannot be zero')

		if stop is None:			#special case of range(n)
			start, stop = 0, start 	#should be treated as if range(0,n)

		#calculate the effective length once
		self._length = max(0, (stop - start + step - 1) // step)

		#need knowledge of start and step (but not stop) to support __getitem__
		self._start = start
		self._step = step

	def __len__(self):
		"""Return number of entries in the range"""
		return self._length

	def __getitem__(self, k):
		"""Return entry at index k (using standard interpretation if negative)"""
		if k < 0:
			k += len(self)			#attempt to convert negative index

		if not 0<= k < self._length:
			raise IndexError('index out of range')

		return self._start + k*self._step

# # r = Range(10)
# r = Range(10, 11, 1)
# for i in r:
# 	print(i)

class Progression:
	"""Iterator producing a generic progression.

	Default iterator  produces the whole numbers 0, 1, 2..."""

	def __init__(self, start=0):
		"""Initialize current to the first value of the progression"""
		self._current = start

	def _advance(self):
		"""Update self._current to a new val.

		This should be overriden by a subclass to customize progression.

		By convention, if current is set to None, this designates the
		end of a finite progression"""

		self._current += 1

	def __next__(self):
		"""Return the next element, or else raise StopIteration error."""
		if self._current is None:			#our convention to end a progression
			raise StopIteration()
		else:
			answer = self._current		#record current value to return
			self._advance()				#advance to prepare for next time
			return answer				#return the answer

	def __iter__(self):
		"""By convention, an iterator must return itself as an iterator"""
		return self

	def print_progression(self, n):
		"""print next n values of the progression"""
		print(" ".join(str(next(self)) for i in range(n)))


# p = Progression()
# p.print_progression(10)

class ArithmeticProgression(Progression):
	"""Iterator producing an arithmetic pogression"""

	def __init__(self, increment = 1, start = 0):
		"""create a new arithmetic progression
		increment   the fixed constant to add to each term (default 1)
		start       the first term of the progression (default 0)
		"""

		super().__init__(start)			#initialize base class
		self._increment = increment

	def _advance(self):
		self._current += self._increment


# a = ArithmeticProgression(10, 3)
# a.print_progression(100)

class GeometricProgression(Progression):
	def __init__(self, base = 2, start = 1):
		super().__init__(start)
		self._base = base

	def _advance(self):
		self._current *= self._base


# g = GeometricProgression(3, 1)
# g.print_progression(20)


class FibonacciProgression(Progression):

	def __init__(self, first = 0, second = 1):

		super().__init__(first)
		self._prev = second - first

	def _advance(self):
		self._prev, self._current = self._current, self._prev + self._current

# f = FibonacciProgression()
# f.print_progression(20)


from abc import ABCMeta, abstractmethod

class Sequence(metaclass=ABCMeta):
	"""Our own version of collections.Sequence abstract base class"""

	@abstractmethod
	def __len__(self):
		"""return the length of the sequence"""

	@abstractmethod
	def __getitem__(self,j):
		"""Return the element at index j of the sequence"""

	def __contains__(self, val):
		for j in range(len(self)):
			if self[j] == val:
				return True
		return False

	def index(self, val):
		"""Return leftmost index at which val is found (or raise ValueError)"""
		for j in range(len(self)):
			if self[j] == val:
				return j
		raise ValueError('value not in sequence')

	def count(self, val):
		"""Return the number of elements equal to given value"""
		k = 0
		for j in range(len(self)):
			if self[j] == val:
				k += 1
		return k


# R-2.1
"""
Give three examples of life-critical software applications.

1) Self-driving cars -- if there is a software failure, it can lead to fatal accidents.
2) insulin checker -- a person who has diabetes must always track his/her insulin intake, and they rely on 
machines that can check their blood 
3) Air traffic control with radar signalling -- software is used to process the radar signals, making it vital 
for air travel safety
"""

#R-2.2
"""
Give an example of a software application in which adaptability can mean
the difference between a prolonged lifetime of sales and bankruptcy.

Being adaptable means that the code is flexible so that it can run in different kinds of hardware and different
operating systems.  A company should be able to respond quickly when environment changes.  
"""

#R-2.3
"""
Describe a component from a text-editor GUI and the methods that it en-
capsulates.

One component is language recognition so that it colors the code appropriately.
its methods would include checking the file extension. If a file extension is not inserted, it will 
use its default color coding scheme on the text.
"""

#R-2.4
"""
Write a Python class, Flower, that has three instance variables of type str,
int, and float, that respectively represent the name of the flower, its num-
ber of petals, and its price. Your class must include a constructor method
that initializes each variable to an appropriate value, and your class should
include methods for setting the value of each type, and retrieving the value
of each type.
"""
class Flower:
	def __init__(self, name, petals, price):
		self._name = name
		self._petals = petals
		self._price = price

	def get_name(self):
		return self._name

	def get_petals(self):
		return self._petals

	def get_price(self):
		return self._price

	def set_name(self, name):
		self._name = name

	def set_petals(self, petals):
		self._petals = petals

	def set_price(self, price):
		self._price = price

# f = Flower('sunflower', 24, 1.25)
# print(f.get_name())
# print(f.get_petals())
# print(f.get_price())
# f.set_name('rose')
# f.set_petals(32)
# f.set_price(1.45)
# print(f.get_name())
# print(f.get_petals())
# print(f.get_price())

#R-2.5
"""
Use the techniques of Section 1.7 to revise the charge and make payment
methods of the CreditCard class to ensure that the caller sends a number
as a parameter.
"""


#R-2.6
"""
If the parameter to the make payment method of the CreditCard class
were a negative number, that would have the effect of raising the balance
on the account. Revise the implementation so that it raises a ValueError if
a negative value is sent.
"""

#P-2.33
"""
Write a Python program that inputs a polynomial in standard algebraic
notation and outputs the first derivative of that polynomial.
"""
