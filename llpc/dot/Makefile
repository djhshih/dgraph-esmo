all: pdf/diagnosis_staging.pdf pdf/localised_treatment.pdf pdf/very_high_risk_cn1.pdf pdf/biochemical_recurrence.pdf

pdf/%.pdf: %.dot
	dot -Tpdf -o $@ $<

clean:
	rm -f pdf/*.pdf
