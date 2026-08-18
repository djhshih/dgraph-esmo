all: pdf/molecular_classification.pdf pdf/stage_1_surgery.pdf pdf/adjuvant_low_intermediate.pdf pdf/adjuvant_intermediate_high.pdf pdf/locoregional_recurrence.pdf pdf/metastatic.pdf

pdf/%.pdf: %.dot
	dot -Tpdf -o $@ $<

clean:
	rm -f pdf/*.pdf
