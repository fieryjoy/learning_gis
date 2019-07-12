This project clips a part of an image and applies a filter on it.

Please copy a valid tif in **data/original.tif**

The scripts will be run inside a docker container:

```./launch_docker.sh```

The resulted files can be found in data folder and can be inspected with qgis.

```qgis data/original.tif data/clipped.tif data/sharpened.tif```

