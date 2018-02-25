CFLAGS = -Wall -std=gnu11
LDLIBS = -lm

.PHONY: default clean
default: out.txt
	cat $<

out.txt: main
	./$< > $@

main: main.o nvector.o

main.o komplex.o: nvector.h

clean:
	$(RM) main main.o nvector.o out.txt
