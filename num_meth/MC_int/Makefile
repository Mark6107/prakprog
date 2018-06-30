all: AB

AB: problems.py out.txt integ_mc.py

out.txt: 
	python3 -c 'from problems import *; probAB()' > $@

clean:
	rm *.txt *.pdf
