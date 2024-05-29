from .utils import *    
from .script import script    

def scene_contour(variable=4):
    """
    Appends lines to script state to set the scene contour parameter.
    
    Example usage:
        set_scene_contour(variable=5)
    

    :param variable: Value of the contour parameter.

    | value, variable
    | 0 No contour
    | 1 X
    | 2 Y
    | 3 Z
    | 4 Vorticity
    | 5 Skin friction coefficient
    | 6 Area
    | 7 Boundary Mach Number
    | 8 Coefficient of pressure (Free-stream velocity)
    | 9 Mach Number
    | 10 Solver partition ID
    | 11 Separation marker
    | 12 Velocity X component
    | 13 Velocity Y component
    | 14 Velocity Z component
    | 15 Velocity magnitude
    | 16 Boundary layer displacement thickness
    | 17 Boundary layer streamline length
    | 18 Coefficient of pressure (reference velocity)
    | 19 Solver mesh quality
    | 20 Boundary layer transition marker
    | 21 Solver mesh stabilization
    | 22 Boundary layer momentum thickness
    | 23 Boundary layer momentum gradient
    | 24 Boundary layer shape factor
    | 25 Boundary layer stagnation marker

    """
    
    # Type and value checking
    valid_variables = list(range(26))  # 0 to 25
    if variable not in valid_variables:
        raise ValueError(f"`variable` should be one of {valid_variables}")
    
    lines = [
        "#************************************************************************",
        "#****************** Change scene contour parameter **********************",
        "#************************************************************************",
        "#",
        "SET_SCENE_CONTOUR",
        f"VARIABLE {variable}"
    ]

    script.append_lines(lines)
    return

def set_vorticity_drag_boundaries(num_boundaries, boundary_indices=None):
    """
    Appends lines to script state to set vorticity-based induced drag boundaries.

    :param num_boundaries: Number of boundaries to be added to the list, or -1 to set all.
    :param boundary_indices: List of boundary indices, ignored if num_boundaries is -1.
    """
    
    # Type and value checking for num_boundaries
    if not isinstance(num_boundaries, int):
        raise ValueError("`num_boundaries` should be an integer value.")
    
    # Prepare script lines
    lines = [
        "#************************************************************************",
        "#****** Set a custom vorticity induced-drag boundary list ***************",
        "#************************************************************************",
        "#"
    ]
    
    if num_boundaries == -1:
        # Setting all mesh boundaries
        lines.append("SET_VORTICITY_DRAG_BOUNDARIES -1")
        lines.append("# All mesh boundaries set as vorticity induced-drag boundaries.")
    else:
        # Validate boundary_indices if num_boundaries is not -1
        if not isinstance(boundary_indices, list) or not all(isinstance(idx, int) for idx in boundary_indices):
            raise ValueError("When `num_boundaries` is not -1, `boundary_indices` should be a list of integers.")
        
        if len(boundary_indices) != num_boundaries:
            raise ValueError("`boundary_indices` length must match `num_boundaries`.")
        
        # Setting specified boundaries
        lines.append(f"SET_VORTICITY_DRAG_BOUNDARIES {num_boundaries}")
        lines.append(",".join(map(str, boundary_indices)))

    # Assuming script.append_lines is a function to append lines to a global script context
    script.append_lines(lines)
    return

def delete_vorticity_drag_boundaries():
    """
    Clears the vorticity induced-drag boundaries from the script state.
    """
    lines = [
        "#************************************************************************",
        "#************** Clear the vorticity induced-drag boundaries *************",
        "#************************************************************************",
        "#",
        "DELETE_VORTICITY_DRAG_BOUNDARIES"
    ]

    script.append_lines(lines)
    return

def set_analysis_moments_model(model="PRESSURE"):
    """
    Sets the moments model used in the analysis to either 'PRESSURE' or 'VORTICITY'.

    :param model: A string that indicates the model type, either 'PRESSURE' (default) or 'VORTICITY'.
    """
    
    # Type and value checking
    if model not in ['PRESSURE', 'VORTICITY']:
        raise ValueError("`model` must be either 'PRESSURE' or 'VORTICITY'.")
    
    lines = [
        "#************************************************************************",
        "#****************** Set the moments model used in the analysis **********",
        "#************************************************************************",
        "#",
        f"SET_ANALYSIS_MOMENTS_MODEL {model}"
    ]

    script.append_lines(lines)
    return

def set_analysis_symmetry_loads(enable):
    """
    Enables or disables the analysis to include loads from symmetry boundaries.

    :param enable: Boolean to enable (True) or disable (False) symmetry loads.
    """
    
    # Type checking
    if not isinstance(enable, bool):
        raise ValueError("`enable` should be a boolean value.")
    
    action = "ENABLE" if enable else "DISABLE"
    
    lines = [
        "#************************************************************************",
        "#**** Enable the analysis to include loads from symmetry boundaries *****" if enable else "#**** Disable the analysis to include loads from symmetry boundaries ****",
        "#************************************************************************",
        "#",
        f"SET_ANALYSIS_SYMMETRY_LOADS {action}"
    ]

    script.append_lines(lines)
    return

def analysis_loads_frame(load_frame=1):
    """
    Appends lines to script state to set the loads frame in the analysis tab.
    

    :param load_frame: Index of the coordinate system used for evaluating aerodynamic loads and moments.
    
    Example usage:
    analysis_loads_frame()
    """
    
    # Type and value checking
    if not isinstance(load_frame, int):
        raise ValueError("`load_frame` should be an integer value.")
    
    lines = [
        "#************************************************************************",
        "#****************** Set the loads frame in the analysis tab *************",
        "#************************************************************************",
        "#",
        f"SET_SOLVER_ANALYSIS_LOADS_FRAME {load_frame}"
    ]

    script.append_lines(lines)
    return

def vorticity_lift_model(enable=True):
    """
    Appends lines to script state to set the lift model to vorticity mode.
    

    :param enable: Boolean to indicate if the model should be enabled or disabled.
    
    Example usage:
    set_vorticity_lift_model(, enable=True)
    """
    
    # Type and value checking
    if not isinstance(enable, bool):
        raise ValueError("`enable` should be a boolean value (True/False).")
    
    status = "ENABLE" if enable else "DISABLE"
    
    lines = [
        "#************************************************************************",
        "#****************** Set the lift model to vorticity mode ****************",
        "#************************************************************************",
        "#",
        f"SET_VORTICITY_LIFT_MODEL {status}"
    ]

    script.append_lines(lines)
    return

def loads_and_moments_units(unit_type='NEWTONS'):
    """
    Appends lines to script state to set the loads and moments units.


    :param unit_type: Unit type for loads and moments.

    Example usage:
    set_loads_and_moments_units()
    """
    
    check_valid_force_units(unit_type)

    lines = [
        "#************************************************************************",
        "#****************** Set the solver analysis units selection *************",
        "#************************************************************************",
        "#",
        f"SET_LOADS_AND_MOMENTS_UNITS {unit_type}"
    ]
    script.append_lines(lines)
    return

def analysis_boundaries(num_boundaries, boundaries_list=[]):
    """
    Appends lines to script state to set the solver analysis boundaries.


    :param num_boundaries: Number of solver boundaries being enabled.
    :param boundaries_list: List of solver boundaries to be enabled.

    Example usage:
    analysis_boundaries(, 5, [1, 2, 4, 5, 7])
    """
    
    if not isinstance(num_boundaries, int) or num_boundaries <= 0:
        raise ValueError("`num_boundaries` should be a positive integer value.")

    if len(boundaries_list) != num_boundaries:
        raise ValueError("Mismatch in number of boundaries and provided list size.")

    boundaries_str = ','.join(map(str, boundaries_list))
    lines = [
        "#************************************************************************",
        "#****************** Set the solver analysis boundaries ******************",
        "#************************************************************************",
        "#",
        f"SET_SOLVER_ANALYSIS_BOUNDARIES {num_boundaries}",
        boundaries_str
    ]

    script.append_lines(lines)
    return

def set_inviscid_loads(enable):
    """
    Enables or disables the computation of inviscid loads and moments only.

    :param enable: Boolean to enable (True) or disable (False) the feature.
    """
    
    # Type checking
    if not isinstance(enable, bool):
        raise ValueError("`enable` should be a boolean value.")

    status = "ENABLE" if enable else "DISABLE"
    
    lines = [
        "#************************************************************************",
        "#********* Set the Analysis to be inviscid loads & moments only *********",
        "#************************************************************************",
        "#",
        f"SET_INVISCID_LOADS {status}"
    ]

    script.append_lines(lines)
    return
