indir = ../dot

all: pc_sus.dg pc_local.dg pc_met.dg pc_met_precision.dg

%.dg: $(indir)/%.dot
	dot2dg.py -o $@ $<

clean:
	rm -f *.dg
