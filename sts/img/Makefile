SCRIPT = ../../download_image.py

all: sts-locoregional-resectable.jpg sts-locoregional-unresectable.jpg sts-advanced-resectable.jpg sts-advanced-unresectable.jpg

sts-locoregional-resectable.jpg:
	python $(SCRIPT) https://www.annalsofoncology.org/cms/10.1016/j.annonc.2021.07.006/asset/b1b8d787-9c02-48f9-a95f-3abe82e121a1/main.assets/gr1_lrg.jpg $@

sts-locoregional-unresectable.jpg:
	python $(SCRIPT) https://www.annalsofoncology.org/cms/10.1016/j.annonc.2021.07.006/asset/e935b10b-970b-4229-ac5d-e0fa619187a1/main.assets/gr2_lrg.jpg $@

sts-advanced-resectable.jpg:
	python $(SCRIPT) https://www.annalsofoncology.org/cms/10.1016/j.annonc.2021.07.006/asset/f9b4349d-7fd9-42db-9bb6-8695027e0a2b/main.assets/gr3_lrg.jpg $@

sts-advanced-unresectable.jpg:
	python $(SCRIPT) https://www.annalsofoncology.org/cms/10.1016/j.annonc.2021.07.006/asset/df75fde6-c19e-4d97-bc7d-f6768acb84c2/main.assets/gr4_lrg.jpg $@
