import os
from .utils import *    
from .script_state import script

def set_freestream(freestream_type, profile_path=None, frame=None, axis=None, angular_velocity=None):
    """
    Appends lines to script state to set a freestream velocity type.
    

    :param freestream_type: Type of the freestream ('CONSTANT', 'CUSTOM', or 'ROTATION').
    :param profile_path: (Optional) Path to the custom velocity profile. Needed for 'CUSTOM' type.
    :param frame: (Optional) Index of the coordinate system used for defining the rotation. Needed for 'ROTATION' type.
    :param axis: (Optional) Axis of the chosen coordinate system used for rotation ('X', 'Y', or 'Z'). Needed for 'ROTATION' type.
    :param angular_velocity: (Optional) Rotational velocity in rad/sec. Needed for 'ROTATION' type.
    
    Example usage:
    set_freestream('path_to_script.txt', 'CONSTANT')
    set_freestream('path_to_script.txt', 'CUSTOM', profile_path='C:/.../Custom_freestream_profile.txt')
    set_freestream('path_to_script.txt', 'ROTATION', frame=1, axis='X', angular_velocity=-0.2)
    """
    
    # Type and value checking
    valid_types = ['CONSTANT', 'CUSTOM', 'ROTATION']
    if freestream_type not in valid_types:
        raise ValueError(f"`freestream_type` should be one of {valid_types}")
    
    lines = []
    if freestream_type == 'CONSTANT':
        lines.extend([
            "#************************************************************************",
            "#**************** Set a constant free-stream velocity *******************",
            "#************************************************************************",
            "",
            "SET_FREESTREAM CONSTANT"
        ])

    elif freestream_type == 'CUSTOM':
        if not profile_path:
            raise ValueError("For `CUSTOM` freestream_type, `profile_path` must be provided.")
        lines.extend([
            "#************************************************************************",
            "#*************** Set a custom free-stream velocity ********************",
            "#************************************************************************",
            "",
            "SET_FREESTREAM CUSTOM",
            profile_path
        ])

    else:  # ROTATION
        if not frame or not axis or angular_velocity is None:
            raise ValueError("For `ROTATION` freestream_type, `frame`, `axis`, and `angular_velocity` must be provided.")
        valid_axes = ['X', 'Y', 'Z']
        if axis not in valid_axes:
            raise ValueError(f"`axis` should be one of {valid_axes}")
        
        lines.extend([
            "#************************************************************************",
            "#*************** Set a rotational free-stream velocity ******************",
            "#************************************************************************",
            "",
            f"SET_FREESTREAM ROTATION {frame} {axis} {angular_velocity}"
        ])
    
    script.append_lines(lines)
    return

def fluid_properties(density=0.5, pressure=65234.35, sonic_velocity=230,
                     temperature=295.0, viscosity=0.0005):
    """
    Appends lines to script state to set the fluid properties.
    
    Example usage:
        fluid_properties('path_to_script.txt')
    

    :param density: Density value (kg/m^3).
    :param pressure: Static pressure value (Pa).
    :param sonic_velocity: Sonic velocity (m/sec).
    :param temperature: Temperature value (K).
    :param viscosity: Viscosity value (Pa-sec).
    """
    
    # Type and value checking
    if not isinstance(density, (int, float)):
        raise ValueError("`density` should be an integer or float value.")
    
    if not isinstance(pressure, (int, float)):
        raise ValueError("`pressure` should be an integer or float value.")
    
    if not isinstance(sonic_velocity, (int, float)):
        raise ValueError("`sonic_velocity` should be an integer or float value.")
    
    if not isinstance(temperature, (int, float)):
        raise ValueError("`temperature` should be an integer or float value.")
    
    if not isinstance(viscosity, (int, float)):
        raise ValueError("`viscosity` should be an integer or float value.")
    
    lines = [
        "#************************************************************************",
        "#********* Set the fluid properties *************************************",
        "#************************************************************************",
        "",
        "FLUID_PROPERTIES",
        f"DENSITY {density}",
        f"PRESSURE {pressure}",
        f"SONIC_VELOCITY {sonic_velocity}",
        f"TEMPERATURE {temperature}",
        f"VISCOSITY {viscosity}"
    ]

    script.append_lines(lines)
    return

def air_altitude(altitude=15000.0):
    """
    Appends lines to script state to set fluid (air) properties based on altitude.

    Example usage:
    air_altitude('path_to_script.txt')


    :param altitude: Altitude value in feet.
    """
    
    # Type and value checking
    if not isinstance(altitude, (int, float)):
        raise ValueError("`altitude` should be an integer or float value.")
    
    lines = [
        "#************************************************************************",
        "#********* Set the fluid (air) properties based on altitude *************",
        "#************************************************************************",
        "",
        f"AIR_ALTITUDE {altitude}"
    ]

    script.append_lines(lines)
    return

