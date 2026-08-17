
indir = ../dot

all: mel_local.dg mel_st3_or_st4.dg mel_itm.dg mel_adv_st3_or_st4.dg mel_mbm.dg mel_follow_up.dg
	
%.dg: $(indir)/%.dot
	dot2dg.py -o $@ $<

clean:
	rm -f *.dg

 