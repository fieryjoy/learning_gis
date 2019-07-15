.PHONY: remove_pycache
remove_pycache:
	find . -name "*.pyc" -delete
	find . -name __pycache__ -type d -empty -delete
	rm -rf env3

clean: remove_pycache

requirements:
	./install_requirements.sh

build: requirements

run:
	python3 clipping.py
	python3 sharpening.py

show: run
	gdalinfo data/original.tif
	gdalinfo data/clipped.tif
	gdalinfo data/sharpened.tif
