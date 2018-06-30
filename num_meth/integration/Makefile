all: A B

A: problems.py outA.txt integ.py

outA.txt: 
	python3 -c 'from problems import *; probA()' > $@

B: problems.py outB.txt integ.py

outB.txt: 
	python3 -c 'from problems import *; probB()' > $@

clean:
	rm *.txt
