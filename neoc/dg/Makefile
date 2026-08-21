indir = ../dot

all: gct_dysgerminoma.dg gct_immature_teratoma.dg gct_yolk_sac.dg scst_granulosa.dg scst_sertoli_leydig.dg sccoht.dg

%.dg: $(indir)/%.dot
	dot2dg.py -o $@ $<

clean:
	rm -f *.dg
