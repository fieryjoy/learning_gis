import rasterio
from scipy import ndimage

with rasterio.open("./data/clipped.tif") as data:
    f = data.read().astype('f4')

    blurred_f = ndimage.gaussian_filter(f, 3)
    filter_blurred_f = ndimage.gaussian_filter(blurred_f, 1)

    alpha = 30
    sharpened = blurred_f + alpha * (blurred_f - filter_blurred_f)

    out_meta = data.meta.copy()
    out_meta.update({
        "driver": "GTiff",
        "height": sharpened.shape[1],
        "wight": sharpened.shape[2],
        "dtype": sharpened.dtype,
    })

with rasterio.open("./data/sharpened.tif", "w", **out_meta) as dest:
    dest.write(sharpened)

