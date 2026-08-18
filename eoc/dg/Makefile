indir = ../dot

all: eoc_early.dg eoc_advanced.dg eoc_recurrent.dg

%.dg: $(indir)/%.dot
	dot2dg.py -o $@ $<

clean:
	rm -f *.dg
