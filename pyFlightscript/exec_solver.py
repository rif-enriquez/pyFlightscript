from .utils import *    
from .script import script    

def start_solver():
    """
    Appends lines to script state to start the solver.
    


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
    
    script.append_lines(lines)
    return

def solver_clear():
    """
    Appends lines to script state to clear the existing solution.
    


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
    
    script.append_lines(lines)
    return

def close_flightstream():
    """
    Appends lines to script state to close FlightStream and exit.



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

    script.append_lines(lines)
    return
