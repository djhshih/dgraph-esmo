indir = ../dot

all: pan_net_surgical.dg si_net_surgical.dg carcinoid_syndrome.dg systemic_therapy.dg

%.dg: $(indir)/%.dot
	dot2dg.py -o $@ $<

clean:
	rm -f *.dg
