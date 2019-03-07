from pdb import set_trace


class CreditCard:

	def __init__(self, customer, bank, acnt, limit, balance = 0):
		"""
		Create a new credit card instance. 
		The initial balance is zero.
		"""
		self._customer = customer
		self._bank = bank
		self._account = acnt
		self._limit = limit
		self._balance = balance
		self._charge_count = 0

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
		if not isinstance(price, (float, int)):
			raise ValueError('price must be a number.')
		if price + self._balance > self._limit:
			print(f"Credit card with account number {self._account} denied. Accrued balance over limit.")
			return False
		else:
			self._balance += price
			self._charge_count += 1
			if self._charge_count > 10:
				self._balance += 1	#$1 surcharge for all calls after 10 charges
			return True

	def make_payment(self, amount):
		if not isinstance(amount, (int, float)):
			raise ValueError('payment must be a number')
		elif amount < 0:
			raise ValueError('payment must be positive')
		"""Process customer payment that reduces the balance"""
		self._balance -= amount

from datetime import datetime

class PredatoryCreditCard(CreditCard):
	"""An extension to CredicCard that compounds interest and fees"""
	def __init__(self, customer, bank, acnt, limit, apr):
		"""Create a new predatory credit cart instance."""

		super().__init__(customer, bank, acnt, limit)	#call super constructor
		self._apr = apr
		self._cycle = 0
		self._minpay = 0
		self._late_fee = False
		self._override_limit = False

	def _set_balance(self, b):
		self._balance = b

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
		fee = 10
		if self._late_fee:
			success = self.charge(fee)
		self._cycle += 1
		prev_month = self._balance
		self._minpay = round(.4*prev_month, 2)
		if self._balance > 0:
			if self._balance >= self._limit:
				self._override_limit = True
			monthly_factor = pow(1 + self._apr, 1/12)
			self._set_balance(self._balance*monthly_factor)
			# set_trace()

	def make_payment(self, amount):
		super().make_payment(amount)
		if self._minpay > 0:
			self._late_fee = True
			self._minpay -= amount
			if self._minpay >= 0:
				self._late_fee = False
		else:
			self._late_fee = False





	def get_apr(self):
		return str(100*self._apr) + '%'

# c = CreditCard('liz', 'bofa', '123 123 123 123', 2500)
# print(c.get_balance())
# c = CreditCard('liz', 'bofa', 'xxxx xxxx xxxx 1234', 2500, 553.20)
# print(c.get_balance())


# if __name__ == '__main__':
# 	wallet = []
# 	wallet.append(PredatoryCreditCard('John Bowman', 'California Savings', '5391 0375 9387 5309', 2500, .195))
# 	wallet.append(PredatoryCreditCard('John Bowman', 'California Federal', '3485 1235 1235 1522', 3500, .20))
# 	wallet.append(PredatoryCreditCard('John Bowman', 'California Finance', '1524 5107 3587 2357', 5000, .21))

# 	for val in range(1, 30):
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

# 	for val in range(1, 25):
# 		wallet[0].charge(val*val)
# 		wallet[1].charge(val*val)
# 		wallet[2].charge(val*val)

# 	for c in range(3):
# 		print('Customer = ', wallet[c].get_customer())
# 		print('Bank = ', wallet[c].get_bank())
# 		print('Account = ', wallet[c].get_account())
# 		print('Limit = ', wallet[c].get_limit())
# 		print('Balance = ', wallet[c].get_balance())
# 		# while wallet[c].get_balance()>100:
# 		# 	wallet[c].make_payment(100)
# 		# 	print('New balance = ', wallet[c].get_balance())
# 		print()

from copy import deepcopy

class Vector:
	"""Represent a vector in multidimensional space"""

	def __init__(self,data):
		"""Create d-dimensional vector of zeros"""
		is_list = False

		try:
			for i in data:
				break
			is_list = True
		except:
			is_list = False

		if is_list:
			copy_data = deepcopy(list(data))
			for i in copy_data:
				if not isinstance(i, (int, float)):
					raise TypeError('Iterable must contain sequence of numbers only.')
			self._coords = copy_data
		elif isinstance(data,int):
				self._coords = [0] * data
		else:
			raise TypeError('Arg passed must be an iterable of numbers or int')

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

	def __radd__(self, other):
		"""To ensure that the sum of other + vector will work, i.e. if other
		is on the right side."""
		return self + other

	def __mul__(self, other):
		"""Return product of two vectors"""
		if not isinstance(other, (int, float, Vector, list)):
			raise ValueError('factor must be a number or vector')
		if isinstance(other, (int, float)):
			product = Vector(len(self))
			for j in range(len(self)):
				product[j] = self[j]*other
			return product
		elif len(self) != len(other):
			raise ValueError('dimensions must agree')
		else:
			dot_product = 0
			for i in range(len(self)):
				dot_product += self[i] * other[i]
			return dot_product

	def __rmul__(self, other):
		"""To ensure that the product of scalar * vector will work, i.e. if scalar
		is on the right side."""
		return self * other

	def __neg__(self):
		"""return the negation of vector"""
		return self * -1

	def __sub__(self, other):
		"""return difference of two vectors"""
		other = -other
		return self + other

	def __eq__(self, other):
		"""Return True if vector has same coordinates as other"""
		return self._coords == other._coords

	def __ne__(self, other):
		"""Return True if vectors differ from each other"""
		return not self == other		#relies on existing __eq__method

	def __str__(self):
		"""Produce string representation of vector."""
		return '<' + str(self._coords)[1:-1] + '>'		#adapt list representation

if __name__ == '__main__':
	# x = Vector(3)
	# x[0] = 1
	# x[1] = 2
	# x[2] = 3
	# y = Vector(3)
	# y[0] = 4
	# y[1] = 8
	# y[2] = 10

	# z= 3*x
	# z =  x * 2
	z = Vector([1, 2,3])
	y = Vector(4)

	# print(y) #why does z have the <> notation printed on screen?
	# print(-z)
	# print(str(z))


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

class ReversedSequenceIterator:
	def __init__(self, sequence):
		seq_copy = deepcopy(list(sequence))
		self._seq = sequence
		self._k = len(sequence) 

	def __next__(self):
		self._k -= 1
		if self._k > -1:
			return (self._seq[self._k])
		else:
			raise StopIteration()

	def __iter__(self):
		return self


r = ReversedSequenceIterator([1,2,3,4])

# for i in range(len(r._seq)):
# 	print(next(r))
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
		self._stop = stop

	def __len__(self):
		"""Return number of entries in the range"""
		return self._length

	def __getitem__(self, k):
		"""Return entry at index k (using standard interpretation if negative)"""
		if k < 0:
			k += len(self)			#attempt to convert negative index

		if not 0<= k < self._length:
			raise IndexError('index out of range')
		# set_trace()
		return self._start + k*self._step

	def __contains__(self, k):
		start = self._start
		slope = self._step
		if k >= self._stop or k < start:
			raise IndexError('index out of range')
		elif (k-start)%slope == 0:
			return True
		else:
			return False



# r = Range(10)
r = Range(10, 200, 10)
# print(200 in r)

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


class SqrRt(Progression):
	def __init__(self, start = 65536):
		super().__init__(start)

	def _advance(self):
		self._current = self._current**(0.5)

# s = SqrRt()
# s.print_progression(4)
class AbsValueDiff(Progression):
	"""
		a Python class that extends the Progression class so that each value
		in the progression is the absolute value of the difference between the pre-
		vious two values.
	"""
	def __init__(self, first = 2, second = 200):
		super().__init__(first)
		self._prev = abs(second - first)

	def _advance(self):
		self._prev, self._current = self._current, abs(self._current - self._prev)


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

	def __eq__(self, other):
		"""checks if two sequences are equivalent"""
		if len(self) != len(other):
			return False
		for j in range(len(self)):
			for i in range(len(other)):
				if self[j] == other[i]:
					pass
				else:
					return False
		return True

	def __lt__(self, other):
		"""Checks if one sequence is lexigraphically less than the other sequence"""
		for j in range(len(self)):
			if self[j] > other[j]:
				return False
		return True

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

see line 43-44 and 52-53
"""


#R-2.6
"""
If the parameter to the make payment method of the CreditCard class
were a negative number, that would have the effect of raising the balance
on the account. Revise the implementation so that it raises a ValueError if
a negative value is sent.

See line 54-55
"""

#R-2.7
"""
The CreditCard class of Section 2.3 initializes the balance of a new ac-
count to zero. Modify that class so that a new account can be given a
nonzero balance using an optional fifth parameter to the constructor. The
four-parameter constructor syntax should continue to produce an account
with zero balance.

See lines 6-15
"""

#R-2.8
"""
Modify the declaration of the first for loop in the CreditCard tests, from
Code Fragment 2.3, so that it will eventually cause exactly one of the three
credit cards to go over its credit limit. Which credit card is it?

See line 46.  It was the credit card from California Savings.
"""

#R-2.9
"""
Implement the sub method for the Vector class of Section 2.3.3, so
that the expression u−v returns a new vector instance representing the
difference between two vectors.

See lines 220-223
"""

#R-2.10
"""
Implement the neg method for the Vector class of Section 2.3.3, so
that the expression −v returns a new vector instance whose coordinates
are all the negated values of the respective coordinates of v.

See lines 216-218
"""

#R-2.11
"""
In Section 2.3.3, we note that our Vector class supports a syntax such as
v = u + [5, 3, 10, −2, 1], in which the sum of a vector and list returns
a new vector. However, the syntax v = [5, 3, 10, −2, 1] + u is illegal.
Explain how the Vector class definition can be revised so that this syntax
generates a new vector.

See lines 189-192
"""

#R-2.12
"""
Implement the mul method for the Vector class of Section 2.3.3, so
that the expression v 3 returns a new vector with coordinates that are 3
times the respective coordinates of v.

See lines 194-202
"""

#R-2.13
""""
Exercise R-2.12 asks for an implementation of mul , for the Vector
class of Section 2.3.3, to provide support for the syntax v * 3. Implement
the rmul method, to provide additional support for syntax 3 * v.

See lines 211-214
"""

#R-2.14
"""
Implement the mul method for the Vector class of Section 2.3.3, so
that the expression u v returns a scalar that represents the dot product of
the vectors.

See lines 205-209
"""

#R-2.15
"""
The Vector class of Section 2.3.3 provides a constructor that takes an in-
teger d, and produces a d-dimensional vector with all coordinates equal to
0. Another convenient form for creating a new vector would be to send the
constructor a parameter that is some iterable type representing a sequence
of numbers, and to create a vector with dimension equal to the length of
that sequence and coordinates equal to the sequence values. For example,
Vector([4, 7, 5]) would produce a three-dimensional vector with coordi-
nates <4, 7, 5>. Modify the constructor so that either of these forms is
acceptable; that is, if a single integer is sent, it produces a vector of that
dimension with all zeros, but if a sequence of numbers is provided, it pro-
duces a vector with coordinates based on that sequence.

See lines 153-166
"""

#R-2.16
"""
Our Range class, from Section 2.3.5, relies on the formula
max(0, (stop − start + step − 1) // step)
to compute the number of elements in the range. It is not immediately ev-
ident why this formula provides the correct calculation, even if assuming
a positive step size. Justify this formula, in your own words.

Interpretation of denominator:
You have to divide by the step as that will account for the partitioning
of the range by an equal amount. You have to use floor division because
the range function should only output countable numbers.
Interpretation of numerator:
You have to subtract the numerator by stop - start as that represents the distance.
You have to subtract by 1 because the end is not inclusive.
You have to also add the step value to ensure the last element will be outputted.

You have to use max to ensure there'll be an output, to avoid bugs
"""

#R-2.18
"""
When using the ArithmeticProgression class of Section 2.4.2 with an in-
crement of 128 and a start of 0, how many calls to next can we make
before we reach an integer of 2^63 or larger?
"""
a = ArithmeticProgression(increment = 128)
# a.print_progression(72050000000000000)
#Technically, you can figure this out by computing 2^63/128, but this would take a long time to compute

#R-2.19
"""
Give a short fragment of Python code that uses the progression classes
from Section 2.4.2 to find the 8 th value of a Fibonacci progression that
starts with 2 and 2 as its first two values.
"""
f = FibonacciProgression(first = 2, second= 2)
# f.print_progression(8)
#8th value is 42

#R-2.20
"""
What are some potential efficiency disadvantages of having very deep in-
heritance trees, that is, a large set of classes, A, B, C, and so on, such that
B extends A, C extends B, D extends C, etc.?

The higher you go in your heirarchy, the more prone you will be for unknown bugs.
If you invoke an instantiation of class A and is not successful, you'd have to inspect
the code going down the hierarchy, which can take lots of time.
"""

#R-2.21
"""
What are some potential efficiency disadvantages of having very shallow
inheritance trees, that is, a large set of classes, A, B, C, and so on, such
that all of these classes extend a single class, Z?

if you have a really shallow inheritance tree, it may imply that Z is not robust enough
to generate an appropriate abstraction for these 'child' trees. This means that
many parts of Z will be overriden, which defeats the purpose of inheritance.  
"""
 
#R-2.22
"""
The collections.Sequence abstract base class does not provide support for
comparing two sequences to each other. Modify our Sequence class from
Code Fragment 2.14 to include a definition for the eq method, so
that expression seq1 == seq2 will return True precisely when the two
sequences are element by element equivalent.

See lines 429-439
"""

#R-2.23
"""
In similar spirit to the previous problem, augment the Sequence class with
method lt , to support lexicographic comparison seq1 < seq2.

see lines 441-446
"""

#C-2.24
"""
Suppose you are on the design team for a new e-book reader. What are the
primary classes and methods that the Python software for your reader will
need? You should include an inheritance diagram for this code, but you
do not need to write any actual code. Your software architecture should
at least include ways for customers to buy new books, view their list of
purchased books, and read their purchased books.

Book class --> get_price(), get_id(), get_author(), num_of_pages(), get_summary()
	Book(title, author, price, unique_id, summary, pages)
Nested in Book will be a Page class --> read_text(), highlight_chars(seq_of_chars), 
get_page_number(), next_page(), go_to_page(n)
	Page(page_number, text)
Customer Class --> get_account_info(), see_shelf(), read_book(title), buy_book(title)
	Customer(account_info, shelf)
"""

#C-2.25
"""
Exercise R-2.12 uses the __mul__ method to support multiplying a Vector
by a number, while Exercise R-2.14 uses the mul method to support
computing a dot product of two vectors. Give a single implementation of
Vector. mul that uses run-time type checking to support both syntaxes
u*v and u*k, where u and v designate vector instances and k represents
a number.

SEe lines 194-202
"""

#C-2.26

"""
The SequenceIterator class of Section 2.3.4 provides what is known as a
forward iterator. Implement a class named ReversedSequenceIterator that
serves as a reverse iterator for any Python sequence type. The first call to
next should return the last element of the sequence, the second call to next
should return the second-to-last element, and so forth.

See lines 280-294

"""

#C-2.27
"""
In Section 2.3.5, we note that our version of the Range class has im-
plicit support for iteration, due to its explicit support of both len
and getitem . The class also receives implicit support of the Boolean
test, “k in r” for Range r. This test is evaluated based on a forward itera-
tion through the range, as evidenced by the relative quickness of the test
2 in Range(10000000) versus 9999999 in Range(10000000). Provide a
more efficient implementation of the contains method to determine
whether a particular value lies within a given range. The running time of
your method should be independent of the length of the range.

SEe lines 345-353
"""

#C-2.28 
"""
The PredatoryCreditCard class of Section 2.4.1 provides a process month
method that models the completion of a monthly cycle. Modify the class
so that once a customer has made ten calls to charge in the current month,
each additional call to that function results in an additional $1 surcharge.

See lines 16 and 50-54
"""

#C-2.29
"""
Modify the PredatoryCreditCard class from Section 2.4.1 so that a cus-
tomer is assigned a minimum monthly payment, as a percentage of the
balance, and so that a late fee is assessed if the customer does not subse-
quently pay that minimum amount before the next monthly cycle.

see lines 100-210
"""

#c-2.30
"""
At the close of Section 2.4.1, we suggest a model in which the CreditCard
class supports a nonpublic method, set balance(b), that could be used
by subclasses to affect a change to the balance, without directly accessing
the balance data member. Implement such a model, revising both the
CreditCard and PredatoryCreditCard classes accordingly.

see lines 194-205
"""

#C-2.31
"""
Write a Python class that extends the Progression class so that each value
in the progression is the absolute value of the difference between the pre-
vious two values. You should include a constructor that accepts a pair of
numbers as the first two values, using 2 and 200 as the defaults.

See lines 431-441
"""

#C-2.32
"""
Write a Python class that extends the Progression class so that each value
in the progression is the square root of the previous value. (Note that
you can no longer represent each value with an integer.) Your construc-
tor should accept an optional parameter specifying the start value, using
65, 536 as a default.

See lines 431-436
"""

#P-2.33
"""
Write a Python program that inputs a polynomial in standard algebraic
notation and outputs the first derivative of that polynomial.
"""

def compare(a, b):
	if a < 0 and b < 0:
		return None
	elif b < 0:
		return a
	elif a < 0:
		return b
	else:
		return min(a,b)

def find_parts(t):
	exp_check = t.find('^')
	if exp_check == -1:
		exp_check = t.find('x')
		if exp_check == -1:
			return ''
		else:
			return t[:exp_check]
	else:
		coeff, deg = t[:exp_check], t[exp_check+1:]
		coeff = coeff[:coeff.find('x')]
		float_check = coeff.find('.')
		if float_check == -1:
			coeff = int(coeff)
		else:
			coeff = float(coeff)
		deg = int(deg)
		return coeff, deg

# def first_derivative_polynomial(polynomial):
# 	idx = 0
# 	pos_idx = polynomial.find('+', idx)
# 	neg_idx = polynomial.find('-', idx)
# 	start_loop = compare(pos_idx, neg_idx)
# 	expr = []

# 	while start_loop:
# 		term = polynomial[idx:start_loop]
# 		derived_term = find_parts(term)
# 		expr.append(new_coeff+'x^'+new_deg)


#P-2.34
"""
Write a Python program that inputs a document and then outputs a bar-
chart plot of the frequencies of each alphabet character that appears in
that document.
"""
import matplotlib.pyplot as plt


def char_analysis(file):
	f = open(file, 'rb')
	abc_dict = dict()
	for i in range(26):
		abc_dict[chr(ord('a')+i)] = 0
	for line in f:
		sline = line.strip(b'\n')
		for char in sline:
			l_c = chr(char).lower()
			if l_c in abc_dict:
				abc_dict[l_c] += 1

	plt.bar(range(len(abc_dict)), list(abc_dict.values()), align='center')
	plt.xticks(range(len(abc_dict)), list(abc_dict.keys()))
	plt.show()




f = 'LICENSE.txt'
# char_analysis(f)

#P-2.35 
"""
Write a set of Python classes that can simulate an Internet application in
which one party, Alice, is periodically creating a set of packets that she
wants to send to Bob. An Internet process is continually checking if Alice
has any packets to send, and if so, it delivers them to Bob’s computer, and
Bob is periodically checking if his computer has a packet from Alice, and,
if so, he reads and deletes it.
"""

# class WorkerA:
# 	def __init__(self)

#P-2.36
"""
Write a Python program to simulate an ecosystem containing two types
of creatures, bears and fish. The ecosystem consists of a river, which is
modeled as a relatively large list. Each element of the list should be a
Bear object, a Fish object, or None. In each time step, based on a random
process, each animal either attempts to move into an adjacent list location
or stay where it is. If two animals of the same type are about to collide in
the same cell, then they stay where they are, but they create a new instance
of that type of animal, which is placed in a random empty (i.e., previously
None) location in the list. If a bear and a fish collide, however, then the
fish dies (i.e., it disappears).
"""




