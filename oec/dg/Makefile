indir = ../dot

all: oec_local.dg oec_advanced.dg

%.dg: $(indir)/%.dot
	dot2dg.py -o $@ $<

clean:
	rm -f *.dg
