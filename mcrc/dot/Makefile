all: pdf/mcrc.pdf pdf/mcrc_first_line.pdf pdf/mcrc_maintenance.pdf pdf/mcrc_second_line.pdf pdf/mcrc_third_line.pdf

pdf/%.pdf: %.dot
	dot -Tpdf -o $@ $<

clean:
	rm -f pdf/*.pdf
