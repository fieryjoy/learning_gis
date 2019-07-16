This project clips a part of an image and applies a filter on it.

Please copy a valid tif in **data/original.tif**

Using docker-compose

    ```docker-compose run gis```
    
    ```cd scripts```
    
    ```./install_requirements.sh```
    
    ```source env3/bin/activate```

    ```jupyter notebook```


The resulted files can be found in data folder and can be inspected with qgis.

```qgis data/original.tif data/clipped.tif data/sharpened.tif```

