indir = ../dot

all: lynch_syndrome.dg gastric_cancer.dg

%.dg: $(indir)/%.dot
	dot2dg.py -o $@ $<

clean:
	rm -f *.dg
