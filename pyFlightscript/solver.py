from .utils import *    
from .script import script

def initialize_solver(surfaces, load_frame, symmetry_periodicity=1,
                      proximity_avoidance='DISABLE', stabilization='ENABLE', stabilization_strength=1.0,
                      fast_multipole='ENABLE', wake_termination_x='DEFAULT', symmetry_type='NONE'):
    """
    Appends lines to script state to initialize the solver.

    :param surfaces: (number or list) Number of surfaces being initialized in the solver (> 0 and < total surfaces). 
                    Value can be -1 to specify all boundaries. This call also starts a block of parameter 
                    lines that specify the initialization settings of each surface to be initialized, in 
                    this order:
                    Index # of the Surface, Motion object index # (0 if no motion),  ENABLE / DISABLE Quad mesher
    :param load_frame: (int) Index of coordinate system to be used for evaluating aerodynamic loads and moments.
                        Use index of 1 for reference coordinate system.
    :param symmetry_periodicity: (int) Integer value for number of periodic symmetry transforms about the Reference frame X axis.
    :param proximity_avoidance: (str) 'ENABLE' or 'DISABLE' proximity avoidance for the wake strands
    :param stabilization: (str) 'ENABLE' or 'DISABLE' solver stabilization.
    :param stabilization_strength: (int or float) 0.0 < Value < 5.0
    :param fast_multipole: (str) 'ENABLE' or 'DISABLE' Fast Multipole solver mode.
    :param wake_termination_x: (str or number) Wake termination plane location downstream of the geometry. X axis value measured 
                                relative to the Reference coordinate system. Use value of DEFAULT if you require 
                                this value to be auto-computed.
    :param symmetry_type: Symmetry type. One of: 'NONE', 'PLANE' or 'PERIODIC'

    Example usage:
    initialize_solver(surfaces=[(1, 0, 'ENABLE'), (2, 0, 'DISABLE')],  load_frame=1, symmetry_periodicity=2,
                      proximity_avoidance='ENABLE', stabilization='DISABLE', stabilization_strength=2.5,
                      fast_multipole='ENABLE', wake_termination_x=5.0, symmetry_type='PLANE')
    """
    
    if surfaces != -1:
        if not isinstance(surfaces, list):
            raise ValueError("`surfaces` should be a list of tuples or -1.")
        for surface in surfaces:
            if not isinstance(surface, tuple) or len(surface) != 3:
                raise ValueError("Each entry in `surfaces` should be a tuple of length 3.")
            if not isinstance(surface[2], str) or surface[2] not in ['ENABLE', 'DISABLE']:
                raise ValueError("Third element in each tuple should be 'ENABLE' or 'DISABLE'.")

    # Check load_frame is integer and >= 1
    if not isinstance(load_frame, int) or load_frame < 1:
        raise ValueError("`load_frame` should be an integer and >= 1.")
    
    # Check symmetry_periodicity is an integer
    if not isinstance(symmetry_periodicity, int):
        raise ValueError("`symmetry_periodicity` should be an integer.")
    
    # Check proximity_avoidance, stabilization, and fast_multipole
    for param, value in {'proximity_avoidance': proximity_avoidance,
                         'stabilization': stabilization,
                         'fast_multipole': fast_multipole}.items():
        if value not in ['ENABLE', 'DISABLE']:
            raise ValueError(f"`{param}` should be either 'ENABLE' or 'DISABLE'.")
    
    # Check wake_termination_x
    if wake_termination_x != 'DEFAULT' and not isinstance(wake_termination_x, (int, float)):
        raise ValueError("`wake_termination_x` should be either 'DEFAULT' or a number.")
    
    
    lines = [
        "#************************************************************************",
        "#****************** Initialize the solver *******************************",
        "#************************************************************************",
        "#",
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
    solver_proximal_boundaries(, 1, 4, 5)
    """
    
    # Type and value checking
    for boundary in boundaries:
        if not isinstance(boundary, int):
            raise ValueError("`boundaries` should be a list/tuple of integer values.")
    
    lines = [
        "#************************************************************************",
        "#********* Enable solver proximity checking for specified boundaries ****",
        "#************************************************************************",
        "#",
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
    >>> solver_uninitialize()
    """
    
    lines = [
        "#************************************************************************",
        "#********* Remove the solver initialization *****************************",
        "#************************************************************************",
        "#",
        "SOLVER_UNINITIALIZE"
    ]
    
    script.append_lines(lines)
    return





