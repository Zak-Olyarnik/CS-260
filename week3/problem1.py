#!/usr/bin/python

# Calculates the xth Fibonacci number, recursively

import sys

def fib(x):
	if x == 0:		# 0 and 1 are base cases
		return 1
	elif x == 1:
		return 1
	else:
		return fib(x-1) + fib(x-2)

def main():
	# calls the fib function with arguments
	x = int(sys.argv[1])
	print str(fib(x))

if __name__ == "__main__" :
   # then this was NOT included in another file, so, run the test driver
   main()

