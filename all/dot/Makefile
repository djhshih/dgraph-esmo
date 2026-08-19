all: pdf/newly_diagnosed.pdf pdf/relapsed_refractory.pdf

pdf/%.pdf: %.dot
	dot -Tpdf -o $@ $<

clean:
	rm -f pdf/*.pdf
