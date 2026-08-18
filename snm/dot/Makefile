

all: pdf/locoregional.pdf pdf/metastatic.pdf pdf/recurrence.pdf

pdf/%.pdf: %.dot
	dot -Tpdf -o $@ $<

clean:
	rm -f pdf/*.pdf

