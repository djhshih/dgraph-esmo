indir = ../dot

all: hboc_brca1.dg hboc_brca2.dg

%.dg: $(indir)/%.dot
	dot2dg.py -o $@ $<

clean:
	rm -f *.dg
