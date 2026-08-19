indir = ../dot

all: seminoma.dg non_seminoma.dg

%.dg: $(indir)/%.dot
	dot2dg.py -o $@ $<

clean:
	rm -f *.dg
