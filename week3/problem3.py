#!/usr/bin/python

# Times the execution of fib and fib_memo on the first 30 numbers

import sys
import timeit			# contains timing function
import problem1		# contains fib
import problem2		# contains fib_memo

def p1():		# dummy function
	problem1.fib(count)

def p2():		# dummy function
	problem2.fib_memo(count)

# times both functions using the dummy functions above
f = open('mydata.txt', 'w')
for count in range(1, 41):
	mytime = timeit.Timer( 'p1()', 'from __main__ import p1' )
	delta = mytime.timeit( 1 )
	mytime2 = timeit.Timer( 'p2()', 'from __main__ import p2' )
	epsilon = mytime2.timeit( 1 )

	# results are written to screen and file to be used to generate a plot later
	print str( count ) + " " +  str( 1000*delta ) + " " + str(1000*epsilon )
	f.write(str( count ) + " " + str(1000*epsilon ) + "\n" )

f.close()

