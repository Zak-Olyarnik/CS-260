#!/usr/bin/env python

# simple node class

class Node:

	def __init__( self, value, size=1 ):
		self.value = value
		self.parent = self
		self.size = size

