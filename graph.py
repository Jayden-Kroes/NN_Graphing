from matplotlib import pyplot as plt
from matplotlib.colors import BoundaryNorm
from matplotlib.ticker import MaxNLocator
import numpy as np

import progress

class Model_Output:
    def __init__(self, equation, grid_size, show_prog=True):
        #x, y, z, cmap
        # Generate an array of x position and y positions for each pos we sample
        self.x, self.y = np.mgrid[slice(0, 1 + 1/grid_size[0], 1/grid_size[0]),
                                  slice(0, 1 + 1/grid_size[1], 1/grid_size[1])]

        
        
        # Initialise the array holding the sample values
        self.z = np.zeros((len(self.x), len(self.y)))
        #self.z = np.zeros((len(positions)))
        # Iterate through all sample positions
        for ypos in range(grid_size[1]+1):
            for xpos in range(grid_size[0]+1):
        #for p in range(len(positions)):
                # Update progress bar
                if show_prog:
                    progress.print_progress(xpos + ypos*(grid_size[0]+1) +1, (grid_size[0]+1)*(grid_size[1]+1))
                    #progress.print_progress(p+1, len(positions))
                # Calcuate sample position's value
                self.z[xpos,ypos] = equation(self.x[xpos,ypos], self.y[xpos, ypos])
                #self.z[p] = equation(self.x[p], self.y[p])




def save_figure(plots = [], save_file=None, title=None):
    plt.clf()
    if title == None:
        plt.title = title
    else:
        plt.title(title)
    if save_file is None:
        save_file = "plot.png"
    plt.savefig(save_file, dpi=(225))

    plt.clf()

def plot_model_output(positions, types, equation, axis, x_parts = 10, y_parts=10, colourmap=np.array(['b','r','g']), dimensions=(20,11.25), show_prog=True, title=None):
    plots = []
    
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
            
    #levels = MaxNLocator(nbins=10).tick_values(0, 1)
    
    cmap = plt.get_cmap('coolwarm', lut=10)
    #norm = BoundaryNorm(levels, ncolors=cmap.N, clip=True)

    plt.ylim((0,1))
    plt.xlim((0,1))
    #modelplot = self.figure_axes[subplot_index].contourf(x , y , z, 10, cmap=cmap)

    modelplot = axis.contourf(x , y , z, 10, cmap=cmap)
    axis.set_title(title)
    # modelplot = plt.pcolormesh(x, y, z, cmap=cmap, norm=norm)
    dataplot = axis.scatter(pos_x, pos_y, c=colourmap[types])

    # plt.colorbar(modelplot)

    # plt.tight_layout()

    # plt.draw()        
    # plt.show(block=False)
    # plt.show()
    plots.append(modelplot)
    plots.append(dataplot)
    return plots



def display_model_output(data, samples, axis, colourmap=np.array(['b','r','g']), dimensions=(20,11.25), show_prog=True, title=None):
    plots = []
    
    pos_x = []
    pos_y = []
    for pos in data.get_data()[0]:
        pos_x.append(pos[0])
        pos_y.append(pos[1])

    
    types = np.array(data.get_data()[1])
            
    #levels = MaxNLocator(nbins=10).tick_values(0, 1)
    
    cmap = plt.get_cmap('coolwarm', lut=10)
    #norm = BoundaryNorm(levels, ncolors=cmap.N, clip=True)

    plt.ylim((0,1))
    plt.xlim((0,1))
    #modelplot = self.figure_axes[subplot_index].contourf(x , y , z, 10, cmap=cmap)

    modelplot = axis.contourf(samples.x , samples.y , samples.z,  10, cmap=cmap)
    axis.set_title(title)
    # modelplot = plt.pcolormesh(x, y, z, cmap=cmap, norm=norm)
    dataplot = axis.scatter(pos_x, pos_y, c=colourmap[types])

    # plt.colorbar(modelplot)

    # plt.tight_layout()

    # plt.draw()        
    # plt.show(block=False)
    # plt.show()
    plots.append(modelplot)
    plots.append(dataplot)
    return plots