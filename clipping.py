import rasterio
from rasterio.mask import mask
from shapely.geometry import box
import geopandas as gpd
import pycrs


def getFeatures(gdf):
    import json
    return [json.loads(gdf.to_json())['features'][0]['geometry']]

# Geographical coordinates
# TODO: get these from original image using rasterio commands
#minx = int(os.environ['COORD_MINX'])
#miny = int(os.environ['COORD_MINY'])
#maxx = int(os.environ['COORD_MAXX'])
#maxy = int(os.environ['COORD_MAXY'])
#epsg = int(os.environ['EPSG'])

with rasterio.open("./data/original.tif") as data:
    crs = data.crs
    bounds = data.bounds
    bbox = box(int(bounds.left), int(bounds.bottom), int(bounds.right), int(bounds.top))
    geo = gpd.GeoDataFrame({'geometry': bbox}, index=[0], crs=crs)

    geo = geo.to_crs(crs=data.crs.data)
    coords = getFeatures(geo)

#    import pdb; pdb.set_trace()
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
