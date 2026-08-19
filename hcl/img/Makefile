SCRIPT = ../../download_image.py

all: newly_diagnosed.jpg relapsed_refractory.jpg hcl_v.jpg

newly_diagnosed.jpg:
	python $(SCRIPT) https://www.annalsofoncology.org/cms/10.1093/annonc/mdv200/asset/f3d21d70-f3b8-43d4-b259-6b1c4e67ac00/main.assets/gr1.jpg $@

relapsed_refractory.jpg:
	python $(SCRIPT) https://www.annalsofoncology.org/cms/10.1093/annonc/mdv200/asset/852718d0-fcd5-43e7-b4b8-e04c8a7cdeb1/main.assets/gr2.jpg $@

hcl_v.jpg:
	python $(SCRIPT) https://www.annalsofoncology.org/cms/10.1093/annonc/mdv200/asset/7a60336f-d958-46b6-bb0a-5cc96c7e14ef/main.assets/gr3.jpg $@
