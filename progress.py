current_session = 1
session_count = 1
current_step = 1
model_index = 0
model_loss = 1.0



def print_progress(graph_prog, graph_size, show_max_size=False, show_sessions=True):
    run_string = 'Step {}{}'.format(str(current_session) + ("-" if show_sessions else ''), current_step)
    model_string = 'Model {}'.format(model_index+1)
    graph_string = 'Graph Prog: {} of {}'.format(graph_prog, graph_size)
    loss_string = 'Loss {:.10f}'.format(model_loss)
    print('\r{} {} {} - {}'.format(run_string, model_string, graph_string, loss_string), end='\r')
