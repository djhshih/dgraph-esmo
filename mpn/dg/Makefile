indir = ../dot

all: diagnosis.dg treatment.dg

%.dg: $(indir)/%.dot
	dot2dg.py -o $@ $<

clean:
	rm -f *.dg
