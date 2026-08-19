indir = ../dot

all: sts_locoregional_resectable.dg sts_locoregional_unresectable.dg sts_advanced_resectable.dg sts_advanced_unresectable.dg

%.dg: $(indir)/%.dot
	dot2dg.py -o $@ $<

clean:
	rm -f *.dg
