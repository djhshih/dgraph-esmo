all: pdf/gc.pdf pdf/gc_first_line.pdf pdf/gc_maintenance.pdf pdf/gc_second_line.pdf pdf/gc_third_line.pdf

pdf/%.pdf: %.dot
	dot -Tpdf -o $@ $<

clean:
	rm -f pdf/*.pdf
