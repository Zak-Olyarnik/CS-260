#!/usr/bin/python

# Concatenates two lists by iterating through A and
# then B and creating a third list, X, with the same
# data.  This is done so that changing either of the 
# original lists does not affect the concatenation.

import sys
import cell				# contains Cell class
import linkedList		# contains LinkedList class

def list_concat_copy( A, B ):
	z = cell.Cell ( A.first.data )
	C = linkedList.LinkedList(	z )
	
	# iterates through list A, copying all data to C
	current = A.first
	while current.next != None:
		current = current.next
		y = cell.Cell (current.data)
		C.add(y)

	# iterates through list B
	z = cell.Cell ( B.first.data )
	C.add(z)	
	current = B.first
	while current.next != None:
		current = current.next
		y = cell.Cell (current.data)
		C.add(y)

	return C

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

	# prints list A
	A = linkedList.LinkedList( d )
	print "list A:"
	A.echo()

	# prints list B
	B = linkedList.LinkedList( i )
	print "list B:"
	B.echo()

	# prints the concatenated list
	X = list_concat_copy( A, B )
	print "concatenation:"
	X.echo()

	# demonstrates that changing A does not affect X
	print "changing A:"
	A = B
	A.echo()
	print "concatenation is unaffected:"
	X.echo()

if __name__ == "__main__" :
   # then this was NOT included in another file, so, run the test driver
   main()

