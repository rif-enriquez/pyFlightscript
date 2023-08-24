from .utils import *    

def start_solver(script_filepath):
    """
    Writes specific lines to 'script_filepath' to start the solver.
    
    :param script_filepath: Path to the script file.

    Example usage:
    start_solver('path_to_script.txt')
    """
    
    lines = [
        "#************************************************************************",
        "#********* Run the solver ***********************************************",
        "#************************************************************************",
        "",
        "START_SOLVER"
    ]
    
    write_lines_to_file(script_filepath, lines)
    return

def solver_clear(script_filepath):
    """
    Writes specific lines to 'script_filepath' to clear the existing solution.
    
    :param script_filepath: Path to the script file.

    Example usage:
    solver_clear('path_to_script.txt')
    """
    
    lines = [
        "#************************************************************************",
        "#********* Clear the existing solution **********************************",
        "#************************************************************************",
        "",
        "SOLVER_CLEAR"
    ]
    
    write_lines_to_file(script_filepath, lines)
    return

def close_flightstream(script_filepath):
    """
    Writes specific lines to 'script_filepath' to close FlightStream and exit.

    :param script_filepath: Path to the script file.

    Example usage:
        close_flightstream('path_to_script.txt')
    """
    
    lines = [
        "#************************************************************************",
        "#****************** Close FlightStream and exit *************************",
        "#************************************************************************",
        "",
        "CLOSE_FLIGHTSTREAM"
    ]

    write_lines_to_file(script_filepath, lines)
    return
