import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation
from mpl_toolkits.axes_grid1 import make_axes_locatable


fig, ax = plt.subplots()
divider = make_axes_locatable(ax)
cax = divider.append_axes('right', size='5%', pad=0.05)

text = ax.text(0,0,0)

def update(iternum):
    ax.clear()
    ax.set_title(iternum)
    curVals  = np.random.rand(100).reshape(10, 10)
    
    vmax     = np.max(curVals)
    vmin     = np.min(curVals)
    #print(vmax)
    levels   = np.linspace(vmin, vmax, 200, endpoint = True)
    p = ax.contourf(curVals, vmax=vmax, vmin=vmin, levels=levels)
    fig.colorbar(p, cax=cax) # Colorbar does not update
    
    

ani = animation.FuncAnimation(fig, update, frames=10, interval=500, blit=False,
                              repeat_delay=2000)
plt.show()
