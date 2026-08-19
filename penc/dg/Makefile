indir = ../dot

all: diagnosis.dg primary_tumour.dg inguinal_ln.dg

%.dg: $(indir)/%.dot
	dot2dg.py -o $@ $<

clean:
	rm -f *.dg
