from .utils import *

def create_new_coordinate_system(script_filepath):
    """
    Writes specific lines to 'script_filepath' to create a new coordinate system.
    
    Example usage:
    create_new_coordinate_system('path_to_script.txt')

    :param script_filepath: Path to the script file.
    """
    
    lines = [
        "#************************************************************************",
        "#****************** Create a new coordinate system **********************",
        "#************************************************************************",
        "",
        "CREATE_NEW_COORDINATE_SYSTEM"
    ]

    write_lines_to_file(script_filepath, lines)
    return

def edit_coordinate_system(script_filepath, frame, name, origin_x, origin_y, origin_z, 
                           vector_x_x, vector_x_y, vector_x_z, 
                           vector_y_x, vector_y_y, vector_y_z,
                           vector_z_x, vector_z_y, vector_z_z):
    """
    Writes specific lines to 'script_filepath' to edit a local coordinate system.

    Example usage:
    edit_coordinate_system('path_to_script.txt', 2, "Prop-1", 0, 1, 0.5,
                           1, 0, 0, 0, -1, 0, 0, 0, -1.2)

    :param script_filepath: Path to the script file.
    :param frame: Index of the local coordinate system.
    :param name: Name of the local coordinate system.
    :param origin_x: X coordinate of the origin.
    :param origin_y: Y coordinate of the origin.
    :param origin_z: Z coordinate of the origin.
    :param vector_x_x: X component of the X axis vector.
    :param vector_x_y: Y component of the X axis vector.
    :param vector_x_z: Z component of the X axis vector.
    :param vector_y_x: X component of the Y axis vector.
    :param vector_y_y: Y component of the Y axis vector.
    :param vector_y_z: Z component of the Y axis vector.
    :param vector_z_x: X component of the Z axis vector.
    :param vector_z_y: Y component of the Z axis vector.
    :param vector_z_z: Z component of the Z axis vector.
    """

    # Type and value checking
    if not isinstance(frame, int) or frame <= 1:
        raise ValueError("`frame` should be an integer greater than 1.")
    if not all(isinstance(val, (int, float)) for val in [origin_x, origin_y, origin_z, 
                                                         vector_x_x, vector_x_y, vector_x_z,
                                                         vector_y_x, vector_y_y, vector_y_z,
                                                         vector_z_x, vector_z_y, vector_z_z]):
        raise ValueError("Coordinates and vector components should be integer or float values.")

    lines = [
        "#************************************************************************",
        "#****************** Edit a local coordinate system **********************",
        "#************************************************************************",
        "",
        "EDIT_COORDINATE_SYSTEM",
        f"FRAME {frame}",
        f"NAME {name}",
        f"ORIGIN_X {origin_x}",
        f"ORIGIN_Y {origin_y}",
        f"ORIGIN_Z {origin_z}",
        f"VECTOR_X_X {vector_x_x}",
        f"VECTOR_X_Y {vector_x_y}",
        f"VECTOR_X_Z {vector_x_z}",
        f"VECTOR_Y_X {vector_y_x}",
        f"VECTOR_Y_Y {vector_y_y}",
        f"VECTOR_Y_Z {vector_y_z}",
        f"VECTOR_Z_X {vector_z_x}",
        f"VECTOR_Z_Y {vector_z_y}",
        f"VECTOR_Z_Z {vector_z_z}"
    ]

    write_lines_to_file(script_filepath, lines)
    return

def set_coordinate_system_name(script_filepath, frame, name):
    """
    Writes specific lines to 'script_filepath' to set the name of an existing local coordinate system.
    
    Example usage:
    set_coordinate_system_name('path_to_script.txt', 2, 'Propeller_Axis')
    
    :param script_filepath: Path to the script file.
    :param frame: Index of the local coordinate system.
    :param name: New name of the coordinate system.
    """
    
    # Type and value checking
    if not isinstance(frame, int):
        raise ValueError("`frame` should be an integer value.")
    
    if frame <= 1:
        raise ValueError("`frame` should be greater than 1.")
    
    if not isinstance(name, str):
        raise ValueError("`name` should be a string.")
    
    lines = [
        "#************************************************************************",
        "#********* Set the name of an existing local coordinate system **********",
        "#************************************************************************",
        "",
        f"SET_COORDINATE_SYSTEM_NAME {frame} {name}"
    ]

    write_lines_to_file(script_filepath, lines)
    return

def set_coordinate_system_origin(script_filepath, frame, x, y, z, units='INCH'):
    """
    Writes specific lines to 'script_filepath' to set the origin of an existing local 
    coordinate system.
    
    Example usage:
    set_coordinate_system_origin('path_to_script.txt', 2, 0.0, 1.0, 1.4, 'INCH')
    
    :param script_filepath: Path to the script file.
    :param frame: Index of the local coordinate system.
    :param x: Origin position in X relative to the reference coordinate system.
    :param y: Origin position in Y relative to the reference coordinate system.
    :param z: Origin position in Z relative to the reference coordinate system.
    :param units: Units of the position values.
    """
    
    # Type and value checking
    if not isinstance(frame, int) or frame <= 1:
        raise ValueError("`frame` should be an integer greater than 1.")
    
    if not isinstance(x, (int, float)) or not isinstance(y, (int, float)) or not isinstance(z, (int, float)):
        raise ValueError("`x`, `y`, and `z` should be integer or float values.")
    
    check_valid_units(units)
    
    lines = [
        "#************************************************************************",
        "#********* Set the origin of an existing local coordinate system ********",
        "#************************************************************************",
        "",
        f"SET_COORDINATE_SYSTEM_ORIGIN {frame} {x} {y} {z} {units}"
    ]

    write_lines_to_file(script_filepath, lines)
    return

