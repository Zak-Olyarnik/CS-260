# Python makefile

.PHONY : run view

problem1: perm problem1.py
		@chmod u+x problem1.py
		python problem1.py
		@echo

problem2: perm problem2.py
		@chmod u+x problem2.py
		python problem2.py
		@echo

problem3: perm problem3.py
		@chmod u+x problem3.py
		python problem3.py
		@echo		
		@gnuplot < plot-instructions
		eog plot.png

perm : cell.py linkedList.py
		@chmod u+x cell.py
		@chmod u+x linkedList.py
		@chmod u+x celltest.py

run : problem1 problem2 problem3 view

view : problem1.py problem2.py
		@\less linkedList.py
		@\less problem1.py
		@\less problem2.py

