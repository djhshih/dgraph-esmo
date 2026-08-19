indir = ../dot

all: newly_diagnosed.dg relapsed_refractory.dg

%.dg: $(indir)/%.dot
	dot2dg.py -o $@ $<

clean:
	rm -f *.dg
