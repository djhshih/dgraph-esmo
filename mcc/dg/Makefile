indir = ../dot

all: mcc_locoregional.dg mcc_advanced.dg

%.dg: $(indir)/%.dot
	dot2dg.py -o $@ $<

clean:
	rm -f *.dg
