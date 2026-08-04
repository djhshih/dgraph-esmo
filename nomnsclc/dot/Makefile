

all: pdf/nsqnscc_ici.pdf pdf/nsqnscc_no_ici.pdf pdf/sqcc_ici.pdf pdf/sqcc_no_ici.pdf

pdf/%.pdf: %.dot
	dot -Tpdf -o $@ $<

clean:
	rm -f pdf/*.pdf

