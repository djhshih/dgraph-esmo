

all: pdf/mel_local.pdf pdf/mel_st3_or_st4.pdf pdf/mel_itm.pdf pdf/mel_adv_st3_or_st4.pdf pdf/mel_mbm.pdf pdf/mel_follow_up.pdf

pdf/%.pdf: %.dot
	dot -Tpdf -o $@ $<

clean:
	rm -f pdf/*.pdf

