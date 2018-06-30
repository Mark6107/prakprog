all: AB

AB: problems.py out.txt ode.py

out.txt: 
	python3 -c 'from problems import *; probAB()' > $@

clean:
	rm *.txt *.pdf
