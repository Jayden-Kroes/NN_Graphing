from matplotlib import pyplot as plt

class DataGraph:
    def __init__():
        pass

    def show_data(data, model=None, x_parts = 10, y_parts=10):
        #plt.contour()
        x = []
        y = []
        v = []
        for xyv in data:
            x.append(xyv[0][0])
            y.append(xyv[0][1])
            v.append(xyv[1])

        plt.scatter(x, y)
        plt.show()
