all: pdf/diagnosis.pdf pdf/adjuvant_stage_iii.pdf pdf/adjuvant_stage_ii.pdf pdf/follow_up.pdf

pdf/%.pdf: %.dot
	dot -Tpdf -o $@ $<

clean:
	rm -f pdf/*.pdf
