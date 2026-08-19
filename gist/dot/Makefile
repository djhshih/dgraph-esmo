all: pdf/gist_localised.pdf pdf/gist_advanced.pdf

pdf/%.pdf: %.dot
	dot -Tpdf -o $@ $<

clean:
	rm -f pdf/*.pdf
