#simple array-based stack implementation
#to implement a stack using a python list, we use the adapter design pattern
#stacks main methods with python equivalence in parenthesis: S.push(e) (L.append(e))and S.pop() (L.pop()),
#we will also add S.top() (L[-1]), S.is_empty() (len(L) == 0), and len(S) (len(L)) for convenience.

class Empty(Exception):
	"""Error attemting to access an element from an empty container"""
	pass
class Full(Empty):
	pass

class ArrayStack:
	"""LIFO stack implementation using apython list as underlying storage"""
	def __init__(self, maxlen=None):
		if maxlen:
			self._data = [None]*maxlen
		else:
			self._data = []
		self._maxlen = 10

	def __len__(self):
		return len(self._data)

	def is_empty(self):
		return len(self._data) == 0

	def push(self, e):
		if len(self._data) >= self._maxlen:
			raise Full('Stack is full')
		self._data.append(e)

	def top(self):
		if self.is_empty():
			raise Empty('Stack is empty')
		return self._data[-1]

	def pop(self):
		if self.is_empty():
			raise Empty('Stack is empty')
		return self._data.pop()

from pdb import set_trace

def is_matched_html(raw):
	"""Return True if all HTML tags are properly matched; False otherwise"""
	stack = ArrayStack()
	fst = raw.find('<')
	while fst != -1:
		sec = raw.find('>', fst+1)
		if sec == -1:
			return False
		tag_idx = raw.find(' ', fst+1)
		tag = raw[fst+1:tag_idx]
		# set_trace()
		if not tag.startswith('/'):
			stack.push(tag)
			# set_trace()
		else:
			if stack.is_empty():
				return False
			if tag[1:] != stack.pop():
				# set_trace()
				return False
		fst = raw.find('<', sec+1)
		# set_trace()
	return stack.is_empty()



# print(is_matched_html('<head attribute=value1 attribute=value2>blahblahblah</head>'))

class ArrayQueue:
	"""FIFO queue implementation using a python list (w/ circular array design) as underlying storage"""
	DEFAULT_CAPACITY = 10

	def __init__(self):
		"""Create an empty qqueue"""
		self._data = [None] * ArrayQueue.DEFAULT_CAPACITY
		self._size = 0
		self._front = 0

	def __len__(self):
		return self._size

	def is_empty(self):
		return self._size == 0

	def first(self):
		"""Return but don't remove the element at front of q."""
		if self.is_empty():
			raise Empty('Queue is empty')
		return self._data[self._front]

	def dequeue(self):
		"""Remove and reutrn the first element of the queue
		Raise Empty exception if the q is empty"""
		if self.is_empty():
			raise Empty('Queue is empty')
		element = self.first()
		# set_trace()
		self._data[self._front] = None
		self._front = (self._front+1)%len(self._data)
		self._size -= 1
		return element
		# set_trace()

	def enqueue(self, e):
		"""Add an element to the back of q"""
		if self._size == len(self._data):
			self._resize(2*len(self._data))
		# set_trace()
		back_idx = (self._front+self._size)%len(self._data)
		self._data[back_idx] = e
		self._size += 1
		# set_trace()


	def _resize(self, cap):
		"""Resize to a new list of capacity >= len(self)"""
		old = self._data
		self._data = [None]*cap
		walk = self._front
		# set_trace()
		for k in range(self._size):
			self._data[k] = old[walk]
			walk = (1+walk)%len(old)
			# set_trace()
		# set_trace()
		self._front = 0


# queue = ArrayQueue()

# for i in range(20):
# 	queue.enqueue(i)

# for i in range(5):
# 	queue.dequeue()

# for i in range(100,112):
# 	queue.enqueue(i)

# R-6.3 Implement a function with signature transfer(S, T) that transfers all ele-
# ments from stack S onto stack T, so that the element that starts at the top
# of S is the first to be inserted onto T, and the element at the bottom of S
# ends up at the top of T.
def transfer(stack_s, stack_t):
	for k in range(len(stack_s)):
		stack_t.push(stack_s.pop())
	return stack_t

stack_s = ArrayStack()
for k in range(3):
	stack_s.push(k)

stack_t = ArrayStack()

for m in range(6,10):
	stack_t.push(m)


# print(transfer(stack_s,stack_t).top())

# R-6.4 Give a recursive method for removing all the elements from a stack.
def remove_all(stack):
	def helper(stack,stack_size):
		if len(stack) == 0:
			return stack
		stack.pop()
		if stack is None:
			stack = ArrayStack()
			return stack
		return helper(stack, len(stack))
	stack = helper(stack,len(stack))
	return stack
# print(len(stack_s))
# print(len(remove_all(stack_s)))

# R-6.5 Implement a function that reverses a list of elements by pushing them onto
# a stack in one order, and writing them back to the list in reversed order.
def reverse_elem(array):
	stack = ArrayStack()
	for i in range(len(array)):
		stack.push(array[i])
	for i in range(len(array)):
		array[i] = stack.pop()
	return array

# arr = [i for i in range(10)]
# print(reverse_elem(arr))

# R-6.13 Suppose you have a deque D containing the numbers (1, 2, 3, 4, 5, 6, 7, 8),
# in this order. Suppose further that you have an initially empty queue Q.
# Give a code fragment that uses only D and Q (and no other variables) and
# results in D storing the elements in the order (1, 2, 3, 5, 4, 6, 7, 8).
from collections import deque
# D = deque([i for i in range(1,9)])
# Q = ArrayQueue()
# for i in range(len(D)):
# 	print(D[i])
# n = len(D)
# for i in range(n):
# 	Q.enqueue(D.popleft())
# set_trace()

# for i in range(n):
# 	D.append(Q.dequeue())
# for i in range(n):
# 	print(D[i])

# C-6.15 Suppose Alice has picked three distinct integers and placed them into a
# stack S in random order. Write a short, straight-line piece of pseudo-code
# (with no loops or recursion) that uses only one comparison and only one
# variable x, yet that results in variable x storing the largest of Alice’s three
# integers with probability 2/3. Argue why your method is correct.

#if stack[0]>stack[1]:
#	return stack[2]
#else:
#	return stack[2]
#My method depicts the monty hall problem.  Stack [0] has a 1/3 chance of 
#being correct.  After knowing that stack[1] is less, there is still a 
#1/3 chance that stack[0] is the largest, but now there are 2 chances of 3 that 
# the third number is the largest.  #the initial choice (which is determined
#in the  comparison) has only one chance in three being of being the largest, 
#while the third remaining number as two chances in three.

# C-6.16 Modify the ArrayStack implementation so that the stack’s capacity is lim-
# ited to maxlen elements, where maxlen is an optional parameter to the
# constructor (that defaults to None). If push is called when the stack is at
# full capacity, throw a Full exception (defined similarly to Empty).

#See lines 9-39

# C-6.17 In the previous exercise, we assume that the underlying list is initially
# empty. Redo that exercise, this time preallocating an underlying list with
# length equal to the stack’s maximum capacity.

#see lines 9-39

# C-6.19 In Code Fragment 6.5 we assume that opening tags in HTML have form
# <name>, as with <li>. More generally, HTML allows optional attributes
# to be expressed as part of an opening tag. The general form used is
# <name attribute1="value1" attribute2="value2">; for example,
# a table can be given a border and additional padding by using an opening
# tag of <table border="3" cellpadding="5">. Modify Code Frag-
# ment 6.5 so that it can properly match tags, even when an opening tag
# may include one or more such attributes.

#see lines 44-66

# C-6.20 Describe a nonrecursive algorithm for enumerating all permutations of the
# numbers {1, 2, . . . , n} using an explicit stack.
# stack = ArrayStack()

# orig_nums = 5
# for i in range(orig_nums):
# 	stack.push(i)
# permutations = []
# cursor = 0
# while cursor < orig_nums:
# 	num = stack.pop()
# 	result = [i for i in range(orig_nums)]
# 	for i in range(orig_nums):
# 		old = result[i]
# 		result[i] = num
# 		result[num] = old
# 		permutations.append(result)
# 		result = [idx for idx in range(orig_nums)]

# 	cursor += 1

# print(permutations)

# C-6.21 Show how to use a stack S and a queue Q to generate all possible subsets
# of an n-element set T nonrecursively.
stack = ArrayStack()
queue = ArrayQueue()
# queue.enqueue(set())
T = [1,2,3, 4, 5]
# for i in T:
# 	stack.push(i)
	# queue.enqueue(i)

# while stack.is_empty()==False:
# 	cur = stack.pop()
# 	set_trace()
# 	for i in range(len(queue)):
# 		a = queue.dequeue()
# 		b = a | {cur}
# 		queue.enqueue(a)
# 		queue.enqueue(b)
# 		set_trace()

# while queue.is_empty()==False:
# 	x = queue.dequeue()
# 	print(x)
# C-6.22 Postfix notation is an unambiguous way of writing an arithmetic expres-
# sion without parentheses. It is defined so that if “(exp 1 ) op (exp 2 )” is a
# normal, fully parenthesized expression whose operation is op, the postfix
# version of this is “pexp 1 pexp 2 op”, where pexp 1 is the postfix version of
# exp 1 and pexp 2 is the postfix version of exp 2 . The postfix version of a sin-
# gle number or variable is just that number or variable. For example, the
# postfix version of “((5 + 2) ∗ (8 − 3))/4” is “5 2 + 8 3 − ∗ 4 /”. Describe
# a nonrecursive way of evaluating an expression in postfix notation.


expr = "5 2 + 8 3 - * 4 / "
step = 0
idx = expr.find(' ', step)
while idx != -1:
	char = expr[:idx]
	expr = expr[idx+1:].strip()
	queue.enqueue(char)
	idx = expr.find(' ',0)
if len(expr) != 0:
	queue.enqueue(expr[0])



expr = ''
while queue.is_empty() == False:
	elem = queue.dequeue()
	if elem not in {'+', '-', '*', '/'}:
		expr += elem + ' '
	elif len(stack) < 2:
		numbers = expr.strip().split(' ')
		if len(numbers) < 2:
			answer = str(eval(stack.pop() + elem + numbers[0]))
			stack.push(answer)
		else:
			answer = str(eval(numbers[0]+elem+numbers[1]))
			stack.push(answer)
			expr = ''
	else:
		numbers = []
		for i in range(2):
			numbers.append(stack.pop())
		answer = str(eval(numbers[0]+elem+numbers[1]))
		stack.push(answer)
	# set_trace()

# print(stack.pop())

# P-6.32 Give a complete ArrayDeque implementation of the double-ended queue
# ADT as sketched in Section 6.3.2.
# P-6.33 Give an array-based implementation of a double-ended queue supporting
# all of the public behaviors shown in Table 6.4 for the collections.deque
# class, including use of the maxlen optional parameter. When a length-
# limited deque is full, provide semantics similar to the collections.deque
# class, whereby a call to insert an element on one end of a deque causes an
# element to be lost from the opposite side.


class ArrayDeque(ArrayQueue):
	def __init__(self):
		super().__init__()

	def add_first(self, e):
		"""call may need to wrap around beginning of array
		self._front = (self._front - 1)%len(self._data)
		"""
		if self._size == self.DEFAULT_CAPACITY:
			self.delete_last()
		# set_trace()
		self._front = (self._front - 1)%len(self._data)
		self._data[self._front] = e 
		self._size += 1
		

	def add_last(self, e):
		"""will be like enqueue"""
		if self._size == self.DEFAULT_CAPACITY:
			self.delete_first()

		back_idx = (self._front+self._size)%len(self._data)
		self._data[back_idx] = e
		self._size += 1

	def delete_first(self):
		"""Just like dequeue"""
		return self.dequeue()

	def delete_last(self):
		"""similar to dequeue but at end of queue"""
		if self.is_empty():
			raise Empty('Queue is empty')
		element = self.last()
		self._data[(self._front + self._size)%len(self._data)] = None
		self._size -= 1
		return element

	def last(self):
		return self._data[(self._front + self._size - 1)%len(self._data)]


D = ArrayDeque()

for i in range(10):
	D.add_last(i)

for i in range(11,15):
	D.add_first(i)

print(len(D))
print(D.first())
print(D.last())
# # set_trace()

# D.delete_last()
# for i in range(2):
# 	D.delete_first()

# print(len(D))
# print(D.first())
# print(D.last())