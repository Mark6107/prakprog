CFLAGS = -Wall -std=gnu11
LDLIBS = -lm
.PHONEY: all clean
all				: out.txt		; cat $<
out.txt			: main			; ./$< > $@
main			: main.o komplex.o
main.o komplex.o: komplex.h
clean			:				; $(RM) main main.o komplex.o out.txt
