#!/usr/bin/python

# implements Floyd's all-pairs shortest-paths algorithm plus predecessor
# matrix

import sys

def floyd(graph):

	distance = {}			# shortest path matrix
	predecessor = {}		# predecessor matrix
	for key in graph:
		distance[key] = {}	# sizes matrices
		predecessor[key] = {}
		for val in graph:
			distance[key][val] = float("inf")	# fills in initial values
			predecessor[key][val] = key
		distance[key][key] = 0
		
	for key in graph:
		for adjVertex in graph[key]:
			distance[key][adjVertex] = graph[key][adjVertex]	# initial costs
			distance[adjVertex][key] = graph[key][adjVertex]	# makes this an
																			# undirected graph
			predecessor[key][adjVertex] = key
 
	# iterates through matrix to check if path being currently viewed is
	# shorter than established path, and replaces it if it is
	for i in graph:
		for j in graph:
			for k in graph:
				path = distance[j][i] + distance[i][k]
				if path < distance[j][k]:
					distance[j][k] = path
					distance[k][j] = path
					predecessor[j][k] = predecessor[i][k]
					predecessor[k][j] = predecessor[i][k]

	return distance, predecessor

 
# main 

graphList = raw_input().split(' ')	# reads in undirected graph from stdin
graph = {}		# map representation of undirected graph
maxrow = 0		# helps size the map

for i in range(0,len(graphList)):
	if ',' not in graphList[i]:
		maxrow = maxrow + 1			# counts number of nodes

for i in range(0,maxrow):		# continues to build graph
	graph[i] = {}

j = 0
for i in range(1,len(graphList)):
	if ',' in graphList[i]:
		mylist = graphList[i].split(',')		# separates node and weight
		graph[j][int(mylist[0])] = int(mylist[1])		# adds to graph
	else:
		j = j + 1		# move to next row
 

distance, predecessor = floyd(graph)	# generate matrices based on graph

# printing output
print "Distance matrix:"
for key in distance:
	for val in distance:
		if distance[key][val] == float("inf"):
			print '%3s' % ("INF"),
		else:
			print '%3g' % (distance[key][val]),
	print
print

print "Predecesor matrix:"
for key in predecessor:
	for  val in predecessor:
		print '%3g' % (predecessor[key][val]),
	print
