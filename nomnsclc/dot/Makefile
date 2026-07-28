

all: pdf/nsqnscc_ici.pdf pdf/nsqnscc-no-ici.pdf pdf/sqcc-ici.pdf pdf/sqcc-no-ici.pdf

pdf/%.pdf: %.dot
	dot -Tpdf -o $@ $<

clean:
	rm -f pdf/*.pdf

