def factorial(n):
	if n == 0: #when you bottom out
		return 1
	else:
		return n*factorial(n-1)

#Each function call generates an activation record that gets suspended each time another function call gets invoked. 
#Recursive functions follow this pattern: wind the stack, and then bottom out once it reaches the base case, and then 
#unwind the stack until it reaches the top of the stack.

#recursive approach to ruler drawing: For each inch, place tick with numeric label. denote length of tick designating
#whole inch as major tick length.  B/w marks for whole inches, ruler contains series of minor ticks, at 1/2, 1/4 inch
#intervals, etc. As interval decreases by 1/2, tick length decreases by one.

#This pattern is an exmaple of a fractal.

def draw_line(tick_length, tick_label=''):
	"""Draw one line with given tick length (followed by optional label)"""
	line = '-'*tick_length
	if tick_label:
		line+= ' ' + tick_label
	print(line)

def draw_interval(center_length):
	"""Draw tick interval based upon a central tick length"""
	if center_length > 0:
		draw_interval(center_length-1)
		draw_line(center_length)
		draw_interval(center_length-1)


def draw_ruler(num_inches, major_length):
	"""Draw english ruler with given number of inches, major tick length"""
	draw_line(major_length, '0')
	for j in range(1, 1 + num_inches):
		draw_interval(major_length - 1)
		draw_line(major_length, str(j))


# draw_ruler(12, 5)

###############################333

#Binary Search
#data should be sorted
def binary_search(data, target, low, high):
	"""Return True if target is found in indicated portion of a Python list.
	
	The search only considers the porition from data[low] to data[high] inclusive.

	"""

	if low > high:
		return False			#interval is empty; no match
	else:
		mid = (low+high)//2
		if target == data[mid]:
			return True
		elif target < data[mid]:
			return binary_search(data, target, low, mid-1)
		elif target > data[mid]:
			return binary_search(data, target, mid+1, high)
#runs O(log(n)) time as opposed to sequential search O(n) time

# print(binary_search([1,2,3,12,1,34,4],3, 5, 7))

#################################################3

import os

def disk_usage(path):
	"""Return the number of bytes used by a file/folder and any descendants"""
	total = os.path.getsize(path)
	if os.path.isdir(path):
		for filename in os.listdir(path):
			childpath = os.path.join(path, filename)
			total += disk_usage(childpath)
	print(f'{total} {path}')
	return total
#there are O(n) recursive calls, each of which runs in O(n) time leading to overall
#O(n^2). But actually its O(n) because the overall are overall O(n) recursive calls
#each of which uses O(1) time outside the loop and that the overall number of operations due to the loop 
# is O(n). Summing everything, the overall number of operations is O(n).  This technique
#of achieving a tighter bound on the series of operations by considering a cumalative effect is called
#amoritization
# print(disk_usage('/home/mathlizard/smartFont'))

#recognizing and avoiding pitfalls when applying recusion
#element uniqueness problem
def unique3(S, start, stop):
	#base case, elemnts are trivially unique
	if stop - start <= 1: return True #at most one item
	elif not unique3(S, start, stop-1): return False
	elif not unique3(S, start+1, stop): return False
	else: return S[start] != S[stop-1]
#terrible use of recursion, running time is O(2^n)

def bad_fibonacci(n):
	if n<=1:
		return n
	else:
		return bad_fibonacci(n-2) + bad_fibonacci(n-1)
		#after computing F_n-2, the call to compute F_n-1 requires its own recursive call to comput
		# F_n-2, as it doesn't have knowledge of the value of F_n-2 that was computed earlier level of recrusion
		#snowballing affect leads to exponential running time

def good_fibonacci(n):
	if n <= 1:
		return (n,0)
	else:
		(a,b) = good_fibonacci(n-1)
		return (a+b, a)
#this takes O(n) time 
# print(good_fibonacci(5))

#Another pitfall is running into infinite recursion (no base case)
#programmer should ensure each recursive call is in som eway progressing toward a base case

#interpreter can be dynamically reconfigred to change default recursive limit
# import sys
# old = sys.getrecursionlimit()
# print(old)
# sys.setrecursionlimit(1000000)


def linear_sum(S, n):
	if n == 0:
		return 0
	else:
		return linear_sum(S, n-1)+ S[n-1]

def reverse(S, start, stop):
	if start < stop - 1:
		S[start], S[stop-1] = S[stop-1], S[start]
		reverse(S, start+1, stop-1)

#Reversing the elements of a sequence using linear recursion

def power(x,n):
	if n == 0:
		return 1
	else:
		return x *power(x, n-1)

#this version is more efficient, recurision call is at most half of exponent
def power(x, n):
	if n == 0:
		return 1
	else:
		partial = power(x, n//2)
		result = partial*partial
		if n%2 == 1:
			result *= x
		return result

def binary_sum(S, start, stop):
	if start >= stop:
		return 0
	elif start == stop-1:
		return S[start]
	else:
		mid = (start+stop)//2
		return binary_sum(S, start, mid) + binary_sum(S, mid, stop)

U = {0,1,2,3,4,5,6,7,8,9}

###################################################

# R-4.1 Describe a recursive algorithm for finding the maximum element in a se-
# quence, S, of n elements. What is your running time and space usage?

def find_max(s):
	def find_m(S, stop):
		if stop == 0:
			return S[stop]
		else:
			return max(S[stop],find_m(S, stop-1))
	return find_m(S, len(S) - 1)

# print(find_max([1,2,3,1,5], 4))
#running time is O(n) and space usage is also O(n)


# R-4.2 Draw the recursion trace for the computation of power(2, 5), using the
# traditional function implemented in Code Fragment 4.11.
# Drawn on notepad. Stack of 6. Bottomed out at power(2,0), returning 1.


# R-4.3 Draw the recursion trace for the computation of power(2, 18), using the
# repeated squaring algorithm, as implemented in Code Fragment 4.12.
# Drawn on notepad.  Stack of 6.

# R-4.6 Describe a recursive function for computing the n th Harmonic number,
# H n = ∑ ni=1 1/i.
def harmonic_num(n):
	if n == 1:
		return 1
	else:
		return (1/n) + harmonic_num(n-1)

# print(harmonic_num(5))

# R-4.7 Describe a recursive function for converting a string of digits into the in-
# teger it represents. For example, 13531 represents the integer 13, 531.
def rec_str_to_int(s,n):
	if n == len(s) - 1:
		return int(s[n])
	else:
		return int(s[n])*10**(len(s) - 1 - n) + rec_str_to_int(s, n+1)

# print(rec_str_to_int('12345', 0))

# R-4.8 Isabel has an interesting way of summing up the values in a sequence A of
# n integers, where n is a power of two. She creates a new sequence B of half
# the size of A and sets B[i] = A[2i] + A[2i + 1], for i = 0, 1, . . . , (n/2) − 1. If
# B has size 1, then she outputs B[0]. Otherwise, she replaces A with B, and
# repeats the process. What is the running time of her algorithm?

#running time is log(n)

# C-4.9 Write a short recursive Python function that finds the minimum and max-
# imum values in a sequence without using any loops.
def find_max_min(S):
	def lwr_bnd(S, n):
		if n == 0:
			return S[n]
		else:
			return min(S[n], lwr_bnd(S, n-1))
	def uppr_bnd(S, n):
		if n == 0:
			return S[n]
		else:
			return max(S[n], uppr_bnd(S, n-1))
	print(lwr_bnd(S, len(S)-1), uppr_bnd(S, len(S)-1))

# find_max_min([112,4,5,16,7,-1, 10])


# C-4.10 Describe a recursive algorithm to compute the integer part of the base-two
# logarithm of n using only addition and integer division.
def log(n):
	if n == 1:
		return 0
	else:
		return 1 + log(n/2)

# print(log(8))


# C-4.11 Describe an efficient recursive function for solving the element unique-
# ness problem, which runs in time that is at most O(n**2) in the worst case
# without using sorting.

def rec_unique_set(S):
	if len(S) == 1:
		return True
	else:
		cand = S.pop()
		for elem in S:
			if cand == elem:
				return False
		return rec_unique_set(S)

# print(rec_unique_set([1,2,3,4,3]))

# C-4.12 Give a recursive algorithm to compute the product of two positive integers,
# m and n, using only addition and subtraction.
def prod(m, n):
	if n == 0:
		return 0
	else:
		return m + prod(m, n-1)
# print(prod(3,4))


# C-4.14 In the Towers of Hanoi puzzle, we are given a platform with three pegs, a,
# b, and c, sticking out of it. On peg a is a stack of n disks, each larger than
# the next, so that the smallest is on the top and the largest is on the bottom.
# The puzzle is to move all the disks from peg a to peg c, moving one disk
# at a time, so that we never place a larger disk on top of a smaller one.
# See Figure 4.15 for an example of the case n = 4. Describe a recursive
# algorithm for solving the Towers of Hanoi puzzle for arbitrary n. (Hint:
# Consider first the subproblem of moving all but the n th disk from peg a to
# another peg using the third as “temporary storage.”)
def hanoi_puzzle(peg_a):
	temp = []
	peg_b = []
	def helper2():
		if len(temp) == 0:
			return peg_b
		else:
			peg_b.append(temp.pop())
			return helper2()
		
	def helper():
		if len(peg_a) == 0:
			return temp
		else:
			temp.append(peg_a.pop())
			return helper()
	temp = helper()
	peg_b = helper2()
	return peg_b
	# print(helper(pyramid,0))

# print(hanoi_puzzle(['bottom', 'middle', 'top']))

# C-4.15 Write a recursive function that will output all the subsets of a set of n
# elements (without repeating any subsets).
# def find subsets(S):
# 	def helper(S, w):


# C-4.16 Write a short recursive Python function that takes a character string s and
# outputs its reverse. For example, the reverse of pots&pans would be
# snap&stop .
def rec_reverse_string(s):
	def helper(s, left, right):
		if left < right:
			s[left], s[right] = s[right], s[left]
			return helper(s, left+1, right -1)
		else:
			return s
			
	s_list = [char for char in s]
	result = helper(s_list, 0, len(s_list)-1)
	return ''.join(result)

# print(rec_reverse_string('pots&pans'))

# C-4.17 Write a short recursive Python function that determines if a string s is a
# palindrome, that is, it is equal to its reverse. For example, racecar and
# gohangasalamiimalasagnahog are palindromes.
def is_palindrome(s):
	def helper(s, left, right):
		if left == -1:
			return True
		else:
			if s[left] != s[right]:
				return False
			return helper(s, left-1, right+1)
	n = len(s)
	mid_pt = n // 2
	if n%2 == 1:
		result = helper(s, mid_pt-1, mid_pt+1)
	else:
		result = helper(s, mid_pt -1, mid_pt)
	return result

# print(is_palindrome('hanna'))


# C-4.18 Use recursion to write a Python function for determining if a string s has
# more vowels than consonants.
def more_vowels(s):
	counter = 0
	def helper(s, n, counter):
		if n == len(s):
			return counter
		else:
			if s[n] in {'a', 'e', 'i', 'o', 'u', 'y'}:
				counter += 1
			return helper(s, n+1, counter)
	counter = helper(s, 0, counter)
	if counter > len(s)//2:
		return True
	else:
		return False

# print(more_vowels('liizi'))


# C-4.19 Write a short recursive Python function that rearranges a sequence of in-
# teger values so that all the even values appear before all the odd values.

def sort_even_odd(S):
	idxs = []
	def helper(S, n):
		if n == len(S):
			return
		elif S[n]%2 == 0:
			idxs.append(n)
		helper(S, n+1)
	helper(S, 0)
	for i in range(len(S)):
		if i not in idxs:
			idxs.append(i)
	for idx,elem in enumerate(idxs):
		idxs[idx] = S[elem]
	return idxs

print(sort_even_odd([5,2, 6]))

#P4.23  Implement a recursive function with signature find(path, filename) that
# reports all entries of the file system rooted at the given path having the
# given file name.

def find(path, filename):
	results = []
	def helper(path, filename):
		if os.path.isdir(path):
			for f in os.listdir(path):
				childpath = os.path.join(path, f)
				if f == filename:
					results.append(childpath)
				else:
					helper(childpath, filename)
		else:
			return None
	helper(path, filename)
	print(results)

# find('/home/mathlizard/myblog/ekeleshian.github.io/', 'index.md')

# Python’s os module provides a function with signature walk(path) that
# is a generator yielding the tuple (dirpath, dirnames, filenames) for each
# subdirectory of the directory identified by string path, such that string
# dirpath is the full path to the subdirectory, dirnames is a list of the names
# of the subdirectories within dirpath, and filenames is a list of the names
# of non-directory entries of dirpath. For example, when visiting the cs016
# subdirectory of the file system shown in Figure 4.6, the walk would yield
# ( /user/rt/courses/cs016 , [ homeworks , programs ], [ grades ]) .
# Give your own implementation of such a walk function.
def walk(path):
	full_path = '/home/mathlizard/' + path
	fs = []
	dirs = []

	if os.path.isdir(full_path):
		for f in os.listdir(full_path):
			if os.path.isdir(full_path+'/'+f):
				dirs.append(f)
			else:
				fs.append(f)

	return (full_path, dirs, fs)

print(walk('smartFont'))

