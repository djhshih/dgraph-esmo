
indir = ../dot

all: eoc-advanced.dg eoc-early.dg eoc-recurrent.dg
	

%.dg: $(indir)/%.dot
	dot2dg.py -o $@ $<

clean:
	rm -f *.dg

