from matplotlib import pyplot as plt
from matplotlib.colors import BoundaryNorm
from matplotlib.ticker import MaxNLocator
import numpy as np

class DataGraph:
    def __init__():
        pass

    def show_data(data, equation, x_parts = 10, y_parts=10, colourmap=np.array(['r','b','g'])):
        #plt.contour()
        data_x = []
        data_y = []
        data_v = []
        for xyv in data:
            data_x.append(xyv[0][0])
            data_y.append(xyv[0][1])
            data_v.append(int(xyv[1]))

        
        data_v = np.array(data_v)


        # plt.show()

        y, x = np.mgrid[slice(0, 1 + 1/y_parts, 1/y_parts),
                slice(0, 1 + 1/x_parts, 1/x_parts)]

        z = np.zeros((len(y), len(x)))
        for y_ind in range(y_parts+1):
            for x_ind in range(x_parts+1):
                z[y_ind, x_ind] = equation(x_ind, y_ind)
                #print(x_ind, y_ind, z[y_ind, x_ind])
    

        # print(x)
        # print(y)
        # print(z)

        levels = MaxNLocator(nbins=15).tick_values(z.min(), z.max())
        
        cmap = plt.get_cmap('PiYG')
        norm = BoundaryNorm(levels, ncolors=cmap.N, clip=True)

        plt.ylim((0,1))
        plt.xlim((0,1))
        plt.contourf(x , y , z, levels=levels, cmap=cmap)
        plt.scatter(data_x, data_y, c=colourmap[data_v])

        plt.show()
