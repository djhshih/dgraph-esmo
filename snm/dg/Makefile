indir = ../dot

all: locoregional.dg recurrence.dg metastatic.dg

%.dg: $(indir)/%.dot
	dot2dg.py -o $@ $<

clean:
	rm -f *.dg
