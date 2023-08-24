from .utils import *

def set_solver_steady(script_filepath):
    """
    Writes specific lines to 'script_filepath' to set the steady solver.
    
    Example usage:
        set_solver_steady('path_to_script.txt')
    """
    
    lines = [
        "#************************************************************************",
        "#********* Set the steady solver ****************************************",
        "#************************************************************************",
        "",
        "SET_SOLVER_STEADY"
    ]

    write_lines_to_file(script_filepath, lines)
    return


def set_solver_unsteady(script_filepath, time_iterations=100, delta_time=0.1):
    """
    Writes specific lines to 'script_filepath' to set the unsteady solver.
    
    :param script_filepath: Path to the script file.
    :param time_iterations: Number of time-stepping iterations to be run by the unsteady solver.
    :param delta_time: Physical time step of the unsteady solver.
    
    Example usage:
        set_solver_unsteady('path_to_script.txt')
    """
    
    # Type and value checking
    if not isinstance(time_iterations, int) or time_iterations <= 0:
        raise ValueError("`time_iterations` should be a positive integer value.")
    
    if not isinstance(delta_time, (int, float)) or delta_time <= 0:
        raise ValueError("`delta_time` should be a positive number.")
    
    lines = [
        "#************************************************************************",
        "#********* Set the unsteady solver **************************************",
        "#************************************************************************",
        "",
        "SET_SOLVER_UNSTEADY",
        f"TIME_ITERATIONS {time_iterations}",
        f"DELTA_TIME {delta_time}"
    ]

    write_lines_to_file(script_filepath, lines)
    return

def unsteady_solver_new_force_plot(script_filepath, frame=1, units='NEWTONS', parameter='FORCE_X', 
                                   name='Plot_Name', boundaries=-1, boundary_indices=None):
    """
    Writes specific lines to 'script_filepath' to create a new unsteady solver force & moments plot.
    
    :param script_filepath: Path to the script file.
    :param frame: Index of the coordinate system to be used.
    :param units: Units for the plot.
    :param parameter: The force or moment parameter.
    :param name: Name of the plot.
    :param boundaries: Total geometry boundaries to be linked.
    :param boundary_indices: List of boundary indices.
    
    Example usage:
    unsteady_solver_new_force_plot('path_to_script.txt', name='Propeller_thrust', boundaries=3, boundary_indices=[1, 2, 4])
    """
    
    # Type and value checking
    if not isinstance(frame, int):
        raise ValueError("`frame` should be an integer value.")
    
    check_valid_force_units(units)
    
    valid_parameters = ['CL', 'CDI', 'CDO', 'CD', 'FORCE_X', 'FORCE_Y', 'FORCE_Z', 'MOMENT_X', 'MOMENT_Y', 'MOMENT_Z']
    if parameter not in valid_parameters:
        raise ValueError(f"`parameter` should be one of {valid_parameters}")
    
    lines = [
        "#************************************************************************",
        "#********* Create a new unsteady solver force & moments plot ************",
        "#************************************************************************",
        "",
        "UNSTEADY_SOLVER_NEW_FORCE_PLOT",
        f"FRAME {frame}",
        f"UNITS {units}",
        f"PARAMETER {parameter}",
        f"NAME {name}",
        f"BOUNDARIES {boundaries}"
    ]
    
    if boundaries != -1 and boundary_indices:
        lines.append(','.join(map(str, boundary_indices)))

    write_lines_to_file(script_filepath, lines)
    return

def unsteady_solver_new_fluid_plot(script_filepath, frame=1, parameter='VELOCITY', name='Plot_Name', vertex=(-1.0, 1.0, 0.0)):
    """
    Writes specific lines to 'script_filepath' to create a new unsteady solver fluid properties plot.
    
    :param script_filepath: Path to the script file.
    :param frame: Index of the coordinate system to be used.
    :param parameter: The fluid property parameter.
    :param name: Name of the plot.
    :param vertex: Vertex coordinates for the fluid property measurement location.
    
    Example usage:
    unsteady_solver_new_fluid_plot('path_to_script.txt', name='Propeller_slipstream', vertex=(-2.0, 1.4, 0.0))
    """
    
    # Type and value checking
    if not isinstance(frame, int):
        raise ValueError("`frame` should be an integer value.")
    
    valid_parameters = ['CP_FREE', 'CP_REF', 'MACH', 'VELOCITY', 'VX', 'VY', 'VZ', 'STATIC_PRESSURE_RATIO']
    if parameter not in valid_parameters:
        raise ValueError(f"`parameter` should be one of {valid_parameters}")
    
    lines = [
        "#************************************************************************",
        "#********* Create a new unsteady solver fluid properties plot ***********",
        "#************************************************************************",
        "",
        "UNSTEADY_SOLVER_NEW_FLUID_PLOT",
        f"FRAME {frame}",
        f"PARAMETER {parameter}",
        f"NAME {name}",
        f"VERTEX {' '.join(map(str, vertex))}"
    ]

    write_lines_to_file(script_filepath, lines)
    return

def unsteady_solver_export_plots(script_filepath, export_filepath):
    """
    Writes specific lines to 'script_filepath' to export all unsteady solver plots.
    
    :param script_filepath: Path to the script file.
    :param export_filepath: Path where plots should be exported.
    
    Example usage:
    unsteady_solver_export_plots('path_to_script.txt', 'C:\\Users\\Desktop\\Models\\my_exported_data.txt')
    """
    
    # Prepare the lines to be written to file
    lines = [
        "#************************************************************************",
        "#****************** Export all unsteady solver plots ********************",
        "#************************************************************************",
        "",
        "UNSTEADY_SOLVER_EXPORT_PLOTS",
        export_filepath
    ]

    write_lines_to_file(script_filepath, lines)
    return


def unsteady_solver_delete_all_plots(script_filepath):
    """
    Writes specific lines to 'script_filepath' to delete all unsteady solver plots.
    
    :param script_filepath: Path to the script file.
    
    Example usage:
    unsteady_solver_delete_all_plots('path_to_script.txt')
    """
    
    # Prepare the lines to be written to file
    lines = [
        "#************************************************************************",
        "#****************** Delete all unsteady solver plots ********************",
        "#************************************************************************",
        "",
        "UNSTEADY_SOLVER_DELETE_ALL_PLOTS"
    ]

    write_lines_to_file(script_filepath, lines)
    return

def set_boundary_layer_type(script_filepath, type_value='TRANSITIONAL'):
    """
    Writes specific lines to 'script_filepath' to set the surface boundary layer type.
    
    :param script_filepath: Path to the script file.
    :param type_value: Type of the boundary layer (default: 'TRANSITIONAL').
    
    Example usage:
    set_boundary_layer_type('path_to_script.txt')
    """
    
    # Type and value checking
    valid_types = ['LAMINAR', 'TRANSITIONAL', 'TURBULENT']
    if type_value not in valid_types:
        raise ValueError(f"`type_value` should be one of {valid_types}")
    
    lines = [
        "#************************************************************************",
        "#****************** Set the surface boundary layer type *****************",
        "#************************************************************************",
        "",
        f"SET_BOUNDARY_LAYER_TYPE {type_value}"
    ]
    
    write_lines_to_file(script_filepath, lines)
    return

def set_surface_roughness(script_filepath, roughness_height=23.5):
    """
    Writes specific lines to 'script_filepath' to set the surface roughness height.
    
    :param script_filepath: Path to the script file.
    :param roughness_height: Height of the surface roughness in nano-meters (default: 23.5 nm).
    
    Example usage:
    set_surface_roughness('path_to_script.txt')
    """
    
    # Type and value checking
    if not isinstance(roughness_height, (int, float)) or roughness_height <= 0.0:
        raise ValueError("`roughness_height` should be a positive integer or float value.")
    
    lines = [
        "#************************************************************************",
        "#****************** Set the surface roughness height ********************",
        "#************************************************************************",
        "",
        f"SET_SURFACE_ROUGHNESS {roughness_height}"
    ]
    
    write_lines_to_file(script_filepath, lines)
    return

def set_solver_viscous_coupling(script_filepath, mode='ENABLE'):
    """
    Writes specific lines to 'script_filepath' to set the solver viscous coupling.

    :param script_filepath: Path to the script file.
    :param mode: The mode to set the solver viscous coupling, either 'ENABLE' or 'DISABLE'.
    
    Example usage:
    set_solver_viscous_coupling('path_to_script.txt')
    """

    # Type and value checking
    valid_modes = ['ENABLE', 'DISABLE']
    if mode not in valid_modes:
        raise ValueError(f"Mode should be one of {valid_modes}")

    lines = [
        "#************************************************************************",
        "#****************** Set the solver viscous coupling ********************",
        "#************************************************************************",
        "",
        f"SET_SOLVER_VISCOUS_COUPLING {mode}"
    ]

    write_lines_to_file(script_filepath, lines)
    return

def set_viscous_excluded_boundaries(script_filepath, num_boundaries, boundaries):
    """
    Writes specific lines to 'script_filepath' to set the viscous exclusion boundary list.

    :param script_filepath: Path to the script file.
    :param num_boundaries: Number of boundaries being excluded.
    :param boundaries: List of indices of boundaries being excluded.
    
    Example usage:
    set_viscous_excluded_boundaries('path_to_script.txt', 3, [1, 2, 4])
    """
    
    # Type and value checking
    if not isinstance(num_boundaries, int):
        raise ValueError("`num_boundaries` should be an integer value.")

    if not isinstance(boundaries, list) or not all(isinstance(b, int) for b in boundaries):
        raise ValueError("`boundaries` should be a list of integers.")

    if len(boundaries) != num_boundaries:
        raise ValueError("`num_boundaries` should match the number of boundaries provided.")

    lines = [
        "#************************************************************************",
        "#************** Set the viscous exclusion boundary list ****************",
        "#************************************************************************",
        "",
        f"SET_VISCOUS_EXCLUDED_BOUNDARIES {num_boundaries}",
        ",".join(map(str, boundaries))
    ]

    write_lines_to_file(script_filepath, lines)
    return

def enable_flow_separation(script_filepath):
    """
    Writes specific lines to 'script_filepath' to enable the flow separation model.
    
    :param script_filepath: Path to the script file.

    Example usage:
    enable_flow_separation('path_to_script.txt')
    """
    
    lines = [
        "#************************************************************************",
        "#************ Enable the flow separation model **************************",
        "#************************************************************************",
        "",
        "ENABLE_FLOW_SEPARATION"
    ]

    write_lines_to_file(script_filepath, lines)
    return

def set_stratford_separation_model(script_filepath, model, crossflow_direction=None, cp=None):
    """
    Writes specific lines to 'script_filepath' to set the Stratford separation model.
    
    :param script_filepath: Path to the script file.
    :param model: Stratford model type (either AXIAL or CROSSFLOW).
    :param crossflow_direction: Direction of the flow for CROSSFLOW model.
    :param cp: Separation pressure coefficient for the CROSSFLOW model.

    Example usage:
    set_stratford_separation_model('path_to_script.txt', 'AXIAL')
    set_stratford_separation_model('path_to_script.txt', 'CROSSFLOW', 'LATERAL', -0.52)
    """
    
    # Type and value checking
    valid_models = ['AXIAL', 'CROSSFLOW']
    if model not in valid_models:
        raise ValueError(f"`model` should be one of {valid_models}")
    
    if model == 'CROSSFLOW':
        valid_directions = ['LONGITUDINAL', 'LATERAL']
        if crossflow_direction not in valid_directions:
            raise ValueError(f"`crossflow_direction` should be one of {valid_directions}")
        
        if cp is None or not isinstance(cp, (int, float)):
            raise ValueError("`cp` should be an integer or float value.")
        
        lines = [
            "#************************************************************************",
            "#****************** Set the Stratford separation model ******************",
            "#************************************************************************",
            "",
            f"SET_STRATFORD_SEPARATION_MODEL {model} {crossflow_direction} {cp}"
        ]
    else:
        lines = [
            "#************************************************************************",
            "#****************** Set the Stratford (axial) separation model **********",
            "#************************************************************************",
            "",
            f"SET_STRATFORD_SEPARATION_MODEL {model}"
        ]

    write_lines_to_file(script_filepath, lines)
    return

def disable_flow_separation(script_filepath):
    """
    Writes specific lines to 'script_filepath' to disable viscous flow separation.
    
    Example usage:
        disable_flow_separation('path_to_script.txt')
    """
    lines = [
        "#************************************************************************",
        "#****************** Disable the viscous flow separation *****************",
        "#************************************************************************",
        "",
        "DISABLE_FLOW_SEPARATION"
    ]
    write_lines_to_file(script_filepath, lines)
    return


def solver_settings(script_filepath, angle_of_attack=0., sideslip_angle=0., 
                    freestream_velocity=100., iterations=500, 
                    convergence_limit=1e-5, forced_run='DISABLE', 
                    compressibility='DISABLE', reference_velocity=100., 
                    reference_area=1., reference_length=1., processors=2, 
                    wake_size=1000):
    """
    Writes specific lines to 'script_filepath' to set the solver settings.
    
    Example usage:
        solver_settings('path_to_script.txt')
    """
    # Type and value checking
    if not isinstance(angle_of_attack, (int, float)) or abs(angle_of_attack) >= 90:
        raise ValueError("`angle_of_attack` should be a number with |angle| < 90.")
    
    if not isinstance(sideslip_angle, (int, float)) or abs(sideslip_angle) >= 90:
        raise ValueError("`sideslip_angle` should be a number with |angle| < 90.")
    
    if not isinstance(freestream_velocity, (int, float)):
        raise ValueError("`freestream_velocity` should be a number.")
    
    if not isinstance(iterations, int):
        raise ValueError("`iterations` should be an integer value.")
    
    valid_run = ['ENABLE', 'DISABLE']
    if forced_run not in valid_run or compressibility not in valid_run:
        raise ValueError(f"`forced_run` and `compressibility` should be one of {valid_run}")
    
    if not isinstance(reference_velocity, (int, float)):
        raise ValueError("`reference_velocity` should be a number.")
    
    if not isinstance(reference_area, (int, float)):
        raise ValueError("`reference_area` should be a number.")
    
    if not isinstance(reference_length, (int, float)):
        raise ValueError("`reference_length` should be a number.")
    
    if not isinstance(processors, int):
        raise ValueError("`processors` should be an integer value.")
    
    if not isinstance(wake_size, (int, float)):
        raise ValueError("`wake_size` should be a number.")

    lines = [
        "#************************************************************************",
        "#********* Set the solver settings **************************************",
        "#************************************************************************",
        "",
        "SOLVER_SETTINGS",
        f"ANGLE_OF_ATTACK {angle_of_attack}",
        f"SIDESLIP_ANGLE {sideslip_angle}",
        f"FREESTREAM_VELOCITY {freestream_velocity}",
        f"ITERATIONS {iterations}",
        f"CONVERGENCE_LIMIT {convergence_limit}",
        f"FORCED_RUN {forced_run}",
        f"COMPRESSIBILITY {compressibility}",
        f"REFERENCE_VELOCITY {reference_velocity}",
        f"REFERENCE_AREA {reference_area}",
        f"REFERENCE_LENGTH {reference_length}",
        f"PROCESSORS {processors}",
        f"WAKE_SIZE {wake_size}"
    ]

    write_lines_to_file(script_filepath, lines)
    return

def solver_set_aoa(script_filepath, angle):
    """
    Writes specific lines to 'script_filepath' to set the solver AOA.
    
    :param script_filepath: Path to the script file.
    :param angle: Angle of attack in degrees. |angle| must be < 90.
    
    Example usage:
    solver_set_aoa('path_to_script.txt', -5.0)
    """
    
    # Type and value checking
    if not isinstance(angle, (int, float)):
        raise ValueError("`angle` should be an integer or float value.")
    if abs(angle) >= 90:
        raise ValueError("`angle` must be less than 90 in magnitude.")
    
    lines = [
        "#************************************************************************",
        "#********* Set the solver AOA *******************************************",
        "#************************************************************************",
        "",
        f"SOLVER_SET_AOA {angle}"
    ]
    
    write_lines_to_file(script_filepath, lines)
    return


def solver_set_sideslip(script_filepath, angle):
    """
    Writes specific lines to 'script_filepath' to set the solver Side-slip angle.
    
    :param script_filepath: Path to the script file.
    :param angle: Side-slip angle in degrees. |angle| must be < 90.
    
    Example usage:
    solver_set_sideslip('path_to_script.txt', 5.0)
    """
    
    # Type and value checking
    if not isinstance(angle, (int, float)):
        raise ValueError("`angle` should be an integer or float value.")
    if abs(angle) >= 90:
        raise ValueError("`angle` must be less than 90 in magnitude.")
    
    lines = [
        "#************************************************************************",
        "#********* Set the solver Side-slip angle *******************************",
        "#************************************************************************",
        "",
        f"SOLVER_SET_SIDESLIP {angle}"
    ]
    
    write_lines_to_file(script_filepath, lines)
    return

def solver_set_velocity(script_filepath, velocity=30.0):
    """
    Writes specific lines to 'script_filepath' to set the solver free-stream velocity.
    
    :param script_filepath: Path to the script file.
    :param velocity: The free-stream velocity value.
    
    Example usage:
    solver_set_velocity('path_to_script.txt')
    """
    
    # Type and value checking
    if not isinstance(velocity, (int, float)):
        raise ValueError("`velocity` should be an integer or float value.")
    
    lines = [
        "#************************************************************************",
        "#********* Set the solver free-stream velocity **************************",
        "#************************************************************************",
        "",
        f"SOLVER_SET_VELOCITY {velocity}"
    ]

    write_lines_to_file(script_filepath, lines)
    return

def solver_set_iterations(script_filepath, num_iterations=500):
    """
    Writes specific lines to 'script_filepath' to set the solver iterations.
    
    :param script_filepath: Path to the script file.
    :param num_iterations: The number of solver iterations.
    
    Example usage:
    solver_set_iterations('path_to_script.txt')
    """
    
    # Type and value checking
    if not isinstance(num_iterations, int) or num_iterations <= 0:
        raise ValueError("`num_iterations` should be a positive integer value.")
    
    lines = [
        "#************************************************************************",
        "#****************** Set the solver iterations ***************************",
        "#************************************************************************",
        "",
        f"SOLVER_SET_ITERATIONS {num_iterations}"
    ]

    write_lines_to_file(script_filepath, lines)
    return

def solver_set_convergence(script_filepath, threshold=1E-5):
    """
    Writes specific lines to 'script_filepath' to set the solver convergence threshold.
    
    :param script_filepath: Path to the script file.
    :param threshold: Convergence threshold value.
    
    Example usage:
    solver_set_convergence('path_to_script.txt')
    """
    
    # Type and value checking
    if not isinstance(threshold, (int, float)):
        raise ValueError("`threshold` should be an integer or float value.")
    
    lines = [
        "#************************************************************************",
        "#****************** Set the solver convergence threshold ****************",
        "#************************************************************************",
        "",
        f"SOLVER_SET_CONVERGENCE {threshold}"
    ]

    write_lines_to_file(script_filepath, lines)
    return


def solver_set_forced_iterations(script_filepath, mode='ENABLE'):
    """
    Writes specific lines to 'script_filepath' to enable or disable solver forced iterations mode.
    
    :param script_filepath: Path to the script file.
    :param mode: Either 'ENABLE' or 'DISABLE'.
    
    Example usage:
    solver_set_forced_iterations('path_to_script.txt')
    """
    
    # Value checking
    valid_modes = ['ENABLE', 'DISABLE']
    if mode not in valid_modes:
        raise ValueError(f"`mode` should be one of {valid_modes}")
    
    lines = [
        "#************************************************************************",
        "#****************** Enable solver forced iterations mode ****************",
        "#************************************************************************",
        "",
        f"SOLVER_SET_FORCED_ITERATIONS {mode}"
    ]

    write_lines_to_file(script_filepath, lines)
    return

def solver_set_ref_velocity(script_filepath, value=100.):
    """
    Writes specific lines to 'script_filepath' to set the solver reference velocity.
    
    :param script_filepath: Path to the script file.
    :param value: Reference velocity.
    
    Example usage:
    solver_set_ref_velocity('path_to_script.txt')
    """
    
    # Type and value checking
    if not isinstance(value, (int, float)) or value <= 0.0:
        raise ValueError("`value` should be a positive number (int or float).")
    
    lines = [
        "#************************************************************************",
        "#********* Set the solver reference velocity ****************************",
        "#************************************************************************",
        "",
        f"SOLVER_SET_REF_VELOCITY {value}"
    ]

    write_lines_to_file(script_filepath, lines)
    return

def solver_set_ref_area(script_filepath, value=1.):
    """
    Writes specific lines to 'script_filepath' to set the solver reference area.
    
    :param script_filepath: Path to the script file.
    :param value: Reference area.
    
    Example usage:
    solver_set_ref_area('path_to_script.txt')
    """
    
    # Type and value checking
    if not isinstance(value, (int, float)) or value <= 0.0:
        raise ValueError("`value` should be a positive number (int or float).")
    
    lines = [
        "#************************************************************************",
        "#********* Set the solver reference area ********************************",
        "#************************************************************************",
        "",
        f"SOLVER_SET_REF_AREA {value}"
    ]

    write_lines_to_file(script_filepath, lines)
    return

def solver_set_ref_length(script_filepath, length=1.):
    """
    Writes specific lines to 'script_filepath' to set the solver reference length.
    
    :param script_filepath: Path to the script file.
    :param length: Reference length.
    
    Example usage:
    solver_set_ref_length('path_to_script.txt', length=2.5)
    """

    # Type and value checking
    if not isinstance(length, (int, float)) or length <= 0:
        raise ValueError("`length` should be a positive integer or float value.")
    
    lines = [
        "#************************************************************************",
        "#********* Set the solver reference length ******************************",
        "#************************************************************************",
        "",
        f"SOLVER_SET_REF_LENGTH {length}"
    ]

    write_lines_to_file(script_filepath, lines)
    return

def solver_set_compressibility(script_filepath, compressibility='ENABLE'):
    """
    Writes specific lines to 'script_filepath' to set the solver compressibility.
    
    :param script_filepath: Path to the script file.
    :param compressibility: Either 'ENABLE' or 'DISABLE'.
    
    Example usage:
    solver_set_compressibility('path_to_script.txt', compressibility='DISABLE')
    """

    # Type and value checking
    valid_options = ['ENABLE', 'DISABLE']
    if compressibility not in valid_options:
        raise ValueError(f"`compressibility` should be one of {valid_options}")
    
    lines = [
        "#************************************************************************",
        "#********* Set the solver compressibility *******************************",
        "#************************************************************************",
        "",
        f"SOLVER_SET_COMPRESSIBILITY {compressibility}"
    ]

    write_lines_to_file(script_filepath, lines)
    return

def solver_parallel_cores(script_filepath, num_cores=16):
    """
    Writes specific lines to 'script_filepath' to set the number of solver parallel cores.
    
    Example usage:
    solver_parallel_cores('path_to_script.txt')
    
    :param script_filepath: Path to the script file.
    :param num_cores: Number of parallel cores.
    """
    
    # Type and value checking
    if not isinstance(num_cores, int):
        raise ValueError("`num_cores` should be an integer value.")
    
    lines = [
        "#************************************************************************",
        "#********* Set the solver parallel cores ********************************",
        "#************************************************************************",
        "",
        f"SOLVER_PARALLEL_CORES {num_cores}"
    ]

    write_lines_to_file(script_filepath, lines)
    return

def solver_set_mesh_induced_wake_velocity(script_filepath, enable=True):
    """
    Writes specific lines to 'script_filepath' to set the solver mesh induced wake velocity.
    
    Example usage:
    solver_set_mesh_induced_wake_velocity('path_to_script.txt')
    
    :param script_filepath: Path to the script file.
    :param enable: Boolean to either enable or disable the feature.
    """
    
    # Type and value checking
    if not isinstance(enable, bool):
        raise ValueError("`enable` should be a boolean value (True/False).")
    
    status = "ENABLE" if enable else "DISABLE"
    
    lines = [
        "#************************************************************************",
        "#********* Set the solver mesh induced wake velocity ********************",
        "#************************************************************************",
        "",
        f"SOLVER_SET_MESH_INDUCED_WAKE_VELOCITY {status}"
    ]

    write_lines_to_file(script_filepath, lines)
    return

def solver_set_adverse_gradient_boundary_layer(script_filepath, mode='ENABLE'):
    """
    Writes specific lines to 'script_filepath' to set the adverse pressure gradient boundary layer mode.

    :param script_filepath: Path to the script file.
    :param mode: Mode to set the adverse pressure gradient boundary layer. ('ENABLE' or 'DISABLE')
    
    Example usage:
    solver_set_adverse_gradient_boundary_layer('path_to_script.txt', 'DISABLE')
    """
    
    # Type and value checking
    valid_modes = ['ENABLE', 'DISABLE']
    if mode not in valid_modes:
        raise ValueError(f"`mode` should be one of {valid_modes}")
    
    lines = [
        "#************************************************************************",
        "#********* Set the adverse pressure gradient boundary layer mode ********",
        "#************************************************************************",
        "",
        f"SOLVER_SET_ADVERSE_GRADIENT_BOUNDARY_LAYER {mode}"
    ]

    write_lines_to_file(script_filepath, lines)
    return

def solver_set_farfield_layers(script_filepath, value=3):
    """
    Writes specific lines to 'script_filepath' to set the solver far-field agglomeration layers.

    :param script_filepath: Path to the script file.
    :param value: Number of farfield layers. (Default is 3)
    
    Example usage:
    solver_set_farfield_layers('path_to_script.txt', 4)
    """
    
    # Type and value checking
    if not isinstance(value, int):
        raise ValueError("`value` should be an integer.")
    
    if not (1 <= value <= 5):
        raise ValueError("`value` should be between 1 and 5, inclusive.")
    
    lines = [
        "#************************************************************************",
        "#********* Set the solver far-field agglomeration layers ****************",
        "#************************************************************************",
        "",
        f"SOLVER_SET_FARFIELD_LAYERS {value}"
    ]

    write_lines_to_file(script_filepath, lines)
    return

def solver_unsteady_pressure_and_kutta(script_filepath, status='ENABLE'):
    """
    Writes specific lines to 'script_filepath' to enable or disable solver unsteady Bernoulli and Kutta terms.
    
    :param script_filepath: Path to the script file.
    :param status: Can be 'ENABLE' or 'DISABLE'.
    
    Example usage:
    solver_unsteady_pressure_and_kutta('path_to_script.txt', status='ENABLE')
    """
    
    # Type and value checking
    if status not in ['ENABLE', 'DISABLE']:
        raise ValueError("`status` should be either 'ENABLE' or 'DISABLE'")
    
    lines = [
        "#************************************************************************",
        "#********* Enable solver unsteady Bernoulli and Kutta terms *************",
        "#************************************************************************",
        "",
        f"SOLVER_UNSTEADY_PRESSURE_AND_KUTTA {status}"
    ]
    
    write_lines_to_file(script_filepath, lines)
    return

def solver_vortex_ring_normalization(script_filepath, status='ENABLE'):
    """
    Writes specific lines to 'script_filepath' to enable or disable solver vortex ring normalization.
    
    :param script_filepath: Path to the script file.
    :param status: Can be 'ENABLE' or 'DISABLE'.
    
    Example usage:
    solver_vortex_ring_normalization('path_to_script.txt', status='ENABLE')
    """
    
    # Type and value checking
    if status not in ['ENABLE', 'DISABLE']:
        raise ValueError("`status` should be either 'ENABLE' or 'DISABLE'")
    
    lines = [
        "#************************************************************************",
        "#********* Enable solver vortex ring normalization **********************",
        "#************************************************************************",
        "",
        f"SOLVER_VORTEX_RING_NORMALIZATION {status}"
    ]
    
    write_lines_to_file(script_filepath, lines)
    return

def set_solver_convergence_iterations(script_filepath, value=500):
    """
    Writes specific lines to 'script_filepath' to set the solver convergence iterations.
    
    :param script_filepath: Path to the script file.
    :param value: Number of iterations the solver must run after crossing the convergence threshold.
    
    Example usage:
    set_solver_convergence_iterations('path_to_script.txt')
    """
    
    # Type and value checking
    if not isinstance(value, int):
        raise ValueError("`value` should be an integer value.")
    
    lines = [
        "#************************************************************************************",
        "#************** Set the solver convergence iterations *********************************",
        "#************************************************************************************",
        "",
        f"SET_SOLVER_CONVERGENCE_ITERATIONS {value}"
    ]

    write_lines_to_file(script_filepath, lines)
    return


def set_wake_streamwise_agglomeration(script_filepath, enable=True):
    """
    Writes specific lines to 'script_filepath' to enable/disable the wake-->streamwise agglomeration feature.
    
    :param script_filepath: Path to the script file.
    :param enable: Boolean value to enable or disable the wake-->streamwise agglomeration feature.
    
    Example usage:
    set_wake_streamwise_agglomeration('path_to_script.txt')
    """
    
    # Type and value checking
    if not isinstance(enable, bool):
        raise ValueError("`enable` should be a boolean value.")
    
    status = "ENABLE" if enable else "DISABLE"
    
    lines = [
        "#************************************************************************",
        "#********* Enable the wake-->streamwise agglomeration feature ************",
        "#************************************************************************",
        "",
        f"SET_WAKE_STREAMWISE_AGGLOMERATION {status}"
    ]

    write_lines_to_file(script_filepath, lines)
    return

