all: pdf/pc_sus.pdf pdf/pc_local.pdf pdf/pc_met.pdf pdf/pc_met_precision.pdf

pdf/%.pdf: %.dot
	dot -Tpdf -o $@ $<

clean:
	rm -f pdf/*.pdf
