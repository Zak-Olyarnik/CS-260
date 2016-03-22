#!/usr/bin/env python

import node				# contains Node class
from lexer import *	# contains input & tokenizing functions

def infix(T):		# left, me, right
   if T:
		infix(T.left)
		print str(T.data),
		infix(T.right) 
   else:
		return

def prefix(T):		# me, left, right
   if T:
		print str(T.data),
		prefix(T.left)
		prefix(T.right)
   else:
      return

def postfix(T):	# left, right, me
   if T:
		postfix(T.left)
		postfix(T.right)
		print str(T.data),
   else:
      return

# EXTRA CREDIT: evaluates the expression by recursively evaluating
# all of the operands
def eval(T):
	if T:
		if str.isdigit( T.data[0] ) :
			return int(T.data)
		else:
			if T.data[0] == "+":
				return eval(T.left) + eval(T.right)
			elif T.data[0] == "-":
				return eval(T.left) - eval(T.right)
			elif T.data[0] == "*":
				return eval(T.left) * eval(T.right)
			elif T.data[0] == "/":
				return eval(T.left) / eval(T.right)



# main.  Places the tokens into a "stack", directly appending any
# digits and re-wrapping any operators into a new tree sublevel
stack = []
while get_expression():
	t = get_next_token()
	while t:
		if str.isdigit( t[0] ) : # we have a (non-negative) number
			mynode = node.Node(t)
			stack.append(mynode)
		else:
			mynode = node.Node(t)
			right = stack.pop()
			left = stack.pop()
			mynode.right = right
			mynode.left = left
			stack.append(mynode)
		t = get_next_token()

	# prints pre-, in-, and post-orders and then evaluates the tree
	tree = stack.pop()
	print "Pre: ",
	prefix(tree)
	print "\nIn: ",
	infix(tree)
	print "\nPost: ",
	postfix(tree)
	print "\nEval: ",
	print str(eval(tree))
	print "\n"
