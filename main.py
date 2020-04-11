import data
import graph

new_data = data.Data()
new_data.generate_data(2, 10)

graph.DataGraph.show_data(new_data.get_data())