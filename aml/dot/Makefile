all: pdf/first_line_eligible.pdf pdf/first_line_ineligible.pdf pdf/relapsed_refractory.pdf pdf/apl_first_line.pdf pdf/apl_relapsed_refractory.pdf

pdf/%.pdf: %.dot
	dot -Tpdf -o $@ $<

clean:
	rm -f pdf/*.pdf
