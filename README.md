# geo_northarrow
Simple North arrow geometry for GIS plotting in python (GeoPlot, Geopandas, etc.)

![image](https://github.com/pmdscully/geo_northarrow/assets/3637403/4b31b277-1e9b-4af7-8da2-5fba1cc2d250)

## Requirements:
- shapely (via pip) <=2.0.1 or >2.0.1. (only requires `Polygon` class)
- geopandas (often requires install via conda)
- numpy
- matplotlib

## Example code:
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
