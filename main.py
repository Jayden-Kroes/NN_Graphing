import data
import graph
import fileManager
import random
import progress
import supervisor
from NNModel import NNModel as NN
import tensorflow as tf

graph_detail = 10
max_runs = 1000
session_count = 1

data_type_count = 2
data_point_count = 20
data_grid_count = [5,5]

model_layers = [100,100,100,100]
final_detail = 20

def randomClass(x, y):
    return random.random()

def new_run():
    dirName = fileManager.get_random_directory()
    print("New session:", dirName)

    new_data = data.GridData()
    new_data.generate_data(data_type_count, data_grid_count[0], data_grid_count[1])

    model1 = NN(2, 1, hidden_layers=model_layers, main_activation=tf.nn.relu)
    # model1.save_weights(dirName + "/data")
    # model2 = NN(2, 1, hidden_layers=model_layers, main_activation=tf.nn.sigmoid)
    # model2.load_weights(dirName + "/data")

    new_class = supervisor.TrainingClass([model1], new_data, max_steps=1000, graduation_value=0.0001)


    graph.show_data(new_data.get_data()[0], new_data.get_data()[1], model1.predict, x_parts=graph_detail, y_parts=graph_detail, save_file=dirName+"/Start.png")
    progress.max_runs = max_runs

    progress.last_loss = 'NA'
    previous_loss = 1.0

    step = 0
    while new_class.continue_class():
        step += 1
        progress.current_run = step
        new_class.begin_new_lesson()
        previous_loss = model1.get_loss_history()[-1]
        progress.last_loss = previous_loss
        file_name = dirName+"/Step "+str(step)+" - "+"MSE {:.4f}".format(float(previous_loss)) + ".png"
        
        graph.show_data(new_data.get_data()[0], new_data.get_data()[1], model1.predict, x_parts=graph_detail, y_parts=graph_detail, save_file=file_name)
    
    # model.show_prediction_accuracy(new_data.get_data()[0], new_data.get_data()[1])
    file_name = dirName+"/" + new_class.end_status + " - "+"MSE {:.4f}".format(float(previous_loss)) + ".png"
    # graph.show_data(new_data.get_data()[0], new_data.get_data()[1], model1.predict, x_parts=graph_detail, y_parts=graph_detail, save_file=file_name, show_prog=False)
    print("Finished session")

progress.session_count = session_count
for i in range(session_count):
    progress.current_session = i + 1
    new_run()
    print()