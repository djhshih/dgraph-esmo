
indir = ../dot

all: locoregional.dg metastatic.dg recurrence.dg
	

%.dg: $(indir)/%.dot
	dot2dg.py -o $@ $<

clean:
	rm -f *.dg

