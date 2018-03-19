CFLAGS = -Wall -std=gnu11
CFLAGS += `gsl-config --cflags`
LDLIBS = `gsl-config --libs`

all: output ; cat $<
output: main ; ./$< > $@
clean: ; $(RM) main output

