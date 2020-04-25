from matplotlib import pyplot as plt
from matplotlib.colors import BoundaryNorm
from matplotlib.ticker import MaxNLocator
import numpy as np

import progress


def show_data(positions, types, equation, x_parts = 10, y_parts=10, colourmap=np.array(['b','r','g']), save_file=None, dimensions=(20,11.25), show_prog=True):
    pos_x = []
    pos_y = []
    for pos in positions:
        pos_x.append(pos[0])
        pos_y.append(pos[1])

    
    types = np.array(types)

    y, x = np.mgrid[slice(0, 1 + 1/y_parts, 1/y_parts),
            slice(0, 1 + 1/x_parts, 1/x_parts)]

    z = np.zeros((len(y), len(x)))
    for y_ind in range(y_parts+1):
        for x_ind in range(x_parts+1):
            # print("\rGenerating graph", , 'of', , end='\r')
            if show_prog:
                progress.print_progress(x_ind + y_ind*(x_parts+1) + 1, (x_parts+1) * (y_parts+1))
            z[x_ind, y_ind] = equation(x[x_ind,y_ind], y[x_ind, y_ind])
            
    levels = MaxNLocator(nbins=10).tick_values(0, 1)
    
    cmap = plt.get_cmap('coolwarm', lut=10)
    norm = BoundaryNorm(levels, ncolors=cmap.N, clip=True)

    plt.ylim((0,1))
    plt.xlim((0,1))
    modelplot = plt.contourf(x , y , z, levels=levels, cmap=cmap)
    # modelplot = plt.pcolormesh(x, y, z, cmap=cmap, norm=norm)
    dataplot = plt.scatter(pos_x, pos_y, c=colourmap[types])

    plt.colorbar(modelplot)

    # plt.tight_layout()

    # plt.draw()        
    # plt.show(block=False)
    # plt.show()
    if save_file is None:
        save_file = "plot.png"
    plt.savefig(save_file, dpi=(225))

    plt.clf()

