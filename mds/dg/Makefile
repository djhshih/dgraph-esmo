indir = ../dot

all: cytogenetics.dg higher_risk.dg lower_risk.dg

%.dg: $(indir)/%.dot
	dot2dg.py -o $@ $<

clean:
	rm -f *.dg
