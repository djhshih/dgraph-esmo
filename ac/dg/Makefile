indir = ../dot

all: diagnosis.dg localised.dg advanced.dg

%.dg: $(indir)/%.dot
	dot2dg.py -o $@ $<

clean:
	rm -f *.dg
