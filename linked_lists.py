class LinkedStack:
	"""LIFO Stack implementation using a singly linked list for storage"""

	class _Node:
		"""Lightweight, nonpublic class for storing a singly linked node"""
		__slots__ = "_element", "_next"

		def __init__(self, element, next):
			self._element = element
			self._next = next

	def __init__(self):
		self._head = None
		self._size = 0

	def __len__(self):
		return self._size

	def is_empty(self):
		return self._size == 0

	def push(self, e):
		"""Add element e to the top of the stack"""
		self._head = self._Node(e, self._head)
		self._size += 1

	def top(self):
		"""Return the element at top of stack. Raise Empty Exception if satck empty"""
		if self.is_empty():
			raise Empty('Stack is empty')
		return self._head._element

	def pop(self):
		"""Remove and return the element from teh top of the stack (i.e. LIFO)"""
		if self.is_empty():
			raise Empty('Stack is empty')
		elem = self._head._element
		self._head = self._head._next
		self._size -= 1
		return elem


class LinkedQueue:
	"""FIFO Queue implementation using a singly linked list for storage"""
	class _Node:
		def __init__(self, element, next):
			self._element = element
			self._next = next

	def __init__(self):
		self._head = None
		self._tail = None
		self._size = 0

	def __len__(slef):
		return self._size

	def is_empty(self):
		return self._size == 0

	def first(self):
		if self.is_empty():
			raise Empty('Queue is empty')
		return self._head._element

	def dequeue(self):
		if self.is_empty():
			raise Empty('Queue is empty')
		elem = self.first()
		self._size -=1
		self._head = self._head._next
		if self.is_empty():
			self._tail = None
		return elem

	def enqueue(self, e):
		newest = self._Node(e, None)
		if self.is_empty():
			self._head = newest
		else:
			self._tail._next = newest
		self._tail = newest
		self._size += 1




class CircularQueue:
	class _Node:
		def __init__(self, element, next):
			self._element = element
			self._next = next

	def __init__(self):
		self._tail = None
		self._size = 0

	def __len__(self):
		return self._size

	def is_empty(self):
		return self._size == 0

	def first(self):
		if self.is_empty():
			raise Empty('Queue is empty')
		head = self._tail._next
		return head._element

	def dequeue(self):
		if self.is_empty():
			raise Empty('Queue is empty')
		oldhead = self._tail._next
		if self._size == 1:
			self._tail = None
		else:
			self._tail._next = oldhead._next
		self._size -= 1
		return oldhead._element

	def rotate(self):
		if self._size > 0:
			self._tail = self._tail._next


class _DoublyLinkedBase:
	class _Node:
		__slots__ = '_element', '_prev', '_next'

		def __init__(self, element, prev, next):
			self._element = element
			self._prev = prev
			self._next = next

	def __init__(self):
		self._header = self._Node(None, None, None)
		self._trailer = self._Node(None, None, None)
		self._header._next = self._trailer
		self._trailer._prev = self._header
		self._size = 0

	def __len__(self):
		return self._size

	def is_empty(self):
		return self._size == 0

	def _insert_between(self, e, predecessor, successor):
		newest = self._Node(e, predecessor, successor)
		predecessor._next = newest
		successor._prev = newest
		self._size += 1
		return newest

	def _delete_node(self, node):
		predecessor = node._prev
		successor = node._next
		predecessor._next = successor
		successor._prev = predecessor
		self._size -=1
		element = node._element
		node._prev = node._next = node._element = None #deprecate the node
		return element


class LinkedDeque(_DoublyLinkedBase):

	def first(self):
		if self.is_empty():
			raise Empty('Dequeue is empty.')
		return self._header._next._element

	def last(self):
		if self.is_empty():
			raise Empty('Dequeue is empty')
		return self._trailer._prev._element

	def insert_first(self, e):
		self._insert_between(e, self._header, self._header._next)

	def insert_last(self, e):
		self._insert_between(e, self._trailer._prev, self._trailer)

	def delete_first(self):
		if self.is_empty():
			raise Empty('Dequeue is empty')
		return self._delete_node(self._header._next)

	def delete_last(self):
		if self.is_empty():
			raise Empty('Dequeue is empty')
		return self._delete_node(self._trailer._prev)


class PositionalList(_DoublyLinkedBase):
	"""A sequential container of elements allowing positional access"""
	class Position:
		def __init__(self, container, node):
			self._container = container
			self._node = node

		def element(self):
			return self._node._element

		def __eq__(self, other):
			return type(other) is type(self) and other._node is self._node

		def __ne__(self, other):
			return not (self == other)

	def _validate(self, p):
		if not isinstance(p, self.Position):
			raise TypeError('p must be a proper Position type')
		if p._container is not self:
			raise ValueError('p does not belong to this container')
		if p._node._next is None:
			raise ValueError('p is no longer valid')
		return p._node

	def _make_position(self, node):
		if node is self._header or node is self._trailer:
			return None
		else:
			return self.Position(self, node)

	def first(self):
		return self._make_position(self._header._next)

	def last(self):
		return self._make_position(self._trailer._prev)

	def before(self, p):
		node = self._validate(p)
		return self._make_position(node._prev)

	def after(self, p):
		node = self._validate(p)
		return self._make_position(node._next)

	def __iter__(self):
		cursor = self.first()
		while cursor is not None:
			yield cursor.element()
			cursor = self.after(cursor)

	def _insert_between(self, e, predecessor, successor):
		node = super()._insert_between(e, predecessor, successor)
		return self._make_position(node)

	def add_first(self, e):
		return self._insert_between(e, self._header, self._header._next)

	def add_last(self, e):
		return self._insert_between(e, self._trailer._prev, self._trailer)

	def add_before(self, p, e):
		original = self._validate(p)
		return self._insert_between(e,original._prev, original)

	def add_later(self, p, e):
		original = self._validate(p)
		return self._insert_between(e, original, original._next)

	def delete(self, p):
		original = self._validate(p)
		return self._delete_node(original)

	def replace(self, p, e):
		original = self._validate(p)
		old_value = original._element
		original._element = e
		return old_value

# L = PositionalList().

def insertion_sort(L):
	if len(L) > 1:
		marker = L.first()
		while marker != L.last():
			pivot = L.after(marker)
			value = pivot.element()
			if value > marker.element():
				marker = pivot
			else:
				walk = marker
				while walk != L.first() and L.before(walk).element() > value:
					walk = L.before(walk)
				L.delete(pivot)
				L.add_before(walk, value)		#reinsert value before walk


class FavoritesList:
	"""List of elements ordered from most frequently accessed to least"""
	class _Item:
		__slots__ = '_value', '_count'
		def __init__(self, e):
			self._value = e
			self._count = 0

	def _find_position(self, e):
		"""Search for element e and return its Position (or None if not found)"""
		walk = self._data.first()
		while walk is not None and walk.element()._value != e:
			walk = self._data.after(walk)
		return walk
	
	def _move_up(self, p):
		"""Move item at Position p earlier in the list based on access count."""
		if p != self._data.first():
			cnt = p.element()._count
			walk = self._data.before(p)
			if cnt > walk.element()._count:
				while (walk != self._data.first() and cnt > self._data.before(walk).element()._count):
					walk = self._data.before(walk)
				self._data.add_before(walk, self._data.delete(p))

	def __init__(self):
		self._data = PositionalList()

	def __len__(self):
		return len(self._data)

	def is_empty(self):
		return len(self._data == 0)

	def access(self, e):
		p = self._find_position(e)
		if p is None:
			p = self._data.add_last(self._Item(e))
		p.element()._count += 1
		self._move_up(p)

	def remove(self, e):
		p = self._find_position(e)
		if p is not None:
			self._data.delete(p)

	def top(self, k):
		if not 1<=k<= len(self):
			raise ValueError('Illegal value for k')
		walk = self._data.first()
		for j in range(k):
			item = walk.element()
			yield item._value
			walk = self._data.after(walk)

from pdb import set_trace

class FavoritesListMTF(FavoritesList):
	"""list of elements ordered with move-to-front heuristic"""

	def _move_up(self, p):
		if p != self._data.first():
			self._data.add_first(self._data.delete(p))

	def top(self, k):
		if not 1<=k<=len(self):
			raise ValueError('Illegal value for k')

		temp = PoisitionalList()
		for item in self._data:
			temp.add_last(item)

		for j in range(k):
			highPos = temp.first()
			walk = temp.after(highPos)
			while walk is not None:
				if walk.element()._count > highPos.element()._count:
					highPos = walk
				walk = temp.after(walk)
			yield highPos.element()._value
			temp.delete(highPos)


# L = PositionalList()
# char = 'e'

# R-7.1 Give an algorithm for finding the second-to-last node in a singly linked
# list in which the last node is indicated by a next reference of None.



# R-7.2 Describe a good algorithm for concatenating two singly linked lists L and
# M, given only references to the first node of each list, into a single list L 
# that contains all the nodes of L followed by all the nodes of M.
# R-7.3 Describe a recursive algorithm that counts the number of nodes in a singly
# linked list.

# S = LinkedStack()
# for i in range(5):
# 	S.push(i)

def count_nodes(S):
	if len(S) != 0:
		S.pop()
		return 1 + count_nodes(S)
	else:
		return 0
# print(count_nodes(S))


# R-7.5 Implement a function that counts the number of nodes in a circularly
# linked list.
class CircularLinkList:
	class _Node:
		def __init__(self, element, next):
			self._element = element
			self._next = next

	def __init__(self):
		# self._header = self._Node(None, None, None)
		self._tail= None
		# self._header._next = self._trailer

	def add_element(self, e):
		newest = self._Node(e, None)
		if self._tail == None:
			newest._next = newest
			# set_trace()
		else:
			newest._next = self._tail._next
			self._tail._next = newest
			# set_trace()
		# set_trace()
		self._tail = newest

	def first(self):
		head = self._tail._next
		return head._element

	def rotate(self):
		# set_trace()
		self._tail = self._tail._next

# L = CircularLinkList()
# L.add_element(3)
# L.add_element(5)
# print(L.first())
# L.rotate()
# print(L.first())
# L.rotate()
# print(L.first())
# L.rotate()
# print(L.first())

# def count(L, stack):
# 	set_trace()
# 	if L.first() in stack:
# 		return 0
# 	else:
# 		stack.add(L.first())
# 		L.rotate()
# 		return 1 + count(L, stack)

# print(count(L, set()))


# R-7.9 Give a fast algorithm for concatenating two doubly linked lists L and M,
# with header and trailer sentinel nodes, into a single list L' .
class SimpleDoublyLinkedList(_DoublyLinkedBase):
	def __init__(self):
		super().__init__()

	def add_element(self, e):
		self._insert_between(e, self._trailer._prev, self._trailer)

	def first(self):
		return self._header._next._element

	def last(self):
		return self._trailer._prev._element

	def delete_first(self):
		return self._delete_node(self._header._next)


# L = SimpleDoublyLinkedList()
# M = SimpleDoublyLinkedList()

# for i in range(5):
# 	L.add_element(i)

# for i in range(5, 10):
# 	M.add_element(i)

# print(L.first())
# print(M.last())

def cat_and_reduce(L, M):
	"""
	inputs: L, M both SimpleDoublyLinkedList types
	output: concatenation of L and M as a single list
	"""
	while len(M) != 0:
		L.add_element(M.delete_first())

	return L

# print(len(cat_and_reduce(L, M)), cat_and_reduce(L, M).first(), cat_and_reduce(L, M).last())


# R-7.19 Suppose that we have made k*n total accesses to the elements in a list L of
# n elements, for some integer k ≥ 1. What are the minimum and maximum
# number of elements that have been accessed fewer than k times?

# min is 0 (one node gets accessed k*n times, hence no other node gets accessed less than k times), 
# max is n-1 (second highest number to k is k - 1; if n-1 nodes get accessed k-1 times, and
# and 1 node gets accessed n+k-1 times)


# 7.42, C-7.42 Write a Scoreboard class that maintains the top 10 scores for a game ap-
#plication using a singly linked list, rather than the array that was used in
#Section 5.5.1.
class GameEntry:
	"""Represents one entry of a list of high scores"""
	def __init__(self, name, score):
		self._name = name
		self._score = score

	def get_name(self):
		return self._name

	def get_score(self):
		return self._score

	def __str__(self):
		return f'({self._name}, {self._score})'

class ScoreBoard:
	"""Fixed-length sequence of high scores in nondecreasing order"""
	def __init__(self, capacity=10):
		self._board = [None]*capacity
		self._n = 0

	def __getitem__(self, k):
		return self._board[k]

	def __str__(self):
		return '\n'.join(str(self._board[j]) for j in range(self._n))

	def add(self, entry):
		score = entry.get_score()
		good = self._n < len(self._board) or score > self._board[-1].get_score()

		if good:
			if self._n < len(self._board):
				self._n += 1

			j = self._n - 1
			while j > 0 and self._board[j-1].get_score() < score:
				self._board[j] = self._board[j-1]
				j-=1
			self._board[j] = entry


class newScoreBoard(LinkedStack):
	def __init__(self):
		super().__init__()
		self._min = GameEntry('', float("-inf"))

	def add_entry(self, val):
		last_visited = []
		score = val.get_score()

		if self._size == 0:
			self._head = self._Node(val, self._head)
			self._size += 1
		elif self._size < 10:
			self._size += 1
			temp_head = self._head
			while True:
				if temp_head._element.get_score() > score:
					last_visited.append(temp_head)
					if temp_head._next:
						temp_head = temp_head._next
					else:
						temp_head._next = self._Node(val, temp_head)
						break
				elif len(last_visited) != 0:
					left_node = last_visited.pop()
					left_node._next = self._Node(val, temp_head)
					break
				else:
					self._head = self._Node(val, temp_head)
					break

		elif self._size == 10:
			temp_head = self._head
			while True:
				if score < self._min.get_score():
					break
				elif temp_head._element.get_score() >= score:
					last_visited.append(temp_head)
					if temp_head._next:
						temp_head = temp_head._next
					else:
						break
				else:
					left_node = last_visited.pop()
					new_node = self._Node(val, temp_head)
					left_node._next =  new_node
					new_node._next = temp_head
					break
		self._min = val


game_entries = []


for char in 'elizabthklshn':
	game_entries.append(GameEntry(char, ord(char)))

# for i in game_entries:
# 	print(i.get_score())
# 	print(i.get_name())


# score_board = newScoreBoard()

# for i in game_entries:
# 	score_board.add_entry(i)

# # set_trace()
# i = 0
# while i < len(score_board):
# 	print(score_board._head._element.get_score())
# 	score_board._head = score_board._head._next
# 	i += 1

# for i in game_entries:
# 	print(i.get_score())


# P.45 An array A is sparse if most of its entries are empty (i.e., None). A list
# L can be used to implement such an array efficiently. In particular, for
# each nonempty cell A[i], we can store an entry (i, e) in L, where e is the
# element stored at A[i]. This approach allows us to represent A using O(m)
# storage, where m is the number of nonempty entries in A. Provide such
# a SparseArray class that minimally supports methods getitem (j) and
# setitem (j, e) to provide standard indexing operations. Analyze the
# efficiency of these methods.
class SparseArray:
	def __init__(self, A):
		self._orig = A
		self._storage = {}
		for idx, elem in enumerate(A):
			if elem != None:
				self._storage[idx] = elem

	def __len__(self):
		return len(self._storage)

	def __getitem__(j):
		return self._storage[j]

	def __setitem__(j, e):
		self._storage[j] = e


# sparse = [None]*1000 + [1] + [None]*1000 + [2]

# new_sparse = SparseArray(sparse)

# print(len(new_sparse))

# set_trace()

# P-7.47 Implement a CardHand class that supports a person arranging a group of
# cards in his or her hand. The simulator should represent the sequence of
# cards using a single positional list ADT so that cards of the same suit are
# kept together. Implement this strategy by means of four “fingers” into the
# hand, one for each of the suits of hearts, clubs, spades, and diamonds,
# so that adding a new card to the person’s hand or playing a correct card
# from the hand can be done in constant time. The class should support the
# following methods:
# • add_card(r, s): Add a new card with rank r and suit s to the hand.
# • play(s): Remove and return a card of suit s from the player’s hand;
# if there is no card of suit s, then remove and return an arbitrary card
# from the hand.
# •__iter__( ): Iterate through all cards currently in the hand.
# • all_of_suit(s): Iterate through all cards of suit s that are currently in
# the hand.
# suits = ['X', 'H', 'D', 'C']
# cards = []
# for s in suits:
# 	for i in range(1, 14):
# 		cards.append(s+ str(i))

# import random

# random.shuffle(cards)

# print(cards)


# class CardHand:
# 	DECK_OF_CARDS = cards
# 	def __init__(self):
# 		for i in range(4):

# # x = CardHand()

# Pos = PositionalList()

# print(Pos.add_first('a'))
# set_trace()

class CardHand(PositionalList):
	def __init__(self):
		super().__init__()
		self._heart = self._Node(None, None, None)
		self._club = self._Node(None, None, None)
		self._spade = self._Node(None, None, None)
		self._diamond = self._Node(None, None, None)
		self._header._next = self._heart
		self._heart._next = self._spade
		self._spade._prev= self._heart
		self._spade._next = self._diamond
		self._diamond._prev = self._spade
		self._diamond._next = self._trailer
		self._trailer._prev = self._diamond
		self._heart_size = 0
		self._club_size = 0
		self._spade_size = 0
		self._diamond_size = 0

	def all_of_suit(self, s):
		if (s == 'heart') and (self._heart_size >0):
			cursor = self._heart._next
			while cursor._element is not None:
				yield cursor._element
				cursor = cursor._next
		if (s == 'club') and (self._club_size >0):
			cursor = self._club._next
			while cursor._element is not None:
				yield cursor._element
				cursor = cursor._next
		if (s == 'spade') and (self._spade_size >0):
			cursor = self._spade._next
			while cursor._element is not None:
				yield cursor._element
				cursor = cursor._next
		if (s == 'diamond') and (self._diamond >0):
			cursor = self._diamond._next
			while cursor._element is not None:
				yield cursor._element
				cursor = cursor._next
	
	def add_card(self, r, s):
		if s=='heart':
			p=self._heart._next
			while (p != None) and (p._element!=None) and (r>p._element):
				p = p._next
			self._insert_between(r, p._prev, p)
			self._heart_size +=1
		elif s=='club':
			p=self._club._next
			while (p != None) and (p._element!=None) and (r>p._element):
				p = p._next
			self._insert_between(r, p._prev, p)
			self._club_size +=1
		elif s=='spade':
			p=self._spade._next
			while (p != None) and (p._element!=None) and (r>p._element):
				p = p._next
			self._insert_between(r, p._prev, p)
			self._spade_size +=1
		elif s=='diamond':
			p=self._diamond._next
			while (p != None) and (p._element!=None) and (r>p._element):
				p = p._next
			self._insert_between(r, p._prev, p)
			self._diamond_size +=1
	
	def autoplay(self):
		if self.is_empty():
			return 0
		elif self._heart_size:
			self._heart_size -=1
			return self._delete_node(self._heart._next)
		elif self._club_size:
			self._club_size -=1
			return self._delete_node(self._club._next)
		elif self._spade_size:
			self._spade_size -=1
			return self._delete_node(self._spade._next)
		elif self._diamond_size:
			self._diamond_size -=1
			return self._delete_node(self._diamond._next)


	def play(self, s):
		if self.is_empty():
			return 0
		elif s == 'heart':
			if self._heart_size ==0:
				return self._autoplay()
			else:
				self._heart_size -=1
				return self._delete_node(self._heart._next)
		elif s == 'club':
			if self._club_size ==0:
				return self._autoplay()
			else:
				self._club_size -=1
				return self._delete_node(self._club._next)
		elif s == 'spade':
			if self._spade_size ==0:
				return self._autoplay()
			else:
				self._heart_size -=1
				return self._delete_node(self._spade._next)
		elif s == 'diamond':
			if self._diamond_size ==0:
				return self._autoplay()
			else:
				self._dimaond_size -=1
				return self._delete_node(self._diamond._next)

L = CardHand()
