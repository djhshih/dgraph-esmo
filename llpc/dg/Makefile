indir = ../dot

all: diagnosis_staging.dg localised_treatment.dg very_high_risk_cn1.dg biochemical_recurrence.dg

%.dg: $(indir)/%.dot
	dot2dg.py -o $@ $<

clean:
	rm -f *.dg
