.PHONY: remove_pycache
remove_pycache:
	find . -name "*.pyc" -delete
	find . -name __pycache__ -type d -empty -delete

clean: remove_pycache

requirements:
	pip3 install -U -r requirements.txt

build: requirements

run:
	python3 clipping.py
	python3 sharpening.py

show: run
	gdalinfo data/original.tif
	gdalinfo data/clipped.tif
	gdalinfo data/sharpened.tif
