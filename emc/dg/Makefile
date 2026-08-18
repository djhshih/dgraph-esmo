indir = ../dot

all: molecular_classification.dg stage_1_surgery.dg adjuvant_low_intermediate.dg adjuvant_intermediate_high.dg locoregional_recurrence.dg metastatic.dg

%.dg: $(indir)/%.dot
	dot2dg.py -o $@ $<

clean:
	rm -f *.dg
