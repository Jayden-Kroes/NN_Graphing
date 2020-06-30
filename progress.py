current_session = 1
session_count = 1
current_step = 1
model_index = 0
model_loss = 1.0

#new_line_per_model = True
L_Newline_per_model = "nl model"
L_Newline_per_step = "nl step"
L_Newline_per_class = "nl class"
linetype = L_Newline_per_class

#TODO when progress line length changes, need to delete stuff after


def print_progress(graph_prog, graph_size, show_max_size=False, show_sessions=True):
    run_string = 'Step {}{}'.format(str(current_session) + ("-" if show_sessions else ''), current_step)
    model_string = 'Model {}'.format(model_index+1)
    graph_string = 'Graph Prog: {} of {}'.format(graph_prog, graph_size)
    loss_string = 'Loss {:.10f}'.format(model_loss)
    print('\r{} {} {} - {}'.format(run_string, model_string, graph_string, loss_string), end='\r')
    
def new_model():
    if linetype == L_Newline_per_model:
        print()

def new_step():
    if linetype == L_Newline_per_model or linetype == L_Newline_per_step:
        print()

def new_run():
    print()

