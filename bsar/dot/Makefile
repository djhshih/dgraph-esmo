all: pdf/diagnostic_strategy.pdf pdf/osteosarcoma_ewing.pdf

pdf/%.pdf: %.dot
	dot -Tpdf -o $@ $<

clean:
	rm -f pdf/*.pdf
