from .utils import *    
from .script_state import script

def initialize_solver(surfaces, load_frame, symmetry_periodicity=0,
                      proximity_avoidance='DISABLE', stabilization='ENABLE', stabilization_strength=1.0,
                      fast_multipole='ENABLE', wake_termination_x='DEFAULT', symmetry_type='NONE'):
    """
    Appends lines to script state to initialize the solver.


    ... [other parameters]
    
    Example usage:
    initialize_solver('path_to_script.txt', [(1, 0, 'ENABLE'), (2, 0, 'ENABLE')], 3.5, 'PLANE', 1, 1, 
                      'DISABLE', 'ENABLE', 1.0, 'ENABLE')
    """
    
    # Type and value checking
    valid_symmetry_types = ['NONE', 'PLANE', 'PERIODIC']
    if symmetry_type not in valid_symmetry_types:
        raise ValueError(f"`symmetry_type` should be one of {valid_symmetry_types}")

    if not (0.0 < stabilization_strength < 5.0):
        raise ValueError("`stabilization_strength` should be a value between 0.0 and 5.0 exclusive.")
    
    lines = [
        "#************************************************************************",
        "#****************** Initialize the solver *******************************",
        "#************************************************************************",
        "",
        "INITIALIZE_SOLVER"
    ]
    
    # Check if surfaces is meant for all boundaries or specific ones
    if surfaces == -1:
        lines.append("SURFACES -1")
    else:
        lines.append(f"SURFACES {len(surfaces)}")
        for surface in surfaces:
            lines.append(f"{surface[0]},{surface[1]},{surface[2]}")
    
    lines.extend([
        f"WAKE_TERMINATION_X {wake_termination_x}",
        f"SYMMETRY_TYPE {symmetry_type}",
        f"SYMMETRY_PERIODICITY {symmetry_periodicity}",
        f"LOAD_FRAME {load_frame}",
        f"PROXIMITY_AVOIDANCE {proximity_avoidance}",
        f"STABILIZATION {stabilization}",
        f"STABILIZATION_STRENGTH {stabilization_strength}",
        f"FAST_MULTIPOLE {fast_multipole}"
    ])

    script.append_lines(lines)
    return


def solver_proximal_boundaries(*boundaries):
    """
    Appends lines to script state to enable solver proximity checking for specified boundaries.
    

    :param boundaries: Indices of the geometry boundaries for which solver proximity checking is being enabled.
    
    Example usage:
    solver_proximal_boundaries('path_to_script.txt', 1, 4, 5)
    """
    
    # Type and value checking
    for boundary in boundaries:
        if not isinstance(boundary, int):
            raise ValueError("`boundaries` should be a list/tuple of integer values.")
    
    lines = [
        "#************************************************************************",
        "#********* Enable solver proximity checking for specified boundaries ****",
        "#************************************************************************",
        "",
        f"SOLVER_PROXIMAL_BOUNDARIES {len(boundaries)}"
    ]

    for boundary in boundaries:
        lines.append(str(boundary))
        
    script.append_lines(lines)
    return

def solver_uninitialize():
    """
    Appends lines to script state to remove the solver initialization.
    

    
    Example usage:
    >>> solver_uninitialize('path_to_script.txt')
    """
    
    lines = [
        "#************************************************************************",
        "#********* Remove the solver initialization *****************************",
        "#************************************************************************",
        "",
        "SOLVER_UNINITIALIZE"
    ]
    
    script.append_lines(lines)
    return





