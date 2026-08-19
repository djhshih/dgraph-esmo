indir = ../dot

all: gist_localised.dg gist_advanced.dg

%.dg: $(indir)/%.dot
	dot2dg.py -o $@ $<

clean:
	rm -f *.dg
