from matplotlib import pyplot as plt
from matplotlib.colors import BoundaryNorm
from matplotlib.ticker import MaxNLocator
import numpy as np

import progress

class Model_Output:
    def __init__(self, equation, grid_size, show_prog=True):
        # Generate an array of x position and y positions for each pos we sample
        self.x, self.y = np.mgrid[slice(0, 1 + 1/grid_size[0], 1/grid_size[0]),
                                  slice(0, 1 + 1/grid_size[1], 1/grid_size[1])]
        
        # Initialise the array holding the sample values
        self.z = np.zeros((len(self.x), len(self.y)))

        # Iterate through all sample positions
        for ypos in range(grid_size[1]+1):
            for xpos in range(grid_size[0]+1):
                # Update progress bar
                if show_prog:
                    progress.print_progress(xpos + ypos*(grid_size[0]+1) +1, (grid_size[0]+1)*(grid_size[1]+1))
                # Calcuate sample position's value
                self.z[xpos,ypos] = equation(self.x[xpos,ypos], self.y[xpos, ypos])


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


def display_model_output(data, samples, axis, colourmap=np.array(['b','r','g']), dimensions=(20,11.25), show_prog=True, title=None, subtitle=None):
    
    if not subtitle is None and not title is None:
        title += '\n' + subtitle
     
    if not title is None:
        axis.set_title(title)
       
    plots = []
    
    pos_x = []
    pos_y = []
    for pos in data.get_data()[0]:
        pos_x.append(pos[0])
        pos_y.append(pos[1])
    
    types = np.array(data.get_data()[1])
    
    cmap = plt.get_cmap('coolwarm', lut=10)

    plt.ylim((0,1))
    plt.xlim((0,1))

    modelplot = axis.contourf(samples.x , samples.y , samples.z,  10, cmap=cmap)    
    dataplot = axis.scatter(pos_x, pos_y, c=colourmap[types])
    
    plots.append(modelplot)
    plots.append(dataplot)
    return plots