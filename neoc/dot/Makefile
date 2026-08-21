all: pdf/gct_dysgerminoma.pdf pdf/gct_immature_teratoma.pdf pdf/gct_yolk_sac.pdf pdf/scst_granulosa.pdf pdf/scst_sertoli_leydig.pdf pdf/sccoht.pdf

pdf/%.pdf: %.dot
	dot -Tpdf -o $@ $<

clean:
	rm -f pdf/*.pdf
