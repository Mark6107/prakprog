all: A B

A: problems.py outA.txt lin_eq.py

outA.txt: 
	python3 -c 'from problems import *; probA()' > $@

B: problems.py outB.txt lin_eq.py

outB.txt: 
	python3 -c 'from problems import *; probB()' > $@

clean:
	rm *.txt *.pdf
