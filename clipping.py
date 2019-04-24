import rasterio
from rasterio.mask import mask
from shapely.geometry import box
import geopandas as gpd
from fiona.crs import from_epsg
import pycrs


def getFeatures(gdf):
    import json
    return [json.loads(gdf.to_json())['features'][0]['geometry']]


minx, miny, maxx, maxy = 12.30, 45.45, 12.37, 45.41
bbox = box(minx, miny, maxx, maxy)

geo = gpd.GeoDataFrame({'geometry': bbox}, index=[0], crs=from_epsg(4326))

with rasterio.open("./data/original.tif") as data:
    geo = geo.to_crs(crs=data.crs.data)
    coords = getFeatures(geo)

    out_img, out_transform = mask(dataset=data, shapes=coords, crop=True)

    out_meta = data.meta.copy()
    epsg_code = int(data.crs.data['init'][5:])

    out_meta.update({
        "driver": "GTiff",
        "height": out_img.shape[1],
        "wight": out_img.shape[2],
        "transform": out_transform,
        "crs": pycrs.parse.from_epsg_code(epsg_code).to_proj4()
    })

with rasterio.open("./data/clipped.tif", "w", **out_meta) as dest:
    dest.write(out_img)
