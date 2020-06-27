import data
import graph
import fileManager
import random
import progress
import supervisor
from NNModel import NNModel as NN
import tensorflow as tf

graph_detail =12
max_runs = 1000
session_count = 1

data_type_count = 2
data_point_count = 20
data_grid_count = [6,6]

model_layers = [100,100,100,100]
model_layers2 = [100,100,100]
final_detail = 20

def random_value(x, y):
    return random.random()


def new_run():
    dirName = fileManager.get_random_directory()

    new_data = data.GridData()
    new_data.generate_data(data_type_count, data_grid_count[0], data_grid_count[1])

    models=[]
    models.append(NN(2, 1, hidden_layers=model_layers, main_activation=tf.nn.relu))
    models.append(NN(2, 1, hidden_layers=model_layers, main_activation=tf.nn.relu))

    print("New session:", dirName)
    step = 0
    progress.last_loss = 'NA'
    progress.current_step = step
    progress.max_runs = max_runs

    new_class = supervisor.TrainingClass(models, new_data, max_steps=1000, graduation_value=0.0001, start_display_size=(graph_detail, graph_detail))
    new_class.display_class_results(dirName+"/Start.png")
    
    # graph.show_data(new_data.get_data()[0], new_data.get_data()[1], model1.predict, x_parts=graph_detail, y_parts=graph_detail, save_file=dirName+"/Start.png")
    
    while new_class.do_continue_class():
        step += 1
        progress.current_step = step
        new_class.run_lesson_training(graph_size=(graph_detail, graph_detail))
        #progress.last_loss = model1.get_loss_history()[-1]
        file_name = dirName+"/Step "+str(step)+".png"
        new_class.display_class_results(file_name)
        # graph.show_data(new_data.get_data()[0], new_data.get_data()[1], model1.predict, x_parts=graph_detail, y_parts=graph_detail, save_file=file_name)
    
    # model.show_prediction_accuracy(new_data.get_data()[0], new_data.get_data()[1])
    #file_name = dirName+"/" + new_class.end_status + ".png"
    # graph.show_data(new_data.get_data()[0], new_data.get_data()[1], model1.predict, x_parts=graph_detail, y_parts=graph_detail, save_file=file_name, show_prog=False)
    print()
    print("Finished session")



#Begin Here
progress.session_count = session_count
for i in range(session_count):
    progress.current_session = i + 1
    new_run()
    print()