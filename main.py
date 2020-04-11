import data
import graph
import random

new_data = data.Data()
new_data.generate_data(2, 10)

def randomClass(x, y):
    return random.random()

graph.DataGraph.show_data(new_data.get_data(), randomClass, x_parts=100, y_parts=100)