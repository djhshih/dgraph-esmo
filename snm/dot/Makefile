all: pdf/locoregional.pdf pdf/recurrence.pdf pdf/metastatic.pdf

pdf/%.pdf: %.dot
	dot -Tpdf -o $@ $<

clean:
	rm -f pdf/*.pdf
