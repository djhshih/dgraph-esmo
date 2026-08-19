indir = ../dot

all: ukp_locoregional.dg gugy_locoregional.dg hn_locoregional.dg metastatic.dg functioning_syndrome.dg parathyroid_carcinoma.dg intrathyroid_thymic.dg

%.dg: $(indir)/%.dot
	dot2dg.py -o $@ $<

clean:
	rm -f *.dg
