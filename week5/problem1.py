#!/usr/bin/python

# 

import sys
import timeit		# contains timing function
import heap			# contains Heap class
import random		# contains random number generator


def make_heap():
	a.makeHeap(items)

def main():

	# defines a global Heap.  I know that globals should
	# generally be avoided, but I couldn't get it into the
	# dummy function to use timeit any other way
	global a
	a = heap.Heap()
	
	# defines items as an array of random numbers from which
	# to build a heap.  The rng takes a sampling of numbers from the
	# range 0-110000
	global items
	for i in range(1,11):
		items = random.sample(xrange(110000), 10000*i)

		# code to time execution, using the dummy function above
   	# in order to avoid passing arguments
		mytime = timeit.Timer( 'make_heap()', 'from __main__ import make_heap' )
		delta = mytime.timeit( 1 )
		# results are written to screen
		print str(10000*i) +  " " + str(1000*delta)



if __name__ == "__main__" :
   # then this was NOT included in another file, so, run the test driver
   main()

