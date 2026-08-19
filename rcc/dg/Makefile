indir = ../dot

all: diagnosis.dg locoregional.dg advanced_ccrcc.dg advanced_prcc.dg advanced_ncc.dg

%.dg: $(indir)/%.dot
	dot2dg.py -o $@ $<

clean:
	rm -f *.dg
