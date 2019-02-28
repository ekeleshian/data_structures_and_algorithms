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

# def sum(values):
# 	if not isinstance(values, (list, tuple, str)):
# 		raise TypeError('parameter must be an interable type')
# 	total = 0
# 	for v in values:
# 		if not isinstance(v, (int, float)):
# 			raise TypeError('elements must be numeric')
# 		total = total+v

# 	return total

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

# def factors(n):
# 	for k in range(1, n+1):
# 		if n%k == 0:
# 			yield k

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
print(sum(i*i for i in range(1, 4, 2)))