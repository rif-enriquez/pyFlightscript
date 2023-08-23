import os
from .utils import *

def create_new_actuator(script_filepath, actuator_type='PROPELLER'):
    """
    Writes specific lines to 'script_filepath' to create a new actuator.
    
    Example usage:
    create_new_actuator('path_to_script.txt')
    
    :param script_filepath: Path to the script file.
    :param actuator_type: Type of the actuator, either 'PROPELLER' or 'JET_EXHAUST'.
    """
    
    # Type and value checking
    valid_types = ['PROPELLER', 'JET_EXHAUST']
    if actuator_type not in valid_types:
        raise ValueError(f"`actuator_type` should be one of {valid_types}")
    
    lines = [
        "#************************************************************************",
        "#****************** Create a new propeller actuator ********************",
        "#************************************************************************",
        "",
        "CREATE_NEW_ACTUATOR",
        f"TYPE {actuator_type}"
    ]

    write_lines_to_file(script_filepath, lines)
    return

def edit_actuator(script_filepath, actuator, name, actuator_type, frame, axis, 
                  offset, radius, ct=None, rpm=None, swirl_velocity=None, 
                  velocity=None, density=None, cm=None):
    """
    Example usage:
        edit_actuator('path_to_script.txt', 1, "Prop-1", "PROPELLER", 2, 1, 0.5, 
                      1.2, ct=0.013, rpm=7000, swirl_velocity="ENABLE")
    
    Writes specific lines to 'script_filepath' to edit an actuator.
    
    :param script_filepath: Path to the script file.
    :param actuator: Index of the actuator to be edited.
    :param name: Name to be assigned to the selected actuator.
    :param actuator_type: Type of the actuator (PROPELLER or JET_EXHAUST).
    :param frame: Index of the coordinate system to be used for this actuator.
    :param axis: Directional axis for the actuator disc.
    :param offset: Offset distance along the axis for the actuator disc.
    :param radius: Radius of the actuator disc.
    :param ct: Thrust coefficient of the propeller (for PROPELLER type only).
    :param rpm: RPM of the propeller (for PROPELLER type only).
    :param swirl_velocity: ENABLE/DISABLE swirl velocity (for PROPELLER type only).
    :param velocity: Exhaust velocity (for JET_EXHAUST type only).
    :param density: Density of the exhaust jet (for JET_EXHAUST type only).
    :param cm: Jet spreading coefficient (for JET_EXHAUST type only).
    """
    
    # Type and value checking
    if not isinstance(actuator, int) or actuator <= 0:
        raise ValueError("`actuator` should be an integer greater than 0.")
    
    if not isinstance(frame, int) or frame <= 0:
        raise ValueError("`frame` should be an integer greater than 0.")
    
    if actuator_type not in ['PROPELLER', 'JET_EXHAUST']:
        raise ValueError("`actuator_type` should be either 'PROPELLER' or 'JET_EXHAUST'.")
    
    if axis not in [1, 2, 3]:
        raise ValueError("`axis` should be one of [1, 2, 3] corresponding to X, Y, Z axes.")
    
    lines = [
        "#************************************************************************",
        "#****************** Edit a propeller actuator here *********************",
        "#************************************************************************",
        "",
        "EDIT_ACTUATOR",
        f"ACTUATOR {actuator}",
        f"NAME {name}",
        f"TYPE {actuator_type}",
        f"FRAME {frame}",
        f"AXIS {axis}",
        f"OFFSET {offset}",
        f"RADIUS {radius}",
    ]
    
    if actuator_type == 'PROPELLER':
        if ct is not None:
            lines.append(f"CT {ct}")
        if rpm is not None:
            lines.append(f"RPM {rpm}")
        if swirl_velocity in ["ENABLE", "DISABLE"]:
            lines.append(f"SWIRL_VELOCITY {swirl_velocity}")
        else:
            raise ValueError("`swirl_velocity` should be either 'ENABLE' or 'DISABLE'.")
    
    elif actuator_type == 'JET_EXHAUST':
        if velocity is not None:
            lines.append(f"VELOCITY {velocity}")
        if density is not None:
            lines.append(f"DENSITY {density}")
        if cm is not None:
            lines.append(f"CM {cm}")
    
    write_lines_to_file(script_filepath, lines)
    return

def set_prop_actuator_rpm(script_filepath, actuator_index=1, rpm=2000):
    """
    Writes specific lines to 'script_filepath' to set the RPM of an actuator.
    
    Example usage:
    set_prop_actuator_rpm('path_to_script.txt', 2, -3400)

    :param script_filepath: Path to the script file.
    :param actuator_index: Index of the actuator whose properties are being set.
    :param rpm: RPM of the propeller actuator.
    """
    
    # Type and value checking
    if not isinstance(actuator_index, int) or actuator_index <= 0:
        raise ValueError("`actuator_index` should be an integer value greater than 0.")
    
    if not isinstance(rpm, (int, float)):
        raise ValueError("`rpm` should be an integer or float value.")
    
    lines = [
        "#************************************************************************",
        "#****************** Set the RPM of an existing actuator *****************",
        "#************************************************************************",
        "",
        f"SET_PROP_ACTUATOR_RPM {actuator_index} {rpm}"
    ]

    write_lines_to_file(script_filepath, lines)
    return

def set_prop_actuator_thrust(script_filepath, actuator_index, ct, thrust_type='COEFFICIENT'):
    """
    Writes specific lines to 'script_filepath' to set the thrust coefficient of an existing actuator.
    
    :param script_filepath: Path to the script file.
    :param actuator_index: Index of the actuator whose properties are being set.
    :param ct: Thrust coefficient of the propeller.
    :param thrust_type: Units for the thrust force.

    Example usage:
    set_prop_actuator_thrust('path_to_script.txt', 2, 0.034)
    """
    
    # Type and value checking
    if not isinstance(actuator_index, int) or actuator_index <= 0:
        raise ValueError("`actuator_index` should be a positive integer value.")
    
    if not isinstance(ct, (int, float)) or ct <= 0:
        raise ValueError("`ct` should be a positive integer or float value.")
    
    valid_thrust_types = ['COEFFICIENT', 'NEWTONS', 'POUNDS']
    if thrust_type not in valid_thrust_types:
        raise ValueError(f"`thrust_type` should be one of {valid_thrust_types}")
    
    lines = [
        "#************************************************************************",
        "#********* Set the thrust coefficient of an existing actuator ***********",
        "#************************************************************************",
        "",
        f"SET_PROP_ACTUATOR_THRUST {actuator_index} {ct} {thrust_type}"
    ]

    write_lines_to_file(script_filepath, lines)
    return

def set_prop_actuator_swirl(script_filepath, actuator_index, status='DISABLE'):
    """
    Writes specific lines to 'script_filepath' to toggle the swirl velocity selection.
    
    :param script_filepath: Path to the script file.
    :param actuator_index: Index of the actuator whose properties are being set.
    :param status: Either 'ENABLE' or 'DISABLE'.
    
    Example usage:
    set_prop_actuator_swirl('path_to_script.txt', 3)
    """

    # Type and value checking
    if not isinstance(actuator_index, int) or actuator_index <= 0:
        raise ValueError("`actuator_index` should be an integer greater than 0.")
    
    valid_statuses = ['ENABLE', 'DISABLE']
    if status not in valid_statuses:
        raise ValueError(f"`status` should be one of {valid_statuses}")
    
    lines = [
        "#************************************************************************",
        "#****************** Toggle the swirl velocity selection *****************",
        "#************************************************************************",
        "",
        f"SET_PROP_ACTUATOR_SWIRL {actuator_index} {status}"
    ]

    write_lines_to_file(script_filepath, lines)
    return

def enable_actuator(script_filepath, actuator_id):
    """
    Writes specific lines to 'script_filepath' to enable an existing actuator.
    
    Example usage:
    >>> enable_actuator('path_to_script.txt', 2)
    
    :param script_filepath: Path to the script file.
    :param actuator_id: ID of the actuator to be enabled.
    """
    
    # Type and value checking
    if not isinstance(actuator_id, int) or actuator_id < 0:
        raise ValueError("`actuator_id` should be a non-negative integer value.")
    
    lines = [
        "#************************************************************************",
        "#****************** Enable an existing actuator *************************",
        "#************************************************************************",
        "",
        f"ENABLE_ACTUATOR {actuator_id}"
    ]

    write_lines_to_file(script_filepath, lines)
    return

def disable_actuator(script_filepath, actuator_id):
    """
    Writes specific lines to 'script_filepath' to disable an existing actuator.
    
    Example usage:
    disable_actuator('path_to_script.txt', 2)
    
    :param script_filepath: Path to the script file.
    :param actuator_id: ID of the actuator to disable.
    """
    
    # Type and value checking
    if not isinstance(actuator_id, int):
        raise ValueError("`actuator_id` should be an integer value.")
    
    lines = [
        "#************************************************************************",
        "#****************** Disable an existing actuator ************************",
        "#************************************************************************",
        "",
        f"DISABLE_ACTUATOR {actuator_id}"
    ]

    write_lines_to_file(script_filepath, lines)
    return

def delete_actuator(script_filepath, actuator_index):
    """
    Writes specific lines to 'script_filepath' to delete an actuator.
    
    Example usage:
    delete_actuator('path_to_script.txt', 1)

    :param script_filepath: Path to the script file.
    :param actuator_index: Index of the actuator to be deleted.
    """
    
    # Type and value checking
    if not isinstance(actuator_index, int) or actuator_index <= 0:
        raise ValueError("`actuator_index` should be an integer value greater than 0.")
    
    lines = [
        "#************************************************************************",
        "#****************** Delete an actuator **********************************",
        "#************************************************************************",
        "",
        "DELETE_ACTUATOR",
        f"ACTUATOR {actuator_index}"
    ]

    write_lines_to_file(script_filepath, lines)
    return