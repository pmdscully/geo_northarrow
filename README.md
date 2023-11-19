# geo_northarrow
Simple North arrow geometry for GIS plotting in Python. Compatible with GeoPlot, Geopandas, and libraries built on Matplotlib.

![image](https://github.com/pmdscully/geo_northarrow/assets/3637403/4b31b277-1e9b-4af7-8da2-5fba1cc2d250)

## Requirements:
- shapely (via pip) <=2.0.1 or >2.0.1. (only requires `Polygon` class)
- geopandas (often requires install via conda)
- numpy
- matplotlib

## Installation:
(Use `!pip` for notebook installations, Jupyter, Colab, etc.)
```
pip install git+https://github.com/pmdscully/geo_northarrow.git
```
(See example install & use [Google Colab notebook here](https://colab.research.google.com/drive/1J94KGiHZhkXfIURpqUKjRnRs57tZcJPF?usp=sharing))

## Example 1 Geopandas Plotting code:
See original example: https://geopandas.org/en/stable/docs/user_guide/mapping.html
```python
import geopandas
import geodatasets
from geo_northarrow import add_north_arrow

chicago = geopandas.read_file(geodatasets.get_path("geoda.chicago_commpop"))
groceries = geopandas.read_file(geodatasets.get_path("geoda.groceries"))
display(chicago.head())
ax = chicago.plot(column="POP2010");

add_north_arrow(ax, scale=.75, xlim_pos=.9025, ylim_pos=.965, color='#000', text_scaler=4, text_yT=-1.25)
```
##### Output:
![image](https://github.com/pmdscully/geo_northarrow/assets/3637403/091d1f15-5638-4034-815f-dc6ef334a0a5)




## Example 2 code:
```python
import matplotlib.pyplot as plt
import geopandas

from geo_northarrow import add_north_arrow

fig, ax = plt.subplots(figsize=(2,3))
_ = ax.set_xlim(0,100) #Define axis limits.   Either manually or by plotting data - e.g. ax = gdf.plot(ax=ax)
_ = ax.set_ylim(0,100) # NB: add_north_arrow() will use the axis limits to define its default relative position and scale.

#...
#... your mapping code...     
#...
add_north_arrow(ax, scale=1.75, xlim_pos=.9025, ylim_pos=.165, color='#000', text_scaler=4, text_yT=-1.25)

# 
# -- Just for the sample plots.
ax.set_facecolor((1.0, 0.47, 0.42))
```
##### Output:
![image](https://github.com/pmdscully/geo_northarrow/assets/3637403/c9958129-97f1-4853-8098-b601b657e2d1)



## `add_north_arrow` Function Arguments:
```
- ax,           - your Matplotlib/ Geopandas axes object.
- scale=1,      - Scale of the Arrow and 'N' character.
- xlim_pos=.9,  - Relative position on the x-axis of the plot. (left:0 to right:1.0)
- ylim_pos=.8,  - Relative position on the y-axis of the plot. (bottom:0 to top:1.0)
- xT=None,      - Absolute transform position on x-axis (Alternative to xlim_pos). Probably will not require.
- yT=None,      - Absolute transform position on y-axis (Alternative to ylim_pos). Probably will not require.
- color='k',    - Color of the polygon (arrow and 'N' character), any matplotlib color scheme (i.e. #000 to #fff and matplotlib color naming).
- text_scaler=1.0,   - Secondary scale multiplier for the 'N' character, for customized sizing.
- text_yT=1.0        - Fine tuning of the y-axis position for the 'N' character, for customized positioning.
```

## How it works:
The function just plots a polygon into the matplotlib axes. The north arrow is composed of 3 sub-polygons (left triangle, right triangle and a serif 'N' character as a polygon) and default layer-ordering (z-order) is used. 

- To make things simpler, **the function attempts to scale and transform** the north arrow (with N character) according to a benchmarked-relative size, relative to the axis lengths of your GIS data plot. Therefore, call `add_north_arrow()` **after plotting your main map data content** (or after defining the axis limits - `ax.set_xlim(0,1)`/ `ax.set_ylim(0,1)`).
- However, the `north_arrow` is only suitable for maps with `north-south axis` that is identical to the `matplotlib yaxis`, as the orientation for north is not extracted from map data.
- It is isolated from other plot artefacts, so easy to add alongside `scalebar` (e.g. see [https://geopandas.org/en/stable/gallery/matplotlib_scalebar.html](https://geopandas.org/en/stable/gallery/matplotlib_scalebar.html))

# LIMITATIONS / FUTURE WORK:
1. **No attempt is made to determine the north orientation from your map or data.** Therefore this `north_arrow` is only suitable for maps with `north-south axis` that is identical to the `matplotlib yaxis`. In future, add an angle input to rotate the arrow in terms of north orientation.
2. Replace `shapely` and `geopandas` depedencies with pure [`matplotlib` Polygon plotting](https://stackoverflow.com/a/26935798/1910555).
