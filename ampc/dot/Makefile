all: pdf/denovo_mcspc.pdf pdf/relapsed_mcspc.pdf pdf/high_risk_nmcrpc.pdf pdf/mcrpc_no_genetic.pdf pdf/mcrpc_genetic.pdf

pdf/%.pdf: %.dot
	dot -Tpdf -o $@ $<

clean:
	rm -f pdf/*.pdf
