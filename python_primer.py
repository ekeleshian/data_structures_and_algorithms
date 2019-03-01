from pdb import set_trace
### 1.1 Preview of Python Program

def preview_python():

	print('Welcome to the GPA calculator')
	print('Please enter all your letter grades, one per line.')
	print('Enter a blank line to designate the end.')

	points = {'A+' : 4.0, 'A':4.0, 'A-':3.67, 'B+':3.33, 'B': 3.0, 'B-': 2.67, 'C+':2.33, 'C': 2.0, 'C-': 1.67, 'D+':1.33,
	'D': 1.0, 'F': 0.0}

	num_courses = 0
	total_points = 0
	done = False
	while not done:
		grade = input()
		if grade == '':
			done = True
		elif grade not in points:
			print(f"Unknown grade {grade} being ignored.")
		else:
			num_courses += 1
			total_points += points[grade]
	if num_courses > 0:
		print(f'Your GPA is {total_points/num_courses:.3}')


# preview_python()


#############################################################

### 1.2 Objects in Python

# print(0o52)
# print(0b1011)
# print(0x7f)

# print('20\u20AC')
# print('liz\n\n\tkeleshian\n\n')

# b = [1, 2]
# array = [1, 'a', b]
# print(len(array))

# del array[2][0]
# print(len(array))
# del array[0]

# print(array)
# print(len(array))

set_one = set('elizabeth keleshian')
set_two = set('edgar aroutiounian')

# print(set_one | set_two) #union
# print(len(set_one | set_two))
# print(set_one & set_two) #intersection
# print(set_one - set_two) #elements in s1 and not in s2
# print(set_two - set_one)
# print(set_one ^ set_two)


###############################################################

### 1.5 Built-in Functions

# array = [1, 2, 3, -4]

array = [0,1]

a = [2,3,4]
b = 4
c = 5.4
d= set()

# print(all(array))
# print(any(array))

# print(hash(a)) #unhashable type: 'list'
# print(b, hash(b))
# print(c, hash(c))
# # print(hash(d)) #unhashable type: 'set'
# print(id(a))
# print(id(b))
# print(id(c))
# print(id(d))

# print(next(a))
# print(hash(-10.0))

# print(-10.0 == -10)

# print(type(10.0))

# print(-10.0 is -10)

# print(isinstance(-10, tuple))

################################################################

### 1.6 Input and Output

# reply = input('Enter x and y, separated by spaces: ')
# pieces = reply.split()
# x = float(pieces[0])
# y = float(pieces[1])
# print(x, y)


################################################################

### 1.7 Exception Handling

def sum(values):
	if not isinstance(values, (list, tuple, str)):
		raise TypeError('parameter must be an interable type')
	total = 0
	for v in values:
		if not isinstance(v, (int, float)):
			raise TypeError('elements must be numeric')
		total = total+v

	return total

# print(sum((1,2,'a',4)))
# from pdb import set_trace

# age = -1
# while age <= 0:
# 	try:
# 		assert False
# 		age = int(input('Enter your age in years: '))
# 		if age <= 0:
# 			print('Your age must be positive.')
# 	except Exception as e:
# 		print(e)
# 		set_trace()
# 		break



################################################################

### 1.8 Iterators and Generators

# data = [1,2,3,4]

# i = iter(data)

# print(next(i))
# print(next(i))
# data[2] = 0
# print(next(i))
# print(next(i))
# print(i)

# d = dict([('a', 1), ('b', 2), ('c', 3)])

# print(d.values())

# a = d.items()

# b = list(a)

# # print(next(a))
# i = iter(b)
# a = next(i)
# print(b)

# print(b[0][0], b[1][0], b[2][0])

def factors(n):
	for k in range(1, n+1):
		if n%k == 0:
			yield k

# print(vars(factors(10)))
# print(factors(10).close())


################################################################

### Exercises

#R-1.1
"""
Write a short Python function is multiple(n, m), that takes two integer
values and returns True if n is a multiple of m, that is, n = mi for some
integer i, and False otherwise
"""
def is_multiple(n,m):
	if n < 0 or m < 0:
		n, m = abs(n), abs(m)
	elif n == 0 or m == 0:
		print('must pass nonzero integers')
		return False
	for i in range(1,int(n/2)+1):
		if n == i*m:
			return True
	return False

# print(is_multiple(-100,0))


#R-1.2

"""
Write a short Python function, is even(k), that takes an integer value and
returns True if k is even, and False otherwise. However, your function
cannot use the multiplication, modulo, or division operators.
"""

def even(k):
	if k < 0:
		k = abs(k)
	while k > 0:
		k -= 2
	if k == 0:
		return True
	else:
		return False

# print(even(10))
# print(even(11))
# print(even(-12))
# print(even(-101))

#R-1.3
"""
Write a short Python function, minmax(data), that takes a sequence of
one or more numbers, and returns the smallest and largest numbers, in the
form of a tuple of length two. Do not use the built-in functions min or
max in implementing your solution.
"""

def minmax(data):
	min_val = data[0]
	max_val = data[0]
	if len(data) == 1:
		return data[0], data[0]
	for i in data[1:]:
		if i < min_val:
			min_val = i
		elif i > max_val:
			max_val = i
	return min_val, max_val

# print(minmax([1, 4, 2, 10, -12, 100, 4, 10]))
# print(minmax([1, 2]))
# print(minmax([1]))

#R-1.4
"""
Write a short Python function that takes a positive integer n and returns
the sum of the squares of all the positive integers smaller than n.
"""
def sum_of_squares(n):
	total = 0
	if n == 1:
		return 0
	for i in range(1,n):
		total += i*i
	return total

# print(sum_of_squares(4))


#R-1.5
"""
Give a single command that computes the sum from Exercise R-1.4, rely-
ing on Python’s comprehension syntax and the built-in sum function.
"""
# print(sum(i*i for i in range(1,4)))


#R-1.6
"""
Write a short Python function that takes a positive integer n and returns
the sum of the squares of all the odd positive integers smaller than n.
"""
def num_of_odd_squares(n):
	total = 0
	for i in range(1, n, 2):
		total += i*i
	return total

# print(num_of_odd_squares(4))

#R-1.7
"""
Give a single command that computes the sum from Exercise R-1.6, rely-
ing on Python’s comprehension syntax and the built-in sum function.
"""
# print(sum(i*i for i in range(1, 4, 2)))


#R-1.8
"""
Python allows negative integers to be used as indices into a sequence,
such as a string. If string s has length n, and expression s[k] is used for in-
dex −n ≤ k < 0, what is the equivalent index j ≥ 0 such that s[j] references
the same element?
"""
# j = -k - 1, so if k == -1, j = 0, and k == -2, j = 1


#R-1.9
"""
What parameters should be sent to the range constructor, to produce a
range with values 50, 60, 70, 80?
"""
# print(list(range(50, 81, 10)))

#R-1.10
"""
What parameters should be sent to the range constructor, to produce a
range with values 8, 6, 4, 2, 0, −2, −4, −6, −8?
"""

# print(list(range(-8, 9, 2)))

#R-1.11
"""
Demonstrate how to use Python’s list comprehension syntax to produce
the list [1, 2, 4, 8, 16, 32, 64, 128, 256].
"""

# print([2**i for i in range(9)])

#R-1.12
"""
Python’s random module includes a function choice(data) that returns a
random element from a non-empty sequence. The random module in-
cludes a more basic function randrange, with parameterization similar to
the built-in range function, that return a random choice from the given
range. Using only the randrange function, implement your own version
of the choice function
"""
from random import randrange
def my_choice(data):
	min_val = min(data)
	max_val = max(data)
	candidate = randrange(min_val, max_val+1)

	while True:
		if candidate in data:
			return candidate
		else:
			candidate = randrange(min_val, max_val+1)

my_data = [-10, 12, 15, 13, -15]
# print(my_choice(my_data))


#C-1.13
"""
Write a pseudo-code description of a function that reverses a list of n
integers, so that the numbers are listed in the opposite order than they
were before, and compare this method to an equivalent Python function
for doing the same thing.
"""
def reverse_list(array, first = 0):
	last = len(array) - 1 - first
	if first <= last:
		old_first = array[first]
		old_last = array[last]
		array[first] = old_last
		array[last] = old_first
		return reverse_list(array, first+1)
	else:
		return array

# print(reverse_list([1, 2, 3, 4,5]))

#python function that does the same thing
# array = [1,2,3,4,5]
# array.reverse()
# print(array)


#C-1.14
"""
Write a short Python function that takes a sequence of integer values and
determines if there is a distinct pair of numbers in the sequence whose
product is odd.
"""
seq = [1 ,2, 1, 4]
seq_one = [1, 2, 4, 6, 8]
seq_two = [1, 4, 2, 6, 3]

def is_product_odd(data):
	count = 0
	seen = set()
	for i in data:
		if i%2 != 0 and i not in seen:
			seen.add(i)
			count+= 1
	if count >= 2:
		return True
	else:
		return False

# print(is_product_odd(seq))

# print(is_product_odd(seq_one))

# print(is_product_odd(seq_two))


#C-1.15
"""
Write a Python function that takes a sequence of numbers and determines
if all the numbers are different from each other (that is, they are distinct).
"""
seq_one = [1, 4, 5, 6]
seq_two = [1, 1, 3, 4]

def is_unique(data):
	count = 0
	seen = set()
	for i in data:
		if i not in seen:
			seen.add(i)
		else:
			count +=1
	return False if count > 0 else True

# print(is_unique(seq_one))
# print(is_unique(seq_two))

#C-1.16
"""
In our implementation of the scale function (page 25), the body of the loop
executes the command data[j] *= factor. We have discussed that numeric
types are immutable, and that use of the *= operator in this context causes
the creation of a new instance (not the mutation of an existing instance).
How is it still possible, then, that our implementation of scale changes the
actual parameter sent by the caller?
"""
#data would have to be a list type so that when you access data[j] 
# and change its value, that means the jth entry of the array is now pointing to a new
# object which is of int or float.

#C-1.17
"""
Had we implemented the scale function (page 25) as follows, does it work
properly?
def scale(data, factor):
	for val in data:
		val *= factor
Explain why or why not.

No, this wouldn't work. val is an iterator
and only exists inside the scope of the for loop.  if you're simply assigning val to be a product
of itself and the factor, you're not mutating the list at all. in fact, since you're not 
mutating the list or returning anything, nothing is useful in this function.
"""

#C-1.18
"""
Demonstrate how to use Python’s list comprehension syntax to produce
the list [0, 2, 6, 12, 20, 30, 42, 56, 72, 90].
"""
# print([x**2 + x for x in range(10)])

#C-1.19
"""
Demonstrate how to use Python’s list comprehension syntax to produce
the list [ a , b , c , ..., z ], but without having to type all 26 such
characters literally.
"""
# print([chr(i) for i in range(ord('a'), ord('a')+26)])

#C-1.20
"""
Python’s random module includes a function shuffle(data) that accepts a
list of elements and randomly reorders the elements so that each possi-
ble order occurs with equal probability. The random module includes a
more basic function randint(a, b) that returns a uniformly random integer
from a to b (including both endpoints). Using only the randint function,
implement your own version of the shuffle function.
"""
from random import randint

def shuffle_data(array):
	max_idx = len(array) - 1
	seen_idx = set()
	length_array = len(array)
	new_array = []
	while len(seen_idx) != length_array:
		idx = randint(0, max_idx)
		if idx not in seen_idx:
			seen_idx.add(idx)
			new_array.append(array[idx])

	return new_array

data = [1, 4, 3, 5, 1, 23, 4]

# print(shuffle_data(data))

#C-1.21
"""
Write a Python program that repeatedly reads lines from standard input
until an EOFError is raised, and then outputs those lines in reverse order
(a user can indicate end of input by typing ctrl-D).
"""

def reverse_lines_from_input():
	results = []
	try:
		print('''Write a few lines of text, where each line is separated by pressing enter. 
			Type ctrl-D when done.\n''')
		while True:
			line = input()
			results.append(line)
	except EOFError as e:
		results.reverse()
		return results


# print(reverse_lines_from_input())

#C-1.22
"""
Write a short Python program that takes two arrays a and b of length n
storing int values, and returns the dot product of a and b. That is, it returns
an array c of length n such that c[i] = a[i] · b[i], for i = 0, . . . , n − 1.
"""

def dot_product(a, b):
	for i, (k,v) in enumerate(zip(a,b)):
		a[i] = k*v
	return a

# print(dot_product([1, 2, 3], [1, 2, 3]))		


#C-1.23
"""
Give an example of a Python code fragment that attempts to write an ele-
ment to a list based on an index that may be out of bounds. If that index
is out of bounds, the program should catch the exception that results, and
print the following error message:
“Don’t try buffer overflow attacks in Python!”
"""
def catch_index_error():
	array = [1,2,3]

	try:
		for i in range(4):
			array[i] = i 
	except IndexError:
		print('Dont try buffer overflow attacks in python!')
		return array

#C-1.24
"""
Write a short Python function that counts the number of vowels in a given
character string.
"""
def count_vowels(s):
	vowels = {'a', 'e', 'i', 'o', 'u', 'y'}
	counter = 0
	for i in s:
		counter +=1 if i in vowels else 0
	return counter

# print(count_vowels('edgar aroutiounian'))

#C-1.25
"""
Write a short Python function that takes a string s, representing a sentence,
and returns a copy of the string with all punctuation removed. For exam-
ple, if given the string "Let's try, Mike.", this function would return
"Lets try Mike".
"""
def remove_punctuations(s):
	puncs = {';', "'", '.',"\"",'!', '?', ',', ':' }
	array = list(s)
	for i, char in enumerate(array):
		if char in puncs:
			set_trace()
			del array[i]
	# set_trace()
	new_s = ''.join(array)

	return new_s

# print(remove_punctuations("hello, my name\'s liz. what is your name? \"my name is: Edgar.\"."))

#C-1.26
"""
Write a short program that takes as input three integers, a, b, and c, from
the console and determines if they can be used in a correct arithmetic
formula (in the given order), like “a + b = c,” “a = b − c,” or “a ∗ b = c.”
"""
def evaluate():
	abc = []
	print("Enter three numbers, separated by new line. Press ctrl-D when done.")
	try:
		while True:
			abc.append(input())
	except EOFError:
		arith_ops = {'+', '-', '*', '/'}
		a, b, c = abc
		for i in arith_ops:
			res = eval(a+i+b)
			if res == int(c):
				return a+i+b+'='+c
			res = eval(b+i+c)
			if res == int(a):
				return a+'='+b+i+c

# print(evaluate())

#C-1.27
"""
In Section 1.8, we provided three different implementations of a generator
that computes factors of a given integer. The third of those implementa-
tions, from page 41, was the most efficient, but we noted that it did not
yield the factors in increasing order. Modify the generator so that it reports
factors in increasing order, while maintaining its general performance ad-
vantages.
"""
def factors(n):
	k = 1
	stored_values = []
	while k*k < n:
		if n%k == 0:
			yield k
			stored_values.append(n//k)
		k+=1
	if k*k == n:
		yield k
	stored_values = sorted(stored_values)
	a = iter(stored_values)
	try:
		while a:
			yield(next(a))
	except StopIteration as e:
		yield e


# result = factors(256)
# try:
# 	while True:
# 		print(next(result))
# except StopIteration as e:
# 	print(e)

#C-1.28
"""
The p-norm of a vector v = (v 1 , v 2 , . . . , v n ) in n-dimensional space is de-
fined as

For the special case of p = 2, this results in the traditional Euclidean
norm, which represents the length of the vector.  Give an implemen-
tation of a function named norm such that norm(v, p) returns the p-norm
value of v and norm(v) returns the Euclidean norm of v. You may assume
that v is a list of numbers.
"""
def norm(v,p):
	total = []
	for elem in v:
		total.append(elem**p)
	return f'{sum(total)**(1/p):.3}'


# print(norm([4,3],2))

# P-1.29
"""
Write a Python program that outputs all possible strings formed by using
the characters c , a , t , d , o , and g exactly once.
"""
from itertools import permutations
def all_possible_strings(s):
	perm = permutations(s)
	perm = list(perm)
	for i in list(perm):
		print(''.join(i))
		
	print(len(perm))

# all_possible_strings('catdog')

# P-1.30
"""
Write a Python program that can take a positive integer greater than 2 as
input and write out the number of times one must repeatedly divide this
number by 2 before getting a value less than 2.
"""
def square_root_approx(n):
	count = 0
	while n >= 2:
		count += 1
		n = n/2
	return count

# print(square_root_approx(100000))

# P-1.31
"""
Write a Python program that can “make change.” Your program should
take two numbers as input, one that is a monetary amount charged and the
other that is a monetary amount given. It should then return the number
of each kind of bill and coin to give back as change for the difference
between the amount given and the amount charged. The values assigned
to the bills and coins can be based on the monetary system of any current
or former government. Try to design your program so that it returns as
few bills and coins as possible.
"""
from collections import Counter

def make_change(amnt_due, amnt_paid):
	change = amnt_paid - amnt_due
	total_bills = []
	denominations = {
	0.01: 'penny(ies)',
	0.05: 'nickel(s)', 
	0.1: 'dime(s)',
	0.25: 'quarter(s)',
	1: 'one dollar bill(s)',
	5: 'five dollar bill(s)', 
	10: 'ten dollar bill(s)',
	20: 'twenty dollar bill(s)',
	50: 'fifty dollar bill(s)',
	100: 'one hundred dollar bill(s)'
	}
	while change > 0:
		min_change = 0.01
		for key in denominations:
			# set_trace()
			if min_change <= key <= change:
				min_change = key
		total_bills.append(denominations[min_change])
		change -= min_change
		change = round(change, 2)

	a = dict(Counter(total_bills))

	return a


# print(make_change(90, 100))

# P-1.32
"""
Write a Python program that can simulate a simple calculator, using the
console as the exclusive input and output device. That is, each input to the
calculator, be it a number, like 12.34 or 1034, or an operator, like + or =,
can be done on a separate line. After each such input, you should output
to the Python console what would be displayed on your calculator.
"""
def calculator():
	expression = []
	a = ''
	while True:
		a = input().strip()
		if a == '=':
			break
		expression.append(a)
	return eval(''.join(expression))

# print(calculator())

# P-1.33
"""
Write a Python program that simulates a handheld calculator. Your pro-
gram should process input from the Python console representing buttons
that are “pushed,” and then output the contents of the screen after each op-
eration is performed. Minimally, your calculator should be able to process
the basic arithmetic operations and a reset/clear operation.
"""

def find_ops(expression, sym):
	idx = -1
	while True:
		idx = expression.find(sym, idx+1)
		if idx == -1:
			break
		else:
			expression = find_nums(expression, sym, idx)

	return expression


def get_answer(l,r,s):
	if l.find('.') == -1:
		l = int(l)
	else:
		l = float(l)
	if r.find('.') == -1:
		r = int(r)
	else:
		r = float(r)
	if s == '*':
		return l*r
	elif s == '+':
		return l+r
	elif s == '/':
		return l/r
	elif s == '-':
		return l - r
	else:
		print('no valid symbols found')



def find_nums(expr, sym, idx):
	lft_num= []
	rgt_num = []
	symbols = ['*', '+', '-', '/']
	num = ''
	bckwrd = idx -1
	frwrd = idx +1
	while True:
		if expr[bckwrd] not in symbols:
			lft_num.append(expr[bckwrd])
			if bckwrd == 0:
				break
			bckwrd -= 1
		else:
			break
	while True:
		if expr[frwrd] not in symbols:
			rgt_num.append(expr[frwrd])
			if frwrd == len(expr) - 1:
				break
			frwrd += 1
		else:
			break

	lft_num.reverse()
	lft_num = ''.join(lft_num)
	rgt_num = ''.join(rgt_num)
	answer = get_answer(lft_num, rgt_num, sym)

	if bckwrd == 0 and frwrd != len(expr)-1:
		expr = str(answer) + expr[frwrd:]
	elif bckwrd != 0 and frwrd == len(expr) - 1:
		expr = expr[:bckwrd+1] + str(answer)
	elif bckwrd != 0 and frwrd != len(expr) - 1:
		expr = expr[:bckwrd+1]+str(answer)+expr[frwrd:]
	else:
		expr = str(answer)
	# set_trace()
	return expr


def handheld_calculator():
	expression = []
	while True:
		a = input().strip()
		if a == '':
			break
		expression.append(a)

	expr = expression[0]
	primary_idx = []
	secondary_idx = []

	primary_ops = ['*', '/']
	secondary_ops = ['+', '-']
	for i in primary_ops:
		expr = find_ops(expr, i)
		# set_trace()
	for i in secondary_ops:
		expr = find_ops(expr, i)

	print(expr)


handheld_calculator()

# P-1.34
"""
A common punishment for school children is to write out a sentence mul-
tiple times. Write a Python stand-alone program that will write out the
following sentence one hundred times: “I will never spam my friends
again.” Your program should number each of the sentences and it should
make eight different random-looking typos.
"""


# P-1.35
"""
The birthday paradox says that the probability that two people in a room
will have the same birthday is more than half, provided n, the number of
people in the room, is more than 23. This property is not really a paradox,
but many people find it surprising. Design a Python program that can test
this paradox by a series of experiments on randomly generated birthdays,
which test this paradox for n = 5, 10, 15, 20, . . . , 100.
"""


# P-1.36
"""
Write a Python program that inputs a list of words, separated by white-
space, and outputs how many times each word appears in the list. You
need not worry about efficiency at this point, however, as this topic is
something that will be addressed later in this book.
"""