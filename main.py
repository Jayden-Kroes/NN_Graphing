import data
import graph
import fileManager
import random
import progress
import supervisor
from NNModel import NNModel as NN

graph_detail = 16
max_runs = 1000
session_count = 2

data_type_count = 2
data_point_count = 20
data_grid_count = [8,8]

model_layers = [100,100,100,100]
final_detail = 35

def randomClass(x, y):
    return random.random()

def new_run():
    # new_data = data.Data()
    # new_data.generate_data(data_type_count, data_point_count)
    new_data = data.GridData()
    new_data.generate_data(data_type_count, data_grid_count[0], data_grid_count[1])

    model = NN(2, 1, hidden_layers=model_layers)
    teacher = supervisor.Supervisor(max_steps=1000, graduation_value=0.0001)#/(data_grid_count[0]*data_grid_count[1]))

    dirName = fileManager.get_random_directory()
    print("New session:", dirName)

    graph.show_data(new_data.get_data()[0], new_data.get_data()[1], model.predict, x_parts=graph_detail, y_parts=graph_detail, save_file=dirName+"/Start.png")
    progress.max_runs = max_runs

    progress.last_loss = 'NA'
    previous_loss = 1.0

    step = 0
    while teacher.do_continue(previous_loss):
        step += 1
    # for i in range(max_runs):
        progress.current_run = step
        model.teach(new_data.get_data()[0], new_data.get_data()[1])
        previous_loss = model.get_loss_history()[-1][-1]
        progress.last_loss = previous_loss
        file_name = dirName+"/Step "+str(step)+" - "+"MSE {:.4f}".format(float(previous_loss)) + ".png"
        graph.show_data(new_data.get_data()[0], new_data.get_data()[1], model.predict, x_parts=graph_detail, y_parts=graph_detail, save_file=file_name)
    
    # model.show_prediction_accuracy(new_data.get_data()[0], new_data.get_data()[1])
    file_name = dirName+"/" + teacher.end_status + " - "+"MSE {:.4f}".format(float(previous_loss)) + ".png"
    graph.show_data(new_data.get_data()[0], new_data.get_data()[1], model.predict, x_parts=graph_detail, y_parts=graph_detail, save_file=file_name, show_prog=False)
    print("Finished session")

progress.session_count = session_count
for i in range(session_count):
    progress.current_session = i + 1
    new_run()
    print()