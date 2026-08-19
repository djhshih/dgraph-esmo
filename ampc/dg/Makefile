indir = ../dot

all: denovo_mcspc.dg relapsed_mcspc.dg high_risk_nmcrpc.dg mcrpc_no_genetic.dg mcrpc_genetic.dg

%.dg: $(indir)/%.dot
	dot2dg.py -o $@ $<

clean:
	rm -f *.dg
