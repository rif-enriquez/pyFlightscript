from .utils import *

def open_fsm(script_filepath, fsm_filepath):
    """
    FS: Opens a flightstream file. 
    python:  Writes a script with specific lines to 'script_filepath', 
      inserting the path from 'fsm_filepath' where necessary.
    """
    lines = [
        "#************************************************************************",
        "#****************** Open an existing simulation file ********************",
        "#************************************************************************",
        "#",
        "OPEN",
        fsm_filepath  # Replace the path with the provided input_filename
    ]

    write_lines_to_file(script_filepath, lines)
    return

def stop_script(script_filepath):
    """
    Writes specific lines indicating a script stop to 'script_filepath'.
    """
    lines = [
        "#************************************************************************",
        "#*********** Stop a script at this location in the script file **********",
        "#************************************************************************",
        "#",
        "STOP"
    ]

    write_lines_to_file(script_filepath, lines)
    return

def save_as_fsm(script_filepath, fsm_filepath):
    """
    Writes specific lines to 'script_filepath' to save an existing simulation file,
    using the path from 'fsm_filepath'.
    """
    lines = [
        "#************************************************************************",
        "#****************** Save an existing simulation file ********************",
        "#************************************************************************",
        "#",
        "SAVEAS",
        fsm_filepath
    ]

    write_lines_to_file(script_filepath, lines)
    return

def create_new_simulation(script_filepath):
    """
    Writes specific lines to 'script_filepath' to create a new simulation.
    """
    lines = [
        "#************************************************************************",
        "#****************** Create a new simulation *****************************",
        "#************************************************************************",
        "#",
        "NEW_SIMULATION"
    ]

    write_lines_to_file(script_filepath, lines)
    return

def set_significant_digits(script_filepath, digits=5):
    """
    Writes specific lines to 'script_filepath' to set the number of significant digits.
    
    :param script_filepath: Path to the script file.
    :param digits: Number of significant digits.
    """
    if not isinstance(digits, int):
        raise ValueError("Digits should be an integer ")
    
    lines = [
        "#************************************************************************",
        "#****************** Set significant digits ******************************",
        "#************************************************************************",
        "#",
        f"SET_SIGNIFICANT_DIGITS {digits}"
    ]

    write_lines_to_file(script_filepath, lines)
    return

def set_vertex_merge_tolerance(script_filepath, tolerance='1E-5'):
    """
    Writes specific lines to 'script_filepath' to set the vertex merge tolerance.
    
    :param script_filepath: Path to the script file.
    :param tolerance: Vertex merge tolerance value.
    """
    lines = [
        "#************************************************************************",
        "#****************** Set vertex merge tolerance **************************",
        "#************************************************************************",
        "#",
        f"SET_VERTEX_MERGE_TOLERANCE {tolerance}"
    ]

    write_lines_to_file(script_filepath, lines)
    return

def set_simulation_length_units(script_filepath, units='METER'):
    """
    Writes specific lines to 'script_filepath' to set the simulation length scale units.
    Checks if the provided unit is valid.
    
    :param script_filepath: Path to the script file.
    :param units: Desired simulation length unit.
    :raises ValueError: If the provided unit is not valid.
    """
    check_valid_units(units)

    lines = [
        "#************************************************************************",
        "#****************** Set simulation length scale units *******************",
        "#************************************************************************",
        "#",
        f"SET_SIMULATION_LENGTH_UNITS {units}"
    ]

    write_lines_to_file(script_filepath, lines)
    return

def set_trailing_edge_sweep_angle(script_filepath, angle=45.):
    """
    Writes specific lines to 'script_filepath' to set the trailing edge sweep angle.
    Checks if the provided angle is within the valid range.
    
    :param script_filepath: Path to the script file.
    :param angle: Desired trailing edge sweep angle in degrees.
    :raises ValueError: If the provided angle is not within [0, 90].
    """
    if not (0 <= angle <= 90):
        raise ValueError("Invalid angle: {}. Must be in the range [0, 90].".format(angle))

    if not isinstance(angle, (int, float)):
        raise ValueError("Angle should be a numeric value.")
    
    lines = [
        "#************************************************************************",
        "#****************** Set trailing edge sweep angle ***********************",
        "#************************************************************************",
        "#",
        f"SET_TRAILING_EDGE_SWEEP_ANGLE {angle}"
    ]

    write_lines_to_file(script_filepath, lines)
    return

def set_trailing_edge_bluntness_angle(script_filepath, angle=85.):
    """
    Writes specific lines to 'script_filepath' to set the trailing edge bluntness angle.
    Checks if the provided angle is within the valid range.
    
    :param script_filepath: Path to the script file.
    :param angle: Desired trailing edge bluntness angle in degrees.
    :raises ValueError: If the provided angle is not within [45, 179].
    """
    if not (45 <= angle <= 179):
        raise ValueError("Invalid angle: {}. Must be in the range [45, 179].".format(angle))

    if not isinstance(angle, (int, float)):
        raise ValueError("Angle should be a numeric value.")
    
    lines = [
        "#************************************************************************",
        "#****************** Set trailing edge bluntness angle *******************",
        "#************************************************************************",
        "#",
        f"SET_TRAILING_EDGE_BLUNTNESS_ANGLE {angle}"
    ]

    write_lines_to_file(script_filepath, lines)
    return

def set_base_region_bending_angle(script_filepath, angle=25.):
    """
    Writes specific lines to 'script_filepath' to set the base region bending angle.
    Checks if the provided angle is within the valid range.
    
    :param script_filepath: Path to the script file.
    :param angle: Desired base region bending angle in degrees.
    :raises ValueError: If the provided angle is not within [0, 90].
    """
    if not (0 <= angle <= 90):
        raise ValueError("Invalid angle: {}. Must be in the range [0, 90].".format(angle))

    if not isinstance(angle, (int, float)):
        raise ValueError("Angle should be a numeric value.")
    
    lines = [
        "#************************************************************************",
        "#****************** Set base region bending angle ***********************",
        "#************************************************************************",
        "#",
        f"SET_BASE_REGION_BENDING_ANGLE {angle}"
    ]

    write_lines_to_file(script_filepath, lines)
    return
