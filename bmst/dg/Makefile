indir = ../dot

all: diagnostic_workup.dg treatment_lung.dg treatment_breast.dg treatment_melanoma.dg

%.dg: $(indir)/%.dot
	dot2dg.py -o $@ $<

clean:
	rm -f *.dg
