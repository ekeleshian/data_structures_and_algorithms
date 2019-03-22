#Exploring list, tuple and str classes
import sys
# data =[]
# for k in range(30):
# 	a = len(data)
# 	b = sys.getsizeof(data)
# 	print(f"length: {a}, size in bytes: {b}")
# 	data.append(None)

import ctypes

class DynamicArray:
	"""A dynamic array class akin to a simplifed python list"""
	def __init__(self):
		"""Create an empty array"""
		self._n = 0
		self._capacity = 1
		self._A = self._make_array(self._capacity)


	def __len__(self):
		return self._n


	def __getitem__(self, k):
		if k < 0:
			k = self._n + k
		if not 0<=k<self._n:
			raise IndexError('invalid index')
		return self._A[k]

	def append(self, obj):
		if self._n == self._capacity:
			self._resize(2*self._capacity)
		self._A[self._n]= obj
		self._n+=1

	def _resize(self, c):
		B = self._make_array(c)
		for k in range(self._n):
			B[k] = self._A[k]
		self._A=B
		self._capacity = c

	def insert(self,k,value):
		if self._n == self._capacity:
			self._resize(2*self._capacity)
		for j in range(self._n, k, -1):
			self._A[j] = self._A[j-1]
		self._A[k] = value
		self._n += 1

	def remove(self, value):
		for k in range(self._n):
			if self._A[k] == value:
				for j in range(k, self._n-1):
					self._A[j] = self._A[j+1]
				self._A[self._n-1] = None
				self._n -=1
				return
		raise ValueError('value not found')



	def _make_array(self, c):
		return (c*ctypes.py_object)()


# da = DynamicArray()
# da.append(10)
# da.append('a')
# print(da[0])
# print(da[1])
# print(da[-1])
# print(len(da))

#Amortized Analysis of dynamic arrays
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

def insertion_sort(A):
	"""sort list of comparable elements into nondecreasing order"""

	for k in range(1, len(A)):
		cur = A[k]
		j = k
		while j > 0 and A[j-1] > cur:
			A[j] = A[j-1]
			j-=1
		A[j]=cur

class CaesarCipher:
	"""Class for doing encryption and decryption using a Caesar cipher"""
	def __init__(self, shift):
		encoder = [None]*26
		decoder = [None]*26
		for k in range(26):
			encoder[k] = chr((k+shift)%26+ord('A'))
			decoder[k] = chr((k-shift)%26 + ord('A'))
		self._forward = ''.join(encoder)
		self._backward = ''.join(decoder)

	def encrypt(self,message):
		"""Return string representing encrypted message"""
		return self._transform(message, self._forward)

	def decrypt(self, secret):
		"""Return decrypted message given encrypted secret"""
		return self._transform(secret, self._backward)

	def _transform(self, original, code):
		"""Utility to perform transformation based on given code string"""
		msg = list(original)
		for k in range(len(msg)):
			if msg[k].isupper():
				j = ord(msg[k]) - ord('A')
				msg[k] = code[j]
		return ''.join(msg)

# if __name__ == '__main__':
# 	cipher = CaesarCipher(3)
# 	message = "THE BUTTON HAS ENGAGED."
# 	coded = cipher.encrypt(message)
# 	print('Secret: ', coded)
# 	answer = cipher.decrypt(coded)
# 	print('Message: ', answer)

class TicTacToe:
	"""Management of a Tictactoe game(no strategy)"""
	def __init__(self):
		self._board = [['']*3 for j in range(3)]
		self._player = "X"

	def mark(self, i, j):
		if not (0<=i<=2 and 0<=j<=2):
			raise ValueError('Invalid board position')
		if self._board[i][j] != '':
			raise ValueError('Board position occupied')
		if self.winner() is not None:
			raise ValueError('Game is already copmlete')
		self._board[i][j] = self._player
		if self._player == 'X':
			self._player = "O"
		else:
			self._player = "X"

	def _is_win(self, mark):
		"""Check whether the board config is a win for the given player"""
		board = self._board
		return (mark == board[0][0] == board[0][1] == board[0][2] or
				mark == board[1][0] == board[1][1] == board[1][2] or
				mark == board[2][0] == board[2][1] == board[2][2] or
				mark == board[0][0] == board[1][0] == board[2][0] or
				mark == board[0][1] == board[1][1] == board[2][1] or
				mark == board[0][2] == board[1][2] == board[2][2] or
				mark == board[0][0] == board[1][1] == board[2][2] or
				mark == board[0][2] == board[1][1] == board[2][0])

	def winner(self):
		for mark in "XO":
			if self._is_win(mark):
				return mark
		return None

	def __str__(self):
		rows = ["|".join(self._board[r]) for r in range(3)]
		return '\n-----\n'.join(rows)


# game = TicTacToe()
# game.mark(1,1)
# game.mark(2,2)
# game.mark(0,2)
# game.mark(1,0)
# game.mark(2,1)
# game.mark(0,0)
# game.mark(0,1)

# print(game)
# winner = game.winner()
# print(winner)
# In Code Fragment 5.1, we perform an experiment to compare the length of
# a Python list to its underlying memory usage. Determining the sequence
# of array sizes requires a manual inspection of the output of that program.
# Redesign the experiment so that the program outputs only those values of
# k at which the existing capacity is exhausted. For example, on a system
# consistent with the results of Code Fragment 5.2, your program should
# output that the sequence of array capacities are 0, 4, 8, 16, 25, . . . .

# data =[]
# bts = []
# for k in range(30):
# 	b = sys.getsizeof(data)
# 	bts.append(b)
# 	if k > 0 and bts[k-1] < bts[k]:
# 		print(k-1)
# 	data.append(None)


# Modify the experiment from Code Fragment 5.1 in order to demonstrate
# that Python’s list class occasionally shrinks the size of its underlying array
# # when elements are popped from a list.
# data =[]
# for k in range(30):
# 	a = len(data)
# 	b = sys.getsizeof(data)
# 	if k > 8 and k%8 == 2:
# 		data.pop()
# 		data.pop()
# 		data.pop()
# 		data.pop()
# 	print(f"length: {a}, size in bytes: {b}")
# 	data.append(None)


# The syntax data.remove(value) for Python list data removes only the first
# occurrence of element value from the list. Give an implementation of a
# function, with signature remove all(data, value), that removes all occur-
# rences of value from the given list, such that the worst-case running time
# of the function is O(n) on a list with n elements. Not that it is not efficient
# enough in general to rely on repeated calls to remove.
from pdb import set_trace

def remove_all(data, value):
	result = []
	k = 0
	for i in range(len(data)):
		if data[i] == value:
			result += data[k:i]
			k = i + 1
	result += data[k:]
	return result

# print(remove_all([1,2,3,4,12,3,3,1], 3))

# P-5.32 Write a Python function that takes two three-dimensional numeric data
# sets and adds them componentwise.
def add_3d(m_1, m_2):
	depth = len(m_1)
	rows = len(m_1[0])
	cols = len(m_1[0][0])
	if depth != len(m_2) or rows != len(m_2[0]) or cols != len(m_2[0][0]):
		raise ValueError('lists must have same number of columns, rows, and depths')

	for d in range(depth):
			for r in range(rows):
				for c in range(cols):
					m_1[d][r][c] += m_2[d][r][c]

	return m_1


# P-5.33 Write a Python program for a matrix class that can add and multiply two-
# dimensional arrays of numbers, assuming the dimensions agree appropri-
# ately for the operation.
import copy 
class Matrix:
	def __init__(self, n, m):
		self.n_rows = n
		self.n_cols = m
		self.matrix = [[0]*m for r in range(n)]

	def __add__(self, m):
		if not isinstance(m,Matrix):
			raise TypeError('can only add with other matrix instances')
		add = copy.deepcopy(self.matrix)
		result.
		for r in range(self.n_rows):
			for c in range(self.n_cols):
				add[r][c] += m.matrix[r][c]
		self.matrix = add

	def partial_mul(self, r, m):
		result = [0]*m.n_cols
		for i, elem in enumerate(r):
			for c in range(m.n_cols):
				result[c] += elem*m.matrix[i][c]
		return result




	def __mul__(self, m):
		if not isinstance(m, (Matrix, int, float)):
			raise TypeError('can only multiply with other matrices or scalars which are either int or float type')
		if isinstance(m,Matrix):
			if self.n_cols != m.n_rows:
				raise ValueError('n_cols of left matrix != n_rows of right matrix, invalid configuration')
			result = Matrix(self.n_rows, m.n_cols)
			# for r in range(self.n_rows):
			# 	for c in range(m.n_cols):
			# 		result.matrix[r][c] += self.matrix[c][]*m.matrix[idx][c]
			for idx, r in enumerate(self.matrix):
				partial_prods = self.partial_mul(r, m)
				result.matrix[idx] = partial_prods
			return result
		for r in range(self.n_rows):
			for c in range(self.n_cols):
				self.matrix[r][c] *= m


m = Matrix(2, 2)
m.matrix[0][0] = 1
m.matrix[0][1] = 2
m.matrix[1][0] = 3
m.matrix[1][1] = 4

n = Matrix(2, 3)
n.matrix[0][0] = 1
n.matrix[0][1] = 2
n.matrix[0][2] = 3
n.matrix[1][0] = 4
n.matrix[1][1] = 5
n.matrix[1][2] = 6

print((m*n).matrix)
print((m+n).matrix)
print((m*2).matrix)
# P-5.34 Write a program that can perform the Caesar cipher for English messages
# that include both upper- and lowercase characters.
# P-5.35 Implement a class, SubstitutionCipher, with a constructor that takes a
# string with the 26 uppercase letters in an arbitrary order and uses that for
# the forward mapping for encryption (akin to the self. forward string in
# our CaesarCipher class of Code Fragment 5.11). You should derive the
# backward mapping from the forward version.
# P-5.36 Redesign the CaesarCipher class as a subclass of the SubstitutionCipher
# from the previous problem.
# P-5.37 Design a RandomCipher class as a subclass of the SubstitutionCipher
# from Exercise P-5.35, so that each instance of the class relies on a random
# permutation of letters for its mapping.


