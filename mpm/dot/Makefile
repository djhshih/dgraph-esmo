

all: pdf/inoperable.pdf pdf/multimodality.pdf pdf/treatment-intent.pdf

pdf/%.pdf: %.dot
	dot -Tpdf -o $@ $<

clean:
	rm -f pdf/*.pdf

