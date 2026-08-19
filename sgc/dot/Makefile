all: pdf/sgc.pdf pdf/parotid.pdf pdf/sublingual.pdf pdf/submandibular.pdf

pdf/%.pdf: %.dot
	dot -Tpdf -o $@ $<

clean:
	rm -f pdf/*.pdf
