SCRIPT = ../../download_image.py

all: seminoma.jpg non-seminoma.jpg

seminoma.jpg:
	python $(SCRIPT) https://www.annalsofoncology.org/cms/10.1016/j.annonc.2022.01.002/asset/adb14f6b-b469-4f14-a6c7-35ee7c96fb4a/main.assets/gr1_lrg.jpg $@

non-seminoma.jpg:
	python $(SCRIPT) https://www.annalsofoncology.org/cms/10.1016/j.annonc.2022.01.002/asset/1eb0a9eb-bef5-45b9-8378-319afb2bc5df/main.assets/gr2_lrg.jpg $@
