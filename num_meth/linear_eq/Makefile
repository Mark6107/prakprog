all: A B

A: problems.py outA.txt

outA.txt: 
	python3 -c 'from problems import *; probA1()' > $@
	python3 -c 'from problems import *; probA2()' >> $@

B: problems.py outB.txt

outB.txt: 
	python3 -c 'from problems import *; probB()' > $@

clean:
	rm *.txt
