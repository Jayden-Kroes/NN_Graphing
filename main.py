import data
import graph
import fileManager
import random
from NNModel import NNModel as NN

dirName = fileManager.get_random_directory()
print("New project:", dirName)

new_data = data.Data()
new_data.generate_data(2, 20)
# print(new_data.positions)
# print(new_data.types)

graph_detail = 20

def randomClass(x, y):
    return random.random()

model = NN(2, 1, hidden_layers=[32, 32, 32])

new_graph = graph.DataGraph()
new_graph.show_data(new_data.get_data()[0], new_data.get_data()[1], model.predict, x_parts=graph_detail, y_parts=graph_detail, save_file=dirName+"/Start.png")
for i in range(1000):
    print()
    print("Run", i)
    model.teach(new_data.get_data()[0], new_data.get_data()[1])
    print("Loss -", model.get_loss_history()[i][-1])
    file_name = dirName+"/Step "+str(i+1)+" - "+"MSE {:.6f}".format(float(model.get_loss_history()[i][-1])) + ".png"
    # print(file_name)
    new_graph.show_data(new_data.get_data()[0], new_data.get_data()[1], model.predict, x_parts=graph_detail, y_parts=graph_detail, save_file=file_name)
    # model.show_prediction_accuracy(new_data.get_data()[0], new_data.get_data()[1])
# new_graph.show_data(new_data.get_data()[0], new_data.get_data()[1], model.predict, x_parts=10, y_parts=10)
model.show_prediction_accuracy(new_data.get_data()[0], new_data.get_data()[1])
# f = open(dirName + "/Loss.txt", 'w')
# f.writelines(str(s for s in model.get_loss_history()[:][-1]))
# f.close()

print("Finished", dirName)