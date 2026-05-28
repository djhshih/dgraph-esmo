
indir = ../dot

all: ebc.dg ebc-aln.dg ebc-dx.dg ebc-her2-pos.dg ebc-hr-pos.dg ebc-tnbc.dg ebc-hr-pos-her2-neg.dg
	

%.dg: $(indir)/%.dot
	dot2dg.py -o $@ $<

clean:
	rm -f *.dg

