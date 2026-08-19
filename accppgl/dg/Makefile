indir = ../dot

all: acc_resectable.dg ppgl_resectable.dg acc_advanced.dg ppgl_advanced.dg

%.dg: $(indir)/%.dot
	dot2dg.py -o $@ $<

clean:
	rm -f *.dg
