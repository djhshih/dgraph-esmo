indir = ../dot

all: early_intermediate.dg advanced.dg

%.dg: $(indir)/%.dot
	dot2dg.py -o $@ $<

clean:
	rm -f *.dg
