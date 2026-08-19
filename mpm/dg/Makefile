indir = ../dot

all: staging.dg treatment_intent.dg multimodality.dg inoperable.dg

%.dg: $(indir)/%.dot
	dot2dg.py -o $@ $<

clean:
	rm -f *.dg
