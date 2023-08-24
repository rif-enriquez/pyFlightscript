from .utils import *    

def set_scene_contour(script_filepath, variable=4):
    """
    Writes specific lines to 'script_filepath' to set the scene contour parameter.
    
    Example usage:
        set_scene_contour('path_to_script.txt', variable=5)
    
    :param script_filepath: Path to the script file.
    :param variable: Value of the contour parameter.

    value, variable
    0 No contour
    1 X
    2 Y
    3 Z
    4 Vorticity
    5 Skin friction coefficient
    6 Area
    7 Boundary Mach Number
    8 Coefficient of pressure (Free-stream velocity)
    9 Mach Number
    10 Solver partition ID
    11 Separation marker
    12 Velocity X component
    13 Velocity Y component
    14 Velocity Z component
    15 Velocity magnitude
    16 Boundary layer displacement thickness
    17 Boundary layer streamline length
    18 Coefficient of pressure (reference velocity)
    19 Solver mesh quality
    20 Boundary layer transition marker
    21 Solver mesh stabilization
    22 Boundary layer momentum thickness
    23 Boundary layer momentum gradient
    24 Boundary layer shape factor
    25 Boundary layer stagnation marker

    """
    
    # Type and value checking
    valid_variables = list(range(26))  # 0 to 25
    if variable not in valid_variables:
        raise ValueError(f"`variable` should be one of {valid_variables}")
    
    lines = [
        "#************************************************************************",
        "#****************** Change scene contour parameter **********************",
        "#************************************************************************",
        "",
        "SET_SCENE_CONTOUR",
        f"VARIABLE {variable}"
    ]

    write_lines_to_file(script_filepath, lines)
    return

def solver_analysis_options(script_filepath, load_frame=1, drag_model='VORTICITY', 
                            moment_model='PRESSURE', compute_symmetry_loads='ENABLE'):
    """
    Writes specific lines to 'script_filepath' to set the solver analysis options.
    
    Example usage:
        solver_analysis_options('path_to_script.txt', load_frame=2, drag_model='PRESSURE')
    
    :param script_filepath: Path to the script file.
    :param load_frame: Index of the coordinate system.
    :param drag_model: Drag model type.
    :param moment_model: Moment model type.
    :param compute_symmetry_loads: ENABLE or DISABLE computation of mirrored boundaries.
    """
    
    # Type and value checking
    if not isinstance(load_frame, int):
        raise ValueError("`load_frame` should be an integer value.")
    
    valid_models = ['VORTICITY', 'PRESSURE']
    if drag_model not in valid_models:
        raise ValueError(f"`drag_model` should be one of {valid_models}")
    if moment_model not in valid_models:
        raise ValueError(f"`moment_model` should be one of {valid_models}")
    
    valid_symmetry_loads = ['ENABLE', 'DISABLE']
    if compute_symmetry_loads not in valid_symmetry_loads:
        raise ValueError(f"`compute_symmetry_loads` should be one of {valid_symmetry_loads}")
    
    lines = [
        "#************************************************************************",
        "#****************** Set the solver analysis options **********************",
        "#************************************************************************",
        "",
        "SOLVER_ANALYSIS_OPTIONS",
        f"LOAD_FRAME {load_frame}",
        f"DRAG_MODEL {drag_model}",
        f"MOMENT_MODEL {moment_model}",
        f"COMPUTE_SYMMETRY_LOADS {compute_symmetry_loads}"
    ]

    write_lines_to_file(script_filepath, lines)
    return

def set_solver_analysis_loads_frame(script_filepath, load_frame=1):
    """
    Writes specific lines to 'script_filepath' to set the loads frame in the analysis tab.
    
    :param script_filepath: Path to the script file.
    :param load_frame: Index of the coordinate system used for evaluating aerodynamic loads and moments.
    
    Example usage:
    set_solver_analysis_loads_frame('path_to_script.txt')
    """
    
    # Type and value checking
    if not isinstance(load_frame, int):
        raise ValueError("`load_frame` should be an integer value.")
    
    lines = [
        "#************************************************************************",
        "#****************** Set the loads frame in the analysis tab *************",
        "#************************************************************************",
        "",
        f"SET_SOLVER_ANALYSIS_LOADS_FRAME {load_frame}"
    ]

    write_lines_to_file(script_filepath, lines)
    return

def set_vorticity_lift_model(script_filepath, enable=True):
    """
    Writes specific lines to 'script_filepath' to set the lift model to vorticity mode.
    
    :param script_filepath: Path to the script file.
    :param enable: Boolean to indicate if the model should be enabled or disabled.
    
    Example usage:
    set_vorticity_lift_model('path_to_script.txt', enable=True)
    """
    
    # Type and value checking
    if not isinstance(enable, bool):
        raise ValueError("`enable` should be a boolean value (True/False).")
    
    status = "ENABLE" if enable else "DISABLE"
    
    lines = [
        "#************************************************************************",
        "#****************** Set the lift model to vorticity mode ****************",
        "#************************************************************************",
        "",
        f"SET_VORTICITY_LIFT_MODEL {status}"
    ]

    write_lines_to_file(script_filepath, lines)
    return

def set_loads_and_moments_units(script_filepath, unit_type='NEWTONS'):
    """
    Writes specific lines to 'script_filepath' to set the loads and moments units.

    :param script_filepath: Path to the script file.
    :param unit_type: Unit type for loads and moments.

    Example usage:
    set_loads_and_moments_units('path_to_script.txt')
    """
    
    check_valid_force_units(unit_type)

    lines = [
        "#************************************************************************",
        "#****************** Set the solver analysis units selection *************",
        "#************************************************************************",
        "",
        f"SET_LOADS_AND_MOMENTS_UNITS {unit_type}"
    ]
    write_lines_to_file(script_filepath, lines)
    return

def set_solver_analysis_boundaries(script_filepath, num_boundaries, boundaries_list=[]):
    """
    Writes specific lines to 'script_filepath' to set the solver analysis boundaries.

    :param script_filepath: Path to the script file.
    :param num_boundaries: Number of solver boundaries being enabled.
    :param boundaries_list: List of solver boundaries to be enabled.

    Example usage:
    set_solver_analysis_boundaries('path_to_script.txt', 5, [1, 2, 4, 5, 7])
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
        "",
        f"SET_SOLVER_ANALYSIS_BOUNDARIES {num_boundaries}",
        boundaries_str
    ]

    write_lines_to_file(script_filepath, lines)
    return
