

all: pdf/parotid.pdf pdf/sgc.pdf pdf/sublingual.pdf pdf/submandibular.pdf

pdf/%.pdf: %.dot
	dot -Tpdf -o $@ $<

clean:
	rm -f pdf/*.pdf

