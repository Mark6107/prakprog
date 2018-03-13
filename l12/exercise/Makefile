TEX = -pdf -pdflatex="pdflatex"
CFLAGS = -I/usr/include
LDLIBS = -L/usr/lib/x86_64-linux-gnu -lgsl -lgslcblas -lm

all: out.txt report.pdf
report.pdf: report.tex
    latexmk $<

out.txt: main
	./$< -20 20 0.2 > $@
main: main.c
