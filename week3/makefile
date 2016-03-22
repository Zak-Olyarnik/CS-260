# Python makefile

.PHONY : run

problem1: problem1.py
		@chmod u+x problem1.py
		python problem1.py $(arg)
		@echo

problem2: problem2.py
		@chmod u+x problem2.py
		python problem2.py $(arg)
		@echo

problem3: problem3.py
		@chmod u+x problem3.py
		python problem3.py
		@echo		
		@gnuplot < plot-instructions
		eog plot.png

view : problem1.py problem2.py
		@\less problem1.py
		@\less problem2.py

