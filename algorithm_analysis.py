# Simple approach to study running time
from time import time
start_time = time()
#run algorithm
end_time = time()
elapsed = end_time - start_time

# a 'fairer' metric - measuring number of CPU cycles -- can use
# clock function of the time module, but stil might be inconsistent

#more advanced -- module named timeit

#O(n) time example
def find_max(seq):
	biggest = seq[0]
	for i in seq:
		if i > biggest:
			biggest = i
	return biggest

# Exploring time complexities with computing prefix averages
# A prefix average: given a sequence S consisting of n numbers, 
# we want to compute a sequence A such that A[j] is the average
# of elements S[0], ..., S[j] for j = 0, ..., n-1
from pdb import set_trace
def prefix_avg1(S):
	"""Return list such that for al j, A[j] equals average of S[0], ..,S[j]"""
	n = len(S) 						#runs O(1)
	A = [0] * 0 					# runs O(n)
	for jdx in range(n):			#maintaining counter j is O(n)
		total = 0					#runs O(n)
		for idx in range(jdx+1):	#maintaining counter i is O(n^2)
			total += S[idx]			#runs 1 + 2+ 3+...+n = n(n+1)/2 = O(n^2) time
			set_trace()
		A[jdx] = total/(jdx+1)		#runs O(n)
	return A

	#To simplify, the time complexity for prefix_avg1 is O(n^2)

data = [1, 2, 3, 4, 5, 6, 7]
# print(prefix_avg1(data))


def prefix_avg2(S):
	n = len(S)
	A = [0] * n
	for j in range(n):
		A[j] = sum(S[0:j+1])/(j+1)		#sum() takes O(j+1), and [0:j+1] also takes O(j+1) time
	return A

	#running time for prefix_avg2 is still dominated by a series of steps that take time 
	# proportional to 1 + 2 + 3 + ... + n and thus O(n^2)


def prefix_avg3(S):
	num = len(S) 					# this is O(1)
	A = [0] * num 					#this is O(n)
	total = 0 						#this is O(1)
	for idx in range(num):
		total += S[idx]				#this is O(n) 
		A[idx] = total/(idx+1)		#this is O(n)
		set_trace()
	return A

	#running time of prefix_avg3 is O(n). Effective that we maintain the current prefix sum dynamically

# print(prefix_avg3(data))

# Exploring time complexities with computing 3-way set disjointness
#suppose A, B, C all have distinct elements in them
def disjoint1(A, B, C):
	"""Return True if there is no element common to all three lists"""
	for a in A:
		for b in B:
			for c in C:
				if a == b == c:
					return False
	return True
	# running time is O(n^3)


def disjoint2(A, B, C):
	for a in A:								#this is O(n)
		for b in B:							# this is O(n^2)
			if a == b:						#evaluated O(n^2 times)
				for c in C:					# maintained O(n^2) times 
					if a == c:
						return False
	return True


#Exploring time comps with computing element uniqueness
def unique1(S):
	"""Return True if there are no duplicate elements in sequence S"""
	for j in range(len(S)):				#1st iter causes n - 1 iterations of inner loop, 2nd iter causes n-2 iterations of inner loop, etc.
		for k in range(j+1, len(S)):	
			if S[j] == S[k]:
				return False
	return True

	#Since the first iter. of the outerloop causes n-1 iterations of the inner loop, etc, we have
	# n-1 + n-2 + n-3+... + 2+ 1 = O(n^2)

def unique2(S):
	temp = sorted(S)					#guarantees O(nlogn)
	for j in range(1, len(temp)):		#this is O(n)
		if temp[j-1] == temp[j]:
			return False
	return True

	#unique2 runs in O(nlogn) which is asymptotically better than unique1

#Exercises
#R-3.1
"""
Graph the functions 8n, 4nlog n, 2n^2 , n^3 , and 2^n using a logarithmic scale
for the x- and y-axes; that is, if the function value f (n) is y, plot this as a
point with x-coordinate at log n and y-coordinate at log y.
"""
import math
import matplotlib.pyplot as plt

# plt.plot([math.log10(i) for i in range(1,10000,1000)], [math.log10(i*8) for i in range(1,10000,1000)])
# plt.plot([math.log10(i) for i in range(1,10000,1000)], [math.log10(i*4)*math.log(i) for i in range(1,10000,1000)])
# plt.plot([math.log10(i) for i in range(1,10000,1000)], [math.log10(2*(i**2)) for i in range(1,10000,1000)])
# plt.plot([math.log10(i) for i in range(1,10000,1000)], [math.log10(2**i) for i in range(1,10000,1000)])

# plt.show()

# R-3.2 The number of operations executed by algorithms A and B is 8n log n and
# 2n^2 , respectively. Determine n 0 such that A is better than B for n ≥ n 0 .
# plt.plot([i for i in range(1,30,3)], [(i*8)*math.log(i) for i in range(1,100,10)])
# plt.plot([i for i in range(1,30,3)], [ 2 * (i**2) for i in range(1,100,10)])

# plt.show()

#n >= 5

# R-3.3 The number of operations executed by algorithms A and B is 40n**2 and
# 2n**3 , respectively. Determine n 0 such that A is better than B for n ≥ n 0 .
# plt.plot([i for i in range(1,20, 2)], [40*(i**2) for i in range(1,100,10)])
# plt.plot([i for i in range(1,20,2)], [ 2*(i**3) for i in range(1,100,10)])

# plt.show()

#N >= 5

# R-3.4 Give an example of a function that is plotted the same on a log-log scale
# # # as it is on a standard scale.

# plt.plot([math.log(i) for i in range(1,1000,10)], [math.log(i) for i in range(1,1000,10)])
# plt.plot([i for i in range(1,100,10)], [i for i in range(1,100,10)])

# plt.show()

# R-3.5 Explain why the plot of the function n^c is a straight line with slope c on a
# log-log scale.
# log(n^c) = c*log(n), and since log(y) = log(x) generates a linear equation, so too does n^c

# R-3.6 What is the sum of all the even numbers from 0 to 2n, for any positive
# integer n?
#(2n)n/2 ==> n^2

# R-3.7 Show that the following two statements are equivalent:
# (a) The running time of algorithm A is always O( f (n)).
# (b) In the worst case, the running time of algorithm A is O( f (n)).

#R-3.9 Order the following functions by asymptotic growth rate.
# 4n log n + 2n    2^10      2^(log n)
# 3n + 100 log n        4n
# 2^n
# n^2 + 10n
# n^3                 nlogn

# sorting from least to greatest: 4n, nlogn, 2n+4nlogn, 3n+100logn, n^2 + 10n, n^3, 2^(logn), 2^n

def example1(S):
	n = len(S)
	total = 0
	for j in range(n):
		total += S[j]
	return total


# #R-3.23
# Give a big-Oh characterization, in terms of n, of the running time of the
# example1 function shown in Code Fragment 3.10.
# O(n)

def example2(S):
	n = len(S)
	total = 0
	for j in range(0, n, 2):
		total += S[j]
	return total

#R-3.24
# Give a big-Oh characterization, in terms of n, of the running time of the
# example2 function shown in Code Fragment 3.10.
# O(n)

def example3(S):
	n=len(S)
	total = 0
	for j in range(n):
		for k in range(1 + j):
			total += S[k]
	return total
#R-3.25
# Give a big-Oh characterization, in terms of n, of the running time of the
# example3 function shown in Code Fragment 3.10.
# O(n^2)

def example4(S):
	n = len(S)
	prefix = 0
	total = 0
	for j in range(n):
		prefix += S[j]
		total += prefix
	return total
# #R-3.26
# Give a big-Oh characterization, in terms of n, of the running time of the
# example4 function shown in Code Fragment 3.10.
# O(n)

def example5(A,B):
	n = len(A)
	count = 0
	for i in range(n):
		total = 0
		for j in range(n):
			for k in range(1+j):
				total += A[k]
		if B[i] == total:
			count +=1
	return count

#R-3.27
# Give a big-Oh characterization, in terms of n, of the running time of the
# example5 function shown in Code Fragment 3.10.
# O(n^3)

import random
arr = []
for k in range(5):
	arr.append(random.randint(0,10000))

def partition(A, lo, hi):
	pivot = hi
	mid = (lo+hi)//2
	if A[lo] < A[mid]:
		if A[mid]< A[hi]:
			pivot = mid
	elif A[lo] < A[hi]:
		pivot = lo
	pivotvalue = A[pivot]
	leftmark = lo + 1
	rightmark = hi
	done = False
	while not done:
		while leftmark <= rightmark and A[leftmark] <= pivotvalue:
			leftmark +=1
		while A[rightmark] >= pivotvalue and rightmark >= leftmark:
			rightmark-=1
		if rightmark < leftmark:
			done = True
		else:
			temp = A[leftmark]
			A[leftmark] = A[rightmark]
			A[rightmark] = temp
	temp = A[lo]
	A[lo] = A[rightmark]
	A[rightmark] = temp

	return rightmark


def quicksort(array):
	quicksort2(array, 0, len(array)-1)

def quicksort2(array, low, high):
	if low < high:
		pivot = partition(array, low, high)
		quicksort2(array, low, pivot-1)
		quicksort2(array, pivot+1, high)

# print(arr)
# quicksort(arr)
# print(arr)

def selectionsort(array):
	for i in range(len(array)-1, 0, -1):
		max_idx = 0
		for idx in range(1, i+1):
			if array[idx] > array[max_idx]:
				max_idx = idx
		temp = array[i]
		array[i]=array[max_idx]
		array[max_idx] = temp

# print(arr)
# selectionsort(arr)
# print(arr)

# def mergesort(array):
# 	if len(array) <= 1:
# 		return array
# 	mid_pt = int(len(array)/2)


# 	left, right = mergesort(array[:mid_pt]), mergesort(array[mid_pt:])
# 	return merge(left, right)

# def merge(left, right):
# 	result = []
# 	r_idx = l_idx = 0
# 	while l_idx < len(left) and r_idx < len(right):
		







