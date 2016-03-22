#!/usr/bin/python


# implements a disjoint set system with initialize, find, and merge
# functions

import node

# creates a list of nodes who are their own parents and size 1
def Initialize(Values):
	set = []	
	for i in Values:
		mynode = node.Node(i)
		set.append(mynode)
	return set

# returns the parent of the given node, also performing path compression by
# recursively calling Find to adjust all parents to the root
def Find(set, value):
	for i in set:     # converts int values passed in into node type
		if i.value == value:
			v1 = i

	if v1.parent != v1:
		v1.parent = Find(set, v1.parent.value)
	return v1.parent

# combines two values into one set by always appending the smaller to the
# larger, or just arbitrarily appending and updating size if they're the same
def Merge(set, value1, value2):
	root1 = Find(set, value1)
	root2 = Find(set, value2)
	if root1 == root2:
		return

	for i in set:		# converts int values passed in into node type
		if i.value == value1:
			v1 = i
		elif i.value == value2:
			v2 = i

	if v1.size < v2.size:
		root1.parent = root2
		root2.size = root2.size + root1.size
	elif v2.size < v1.size:
		root2.parent = root1
		root1.size = root1.size + root2.size
	else:
		root2.parent = root1
		root1.size = root1.size + root2.size

