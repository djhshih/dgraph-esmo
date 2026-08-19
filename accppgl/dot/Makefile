all: pdf/acc_resectable.pdf pdf/ppgl_resectable.pdf pdf/acc_advanced.pdf pdf/ppgl_advanced.pdf

pdf/%.pdf: %.dot
	dot -Tpdf -o $@ $<

clean:
	rm -f pdf/*.pdf
