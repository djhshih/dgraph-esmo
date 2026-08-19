indir = ../dot

all: cup_vs__ve_nsclc.dg cup_vs_+ve_nsclc.dg cup_vs_cca.dg cup_vs_ovarian.dg cup_vs_rcc.dg cup_vs_sgc.dg cup_vs_breast.dg

%.dg: $(indir)/%.dot
	dot2dg.py -o $@ $<

clean:
	rm -f *.dg
