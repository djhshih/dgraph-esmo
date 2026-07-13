
indir = ../dot

all: locoregional_staging.dg resectable.dg systemic_treatment.dg	

%.dg: $(indir)/%.dot
	dot2dg.py -o $@ $<

clean:
	rm -f *.dg

 