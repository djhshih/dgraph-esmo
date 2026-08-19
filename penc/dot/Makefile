all: pdf/diagnosis.pdf pdf/primary_tumour.pdf pdf/inguinal_ln.pdf

pdf/%.pdf: %.dot
	dot -Tpdf -o $@ $<

clean:
	rm -f pdf/*.pdf
