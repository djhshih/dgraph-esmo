
indir = ../dot

all: ebc.dg ebc-aln.dg ebc-dx.dg
	

%.dg: $(indir)/%.dot
	dot2dg.py -o $@ $<

clean:
	rm -f *.dg

