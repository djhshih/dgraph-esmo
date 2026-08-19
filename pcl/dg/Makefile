indir = ../dot

all: mf_ss.dg cd30_lpd.dg pcmzl_pcfcl.dg pclbcl_lt.dg

%.dg: $(indir)/%.dot
	dot2dg.py -o $@ $<

clean:
	rm -f *.dg
