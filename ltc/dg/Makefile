indir = ../dot

all: lung_adjuvant.dg thymic_adjuvant.dg functioning_syndrome.dg advanced.dg

%.dg: $(indir)/%.dot
	dot2dg.py -o $@ $<

clean:
	rm -f *.dg
