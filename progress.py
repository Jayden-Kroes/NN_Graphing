current_session = 1
session_count = 1
current_run = 1
max_runs = 1
last_loss = 1.0



def print_progress(graph_prog, graph_size, show_max_size=False, show_sessions=False):
    session_string = 'Session {} of {}'.format(current_session, session_count)
    run_string = 'Step {}'.format(current_run) + (' of {}'.format(max_runs) if show_max_size else '')
    graph_string = 'Graph Prog: {} of {}'.format(graph_prog, graph_size)
    loss_string = 'Loss {:.10f}'.format(last_loss)
    print('\r' + ('{} '.format(session_string) if show_sessions else '') + '{} {} - {}'.format(run_string, graph_string, loss_string), end='\r')
