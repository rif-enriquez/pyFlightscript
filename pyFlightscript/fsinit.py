from .utils import *    
from .script_state import script

def open_fsm(fsm_filepath):
    """
    FS: Opens a flightstream file. 
    python:  Writes a script with specific lines to '', 
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

    script.append_lines(lines)
    return

def stop_script():
    """
    Writes specific lines indicating a script stop to ''.
    """
    lines = [
        "#************************************************************************",
        "#*********** Stop a script at this location in the script file **********",
        "#************************************************************************",
        "#",
        "STOP"
    ]

    script.append_lines(lines)
    return

def save_as_fsm(fsm_filepath):
    """
    Appends lines to script state to save an existing simulation file,
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

    script.append_lines(lines)
    return

def create_new_simulation():
    """
    Appends lines to script state to create a new simulation.
    """
    lines = [
        "#************************************************************************",
        "#****************** Create a new simulation *****************************",
        "#************************************************************************",
        "#",
        "NEW_SIMULATION"
    ]

    script.append_lines(lines)
    return

def set_significant_digits(digits=5):
    """
    Appends lines to script state to set the number of significant digits.
    
    :param : Path to the script file.
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

    script.append_lines(lines)
    return

def set_vertex_merge_tolerance(tolerance='1E-5'):
    """
    Appends lines to script state to set the vertex merge tolerance.
    
    :param : Path to the script file.
    :param tolerance: Vertex merge tolerance value.
    """
    lines = [
        "#************************************************************************",
        "#****************** Set vertex merge tolerance **************************",
        "#************************************************************************",
        "#",
        f"SET_VERTEX_MERGE_TOLERANCE {tolerance}"
    ]

    script.append_lines(lines)
    return

def set_simulation_length_units(units='METER'):
    """
    Appends lines to script state to set the simulation length scale units.
    Checks if the provided unit is valid.
    
    :param : Path to the script file.
    :param units: Desired simulation length unit.
    :raises ValueError: If the provided unit is not valid.
    """
    check_valid_length_units(units)

    lines = [
        "#************************************************************************",
        "#****************** Set simulation length scale units *******************",
        "#************************************************************************",
        "#",
        f"SET_SIMULATION_LENGTH_UNITS {units}"
    ]

    script.append_lines(lines)
    return

def set_trailing_edge_sweep_angle(angle=45.):
    """
    Appends lines to script state to set the trailing edge sweep angle.
    Checks if the provided angle is within the valid range.
    
    :param : Path to the script file.
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

    script.append_lines(lines)
    return

def set_trailing_edge_bluntness_angle(angle=85.):
    """
    Appends lines to script state to set the trailing edge bluntness angle.
    Checks if the provided angle is within the valid range.
    
    :param : Path to the script file.
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

    script.append_lines(lines)
    return

def set_base_region_bending_angle(angle=25.):
    """
    Appends lines to script state to set the base region bending angle.
    Checks if the provided angle is within the valid range.
    
    :param : Path to the script file.
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

    script.append_lines(lines)
    return
