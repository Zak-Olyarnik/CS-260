#!/usr/bin/python

import sys
import cell
import linkedList
import problem1

a = cell.Cell( 4 )
b = cell.Cell( 3, a )
c = cell.Cell( 2, b )
d = cell.Cell( 1, c )
e = cell.Cell( 9 )
f = cell.Cell( 8, e )
g = cell.Cell( 7, f )
h = cell.Cell( 6, g )
i = cell.Cell( 5, h )

L = linkedList.LinkedList( d )
M = linkedList.LinkedList( i )
#L.echo()
#M.echo()

X = problem1.list_concat( L, M )
#X.echo()
