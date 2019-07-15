This project clips a part of an image and applies a filter on it.

Please copy a valid tif in **data/original.tif**

There are two ways of running the container.

1) Only using docker

    The scripts will be run inside a docker container:

    ```./launch_docker.sh```

2) Using docker-compose

    ```docker-compose run gis```

    ```./install_requirements.sh```
    
    ```source env3/bin/activate```

    ```jupyter notebook```


The resulted files can be found in data folder and can be inspected with qgis.

```qgis data/original.tif data/clipped.tif data/sharpened.tif```

