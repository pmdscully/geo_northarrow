import matplotlib.pyplot as plt
import numpy as np
import geopandas
from shapely.geometry import Polygon
from matplotlib.patches import Rectangle

def add_north_arrow(ax, scale=1, xlim_pos=.9, ylim_pos=.8, xT=None, yT=None, color='k', text_scaler=1.0, text_yT=1.0, background=False, bg_color='white', bg_padding=0.5):
    def t_s(xy,xT,yT,s): return (xT+(xy[0]*s),yT+(xy[1]*s))
    def get_default_scale_factor(ax):
        xax_diff = abs(max(ax.get_xlim())-min(ax.get_xlim()))
        yax_diff = abs(max(ax.get_ylim())-min(ax.get_ylim()))
        baseline_lim = 45
        return (sum([xax_diff,yax_diff])/2)/baseline_lim
    def _anchor_pos(_lim, lim_scale): return min(_lim)+(abs(_lim[0]-_lim[1])*lim_scale)
    xT = _anchor_pos(ax.get_xlim(), xlim_pos) if not xT else xT
    yT = _anchor_pos(ax.get_ylim(), ylim_pos) if not yT else yT
    def get_n(scale, text_yT):
        def n_char():
            l = (3.248,5.059,3.248,5.019,3.260,5.019,3.316,5.007,3.339,4.950,3.339,4.479,3.315,4.425,3.260,4.414,3.248,4.414,3.248,4.374,3.423,4.374,3.767,4.904,3.767,4.479,3.743,4.425,3.688,4.414,3.676,4.414,3.676,4.374,3.917,4.374,3.917,4.414,3.904,4.414,3.849,4.426,3.826,4.483,3.826,5.059,3.757,5.059,3.397,4.506,3.397,4.950,3.421,5.007,3.476,5.019,3.489,5.019,3.489,5.059)
            p = []
            t = []
            for i,v in enumerate(l):
                if i%2==0:
                    t += [v]
                elif i%1==0:
                    t += [-v]
                    p += [t]
                    t = []
            return p
        def n_char_TS(points, xTn=0, yTn=0):
            return [ ( (x+xTn) , (y+yTn) ) for (x,y) in points ]
        points = n_char()
        x = np.array(points)[:,0].copy()
        y = np.array(points)[:,1].copy()
        xTn = float((abs(x.max()-x.min())/2)+x.min())
        yTn = float((abs(y.max()-y.min())/2)+y.min())
        pointsZeroed = n_char_TS(points, -xTn, -yTn)
        pointsScaled = [t_s(t,xT=0,yT=0,s=scale) for t in pointsZeroed]
        pointsT = [t_s(t,xT=0,yT=text_yT,s=1) for t in pointsScaled]
        return pointsT
    n_points = get_n(text_scaler, text_yT)
    default_scale = get_default_scale_factor(ax)
    scale = default_scale*scale
    a = [(0, 5), (0, 1), (2, 0)]
    b = [(0, 5), (0, 1), (-2, 0)]
    a = [t_s(t,xT,yT,scale) for t in a]
    b = [t_s(t,xT,yT,scale) for t in b]
    n_points = [t_s(t,xT,yT,scale) for t in n_points]

     # Adicionando um "box" branco em torno da seta
    if background:
        padding = bg_padding * scale
        x_min = min([x for x, y in a + b + n_points]) - padding
        x_max = max([x for x, y in a + b + n_points]) + padding
        y_min = min([y for x, y in a + b + n_points]) - padding
        y_max = max([y for x, y in a + b + n_points]) + padding
        
        rect = Rectangle((x_min, y_min), x_max - x_min, y_max - y_min, facecolor=bg_color, edgecolor='none')
        ax.add_patch(rect)


    p1 = geopandas.GeoDataFrame([1], geometry=[Polygon(a)])
    p2 = geopandas.GeoDataFrame([1], geometry=[Polygon(b)])
    p3 = geopandas.GeoDataFrame([1], geometry=[Polygon(n_points)])
    ax = p1.plot(fc='none', ec=color, lw=2, ax=ax)
    p2.plot(fc=color, ec=color, lw=2, ax=ax)
    p3.plot(fc=color, ax=ax)

if __name__ == "__main__":
  fig, ax = plt.subplots(figsize=(2,3))
  _ = ax.set_xlim(0,100) #Define axis limits (either by plotting data or manually).
  _ = ax.set_ylim(0,100) # NB: add_north_arrow() will use the axis limits to define its default relative position and scale.
  
  #...
  #... your mapping code...
  #...
  add_north_arrow(ax, scale=1.75, xlim_pos=.9025, ylim_pos=.165, color='#000', text_scaler=4, text_yT=-1.25, background=True)
  
  # 
  # -- Just for the sample plots.
  ax.set_facecolor((1.0, 0.47, 0.42))