all: pdf/cytogenetics.pdf pdf/higher_risk.pdf pdf/lower_risk.pdf

pdf/%.pdf: %.dot
	dot -Tpdf -o $@ $<

clean:
	rm -f pdf/*.pdf
