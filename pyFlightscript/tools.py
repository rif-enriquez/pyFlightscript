from .utils import *    
from .script_state import script

def execute_solver_sweeper(sweep_results_path, results_filename,
                           angle_of_attack='ENABLE', side_slip_angle='DISABLE', 
                           velocity='DISABLE', angle_of_attack_start=0.0, 
                           angle_of_attack_stop=0., angle_of_attack_delta=1.,
                           side_slip_angle_start=0., side_slip_angle_stop=0., 
                           side_slip_angle_delta=1.0, velocity_start=0., 
                           velocity_stop=0.0, velocity_delta=1.0, 
                           export_surface_data_per_step='ENABLE', 
                           clear_solution_after_each_run='ENABLE',
                           reference_velocity_equals_freestream='ENABLE',
                           append_to_existing_sweep='DISABLE'):
    """
    Appends lines to script state to execute the solver sweeper.
    
    Example usage:
    execute_solver_sweeper('path_to_script.txt', angle_of_attack='ENABLE', 
                           side_slip_angle='DISABLE', velocity='DISABLE', 
                           angle_of_attack_start=0.0, angle_of_attack_stop=10.0,
                           angle_of_attack_delta=1.0, export_surface_data_per_step='ENABLE',
                           sweep_results_path='C:\\...\\sweep_results\\', 
                           clear_solution_after_each_run='ENABLE')
    

    :... other parameters ...
    """
    
    # Type and value checking
    valid_options = ['ENABLE', 'DISABLE']
    if angle_of_attack not in valid_options or side_slip_angle not in valid_options or \
       velocity not in valid_options or export_surface_data_per_step not in valid_options or \
       clear_solution_after_each_run not in valid_options or \
       reference_velocity_equals_freestream not in valid_options or \
       append_to_existing_sweep not in valid_options:
        raise ValueError("Only 'ENABLE' or 'DISABLE' are valid options for the respective fields.")
    
    # Create lines based on the given values
    lines = [
        "#************************************************************************",
        "#****************** Initialize and execute the solver sweeper ***********",
        "#************************************************************************",
        "",
        "EXECUTE_SOLVER_SWEEPER",
        f"ANGLE_OF_ATTACK {angle_of_attack}",
        f"SIDE_SLIP_ANGLE {side_slip_angle}",
        f"VELOCITY {velocity}",
        f"ANGLE_OF_ATTACK_START {angle_of_attack_start}",
        f"ANGLE_OF_ATTACK_STOP {angle_of_attack_stop}",
        f"ANGLE_OF_ATTACK_DELTA {angle_of_attack_delta}",
        f"SIDE_SLIP_ANGLE_START {side_slip_angle_start}",
        f"SIDE_SLIP_ANGLE_STOP {side_slip_angle_stop}",
        f"SIDE_SLIP_ANGLE_DELTA {side_slip_angle_delta}",
        f"VELOCITY_START {velocity_start}",
        f"VELOCITY_STOP {velocity_stop}",
        f"VELOCITY_DELTA {velocity_delta}",
        f"EXPORT_SURFACE_DATA_PER_STEP {export_surface_data_per_step}",
        f"{sweep_results_path}",
        f"CLEAR_SOLUTION_AFTER_EACH_RUN {clear_solution_after_each_run}",
        f"REFERENCE_VELOCITY_EQUALS_FREESTREAM {reference_velocity_equals_freestream}",
        f"APPEND_TO_EXISTING_SWEEP {append_to_existing_sweep}",
        f"{results_filename}"
    ]

    script.append_lines(lines)
    return


def set_stability_toolbox(longitudinal='ENABLE', lateral='ENABLE', 
                          longitudinal_ref_length=1.5, lateral_ref_length=0.5, 
                          units='PER_DEGREE', clear_solver_per_run='DISABLE'):
    """
    Appends lines to script state to set the S&C toolbox parameters.


    :param longitudinal: ENABLE or DISABLE computation of longitudinal stability coefficients.
    :param lateral: ENABLE or DISABLE computation of lateral stability coefficients.
    :param longitudinal_ref_length: Value of the reference length used in computing the longitudinal stability coefficients.
    :param lateral_ref_length: Value of the reference length used in computing the lateral stability coefficients.
    :param units: PER_RADIAN or PER_DEGREE (only for dynamic stability coefficients).
    :param clear_solver_per_run: ENABLE or DISABLE clearing of the solution prior to each solver run.

    Example usage:
    >>> set_stability_toolbox('path_to_script.txt')
    """
    
    valid_options = ['ENABLE', 'DISABLE']
    
    if longitudinal not in valid_options:
        raise ValueError(f"`longitudinal` should be one of {valid_options}")

    if lateral not in valid_options:
        raise ValueError(f"`lateral` should be one of {valid_options}")

    if not isinstance(longitudinal_ref_length, (int, float)):
        raise ValueError("`longitudinal_ref_length` should be an integer or float value.")
        
    if not isinstance(lateral_ref_length, (int, float)):
        raise ValueError("`lateral_ref_length` should be an integer or float value.")

    valid_units = ['PER_RADIAN', 'PER_DEGREE']
    if units not in valid_units:
        raise ValueError(f"`units` should be one of {valid_units}")

    if clear_solver_per_run not in valid_options:
        raise ValueError(f"`clear_solver_per_run` should be one of {valid_options}")

    lines = [
        "#************************************************************************",
        "#****************** Set the S&C toolbox parameters here *****************",
        "#************************************************************************",
        "",
        "SET_STABILITY_TOOLBOX",
        f"LONGITUDINAL {longitudinal}",
        f"LATERAL {lateral}",
        f"LONGITUDINAL_REF_LENGTH {longitudinal_ref_length}",
        f"LATERAL_REF_LENGTH {lateral_ref_length}",
        f"UNITS {units}",
        f"CLEAR_SOLVER_PER_RUN {clear_solver_per_run}"
    ]

    script.append_lines(lines)
    return

def compute_static_stability():
    """
    Appends lines to script state to compute the static stability coefficients.



    Example usage:
    >>> compute_static_stability('path_to_script.txt')
    """
    
    lines = [
        "#************************************************************************",
        "#****************** Compute the static stability coefficients ***********",
        "#************************************************************************",
        "",
        "COMPUTE_STATIC_STABILITY"
    ]

    script.append_lines(lines)
    return

def compute_dynamic_stability():
    """
    Appends lines to script state to compute the dynamic stability coefficients.
    

    
    Example usage:
        compute_dynamic_stability('path_to_script.txt')
    """
    
    lines = [
        "#************************************************************************",
        "#****************** Compute the dynamic stability coefficients **********",
        "#************************************************************************",
        "",
        "COMPUTE_DYNAMIC_STABILITY"
    ]

    script.append_lines(lines)
    return

def export_stability_results(filename):
    """
    Appends lines to script state to export the S&C toolbox results to an external file.
    

    :param filename: Filename with its path for the exported results.
    
    Example usage:
        export_stability_results('path_to_script.txt', 'C:\\...\\Testing cases\\another_test.txt')
    """
    
    # Type and value checking
    if not isinstance(filename, str):
        raise ValueError("`filename` should be a string.")
    
    lines = [
        "#************************************************************************",
        "#*********** Export the S&C toolbox results to external file ************",
        "#************************************************************************",
        "",
        "EXPORT_STABILITY_RESULTS",
        f"{filename}"
    ]

    script.append_lines(lines)
    return
