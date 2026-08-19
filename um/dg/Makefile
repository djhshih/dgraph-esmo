indir = ../dot

all: staging_risk.dg primary.dg metastatic.dg surveillance.dg

%.dg: $(indir)/%.dot
	dot2dg.py -o $@ $<

clean:
	rm -f *.dg
