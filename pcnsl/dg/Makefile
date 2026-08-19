indir = ../dot

all: diagnosis.dg first_line.dg pvrl.dg rr.dg

%.dg: $(indir)/%.dot
	dot2dg.py -o $@ $<

clean:
	rm -f *.dg
