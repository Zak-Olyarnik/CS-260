#!/usr/bin/python

# Concatenates two lists by changing the "next" pointer
# of the last cell of A to the first cell of B.  The
# return value is A, which now contains all cells of 
# both lists.  The A.last pointer is then reset to
# B.last, the true end of the new list.

import sys
import cell				# contains Cell class
import linkedList		# contains LinkedList class

def list_concat( A, B ):
	A.last.next = B.first
	A.last = B.last
	return A

def main():
	# creates cells to build lists
	a = cell.Cell( 4 )
	b = cell.Cell( 3, a )
	c = cell.Cell( 2, b )
	d = cell.Cell( 1, c )
	e = cell.Cell( 9 )
	f = cell.Cell( 8, e )
	g = cell.Cell( 7, f )
	h = cell.Cell( 6, g )
	i = cell.Cell( 5, h )
	z = cell.Cell( 0 )

	# prints list A
	A = linkedList.LinkedList( d )
	print "list A:"
	A.echo()

	# prints list B
	B = linkedList.LinkedList( i )
	print "list B:"
	B.echo()

	# prints the concatenated list
	X = list_concat( A, B )
	print "concatenation:"
	X.echo()

if __name__ == "__main__" :
   # then this was NOT included in another file, so, run the test driver
   main()

