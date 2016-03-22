#!/usr/bin/python

# implementation of Heap Class.  Made to mimic a priority queue, so includes
# methods like insert, upHeap, and deleteMin which are unused in the current
# assignment

class Heap:
	def __init__(self):
		self.array = [0]
		self.size = 0

	# moves smaller data up the heap
	def upHeap(self,i):
		while i // 2 > 0:		# floor division, always returns int, makes sure
									# we have not reached root
			if self.array[i] < self.array[i // 2]:	# swaps current with parent
				temp = self.array[i // 2]
				self.array[i // 2] = self.array[i]
				self.array[i] = temp
				i = i // 2
			else:
				return

	def insert(self,new):
		self.array.append(new)
		self.size = self.size + 1
		self.upHeap(self.size)

	# moves larger data down the heap
	def downHeap(self,i):
		while (i * 2) <= self.size:	# keeps from falling off the end
			minChild = self.findMinChild(i)
			if self.array[i] > self.array[minChild]:	# swaps current with
				temp = self.array[i]							# minChild
				self.array[i] = self.array[minChild]
				self.array[minChild] = temp
				i = minChild
			else:
				return		# if current not < minChild, it is placed correctly

	def findMinChild(self,i):
		left = 2 * i
		right = 2 * i +  1
		if right > self.size:	# if right child does not exist in the heap,
			return left				# then left child must be returned
		else:
			if self.array[left] < self.array[right]: # else compare directly
				return left
			else:
				return right

	def deleteMin(self):
		root = self.array[1]
		self.array[1] = self.array[self.size]	# swaps root (being deleted)
		self.size = self.size - 1					# with lowest leaf, then
		self.array.pop()								# downheaps that leaf back into
		self.downHeap(1)								# position
		return root

	# makes the heap from an initial array
	def makeHeap(self, dataArray):
		i = len(dataArray) // 2			# everything past the halfway point in
												# the array will be a leaf and does not
												# need processed
		self.size = len(dataArray)
		self.array = [0] + dataArray[:]	# putting an unused 0 in the first
													# array slot will simplify integer
													# operations later
		while (i > 0):
			self.downHeap(i)				# downHeaps nodes from the last interior
												# parent up to the root
			i = i - 1
