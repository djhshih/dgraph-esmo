indir = ../dot

all: diagnostic_strategy.dg osteosarcoma_ewing.dg

%.dg: $(indir)/%.dot
	dot2dg.py -o $@ $<

clean:
	rm -f *.dg
