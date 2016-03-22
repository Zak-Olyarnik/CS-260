#!/usr/bin/python

# Times the execution of list_concat and list_concat_copy
# with input lists of sizes 1000-15000

import sys
import cell          # contains Cell class
import linkedList    # contains LinkedList class
import timeit			# contains timing function
import problem1		# contains list_concat
import problem2		# contains list_concat_copy

def p1():		# dummy function
	problem1.list_concat( A, B )

def p2():		# dummy function
	problem2.list_concat_copy( C, D )

# creates four lists to use concatenation functions on
# the outer loop handles the different data sizes and
# the inner loop actually adds the cells to each list
x = 0
f = open('mydata.txt', 'w')
for count in range(1, 16):
	A = linkedList.LinkedList( cell.Cell( x ))
	B = linkedList.LinkedList( cell.Cell( x ))
	C = linkedList.LinkedList( cell.Cell( x ))
	D = linkedList.LinkedList( cell.Cell( x ))
	for num in range(1, count*1000):
		A.add( cell.Cell( x ))
		B.add( cell.Cell( x ))
		C.add( cell.Cell( x ))
		D.add( cell.Cell( x ))

	# code to time execution, using the dummy functions above
	# in order to avoid passing arguments
	mytime = timeit.Timer( 'p1()', 'from __main__ import p1' )
	delta = mytime.timeit( 1 )
	mytime2 = timeit.Timer( 'p2()', 'from __main__ import p2' )
	epsilon = mytime2.timeit( 1 )

	# results are written to screen and file to be used to generate a plot later
	print str( 1000*count ) + " " +  str( 1000*delta ) + " " + str(1000*epsilon )
	f.write(str( 1000*count ) + " " +  str( 1000*delta ) + " " + str(1000*epsilon ) + "\n" )

f.close()

