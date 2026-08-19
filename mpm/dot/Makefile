all: pdf/staging.pdf pdf/treatment_intent.pdf pdf/multimodality.pdf pdf/inoperable.pdf

pdf/%.pdf: %.dot
	dot -Tpdf -o $@ $<

clean:
	rm -f pdf/*.pdf
