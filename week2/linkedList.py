#!/usr/bin/python

# uses the cell class as a template to build linked lists

import sys
import cell

class LinkedList:

	# the linked list has attribues first and last,
	# which serve as pointers to the first and last
	# cells in the list
	def __init__( self, first ):
		self.first = first
		current = self.first
		while current.next != None:
			current = current.next
		self.last = current

	# walks the list to print out the data stored
	# in each cell
	def __str__( self ):
		current = self.first
		running = ( current.__str__() )
		while current.next != None:
			current = current.next
			running = running + ( current.__str__() )
		return str( running )

	def echo( self ):
		print self.__str__()

	# allows the addition of a new cell to the end
	# of a list.  Very important that .last is kept
	# accurate!
	def add( self, c ):
		self.last.next = c
		self.last = self.last.next

