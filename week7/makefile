# Python makefile

.PHONY : run view

prob1: node.py set.py test-set-new.py
		@chmod u+x node.py
		@chmod u+x set.py
		@chmod u+x test-set-new.py
		python test-set-new.py

run : prob1

view : node.py set.py
		@\less node.py
		@\less set.py


