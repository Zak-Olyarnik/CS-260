#!/usr/bin/python

# Calculates the xth Fibonacci number, using memoisation

import sys

def fib_memo(x):
# clears the storage list, initializes the base cases,
# and calls a secondary fib_ function to actually compute
	F = [-1] * 101
	F[0] = 1
	F[1] = 1
	return str(fib_(x,F))

def fib_(x,F):
# checks the list to see if the xth number has already
# been computed before doing it manually.  Adds each new
# number computed to the list to make future runs faster
	if F[x] != -1:
		return F[x]
	else:
		F[x] = fib_(x-1,F) + fib_(x-2,F)
		return F[x]

def main():
	# calls the fib_memo function with arguments
	x = int(sys.argv[1])
	print fib_memo(x)

if __name__ == "__main__" :
   # then this was NOT included in another file, so, run the test driver
   main()

