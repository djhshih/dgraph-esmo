indir = ../dot

all: resectable.dg unresectable.dg metastatic.dg

%.dg: $(indir)/%.dot
	dot2dg.py -o $@ $<

clean:
	rm -f *.dg
