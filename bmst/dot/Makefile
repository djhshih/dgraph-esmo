all: pdf/diagnostic_workup.pdf pdf/treatment_lung.pdf pdf/treatment_breast.pdf pdf/treatment_melanoma.pdf

pdf/%.pdf: %.dot
	dot -Tpdf -o $@ $<

clean:
	rm -f pdf/*.pdf
