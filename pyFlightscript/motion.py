from .utils import *

def create_new_motion_euclidean(script_filepath):
    """
    Writes specific lines to 'script_filepath' to create a new Euclidean motion definition.
    
    Example usage:
    create_new_motion_euclidean('path_to_script.txt')

    :param script_filepath: Path to the script file.
    """
    
    lines = [
        "#************************************************************************",
        "#************** Create a new Euclidean motion definition ****************",
        "#************************************************************************",
        "",
        "CREATE_NEW_MOTION_EUCLIDEAN"
    ]

    write_lines_to_file(script_filepath, lines)
    return

def create_new_motion_custom(script_filepath):
    """
    Writes specific lines to 'script_filepath' to create a new Custom motion definition.

    Example usage:
    create_new_motion_custom('path_to_script.txt')
    """
    
    lines = [
        "#************************************************************************",
        "#************** Create a new Custom motion definition *******************",
        "#************************************************************************",
        "",
        "CREATE_NEW_MOTION_CUSTOM"
    ]

    write_lines_to_file(script_filepath, lines)
    return


def create_new_motion_6dof(script_filepath):
    """
    Writes specific lines to 'script_filepath' to create a new 6DOF motion definition.
    
    Example usage:
        create_new_motion_6dof('path_to_script.txt')
    
    :param script_filepath: Path to the script file.
    """
    
    lines = [
        "#************************************************************************",
        "#************** Create a new 6DOF motion definition ********************",
        "#************************************************************************",
        "",
        "CREATE_NEW_MOTION_6DOF"
    ]

    write_lines_to_file(script_filepath, lines)
    return

def create_new_motion_fsi(script_filepath):
    """
    Writes specific lines to 'script_filepath' to create a new FSI motion definition.
    
    Example usage:
    create_new_motion_fsi('path_to_script.txt')
    """
    
    lines = [
        "#************************************************************************",
        "#************** Create a new FSI motion definition **********************",
        "#************************************************************************",
        "",
        "CREATE_NEW_MOTION_FSI"
    ]

    write_lines_to_file(script_filepath, lines)
    return

def set_motion_boundaries(script_filepath, motion_id, num_boundaries=-1, boundaries=None):
    """
    Writes specific lines to 'script_filepath' to specify motion boundaries.
    
    :param script_filepath: Path to the script file.
    :param motion_id: Index of the motion definition.
    :param num_boundaries: Number of geometry boundaries being specified.
    :param boundaries: List of geometry boundaries if num_boundaries is not set to -1.
    
    Example usage:
    >>> set_motion_boundaries('path_to_script.txt', 1, 4, [1, 2, 3, 5])
    >>> set_motion_boundaries('path_to_script.txt', 1)
    """

    # Type and value checking
    if not isinstance(motion_id, int) or motion_id <= 0:
        raise ValueError("`motion_id` should be an integer value greater than 0.")
    
    if not isinstance(num_boundaries, int):
        raise ValueError("`num_boundaries` should be an integer value.")
    
    if num_boundaries != -1 and (boundaries is None or not isinstance(boundaries, list)):
        raise ValueError("`boundaries` should be provided and be a list if `num_boundaries` is not -1.")

    lines = [
        "#************************************************************************",
        "#*********** Specify motion definition boundaries *************",
        "#************************************************************************",
        "",
        f"SET_MOTION_BOUNDARIES {motion_id} {num_boundaries}",
    ]
    if num_boundaries != -1:
        boundaries_str = ','.join(map(str, boundaries))
        lines.append(boundaries_str)

    write_lines_to_file(script_filepath, lines)
    return

def set_motion_moving_frames(script_filepath, motion_id, num_frames, frames_list=None):
    """
    Writes specific lines to 'script_filepath' to specify local frames to motion definition.
    
    # Example usage:
    # set_motion_moving_frames('path_to_script1.txt', 1, 4, [1,2,3,5])

    :param script_filepath: Path to the script file.
    :param motion_id: Index of the motion definition.
    :param num_frames: Number of user-defined local coordinate frames.
    :param frames_list: List of frame indices. Only necessary if num_frames > 0.
    """
    
    # Type and value checking
    if not isinstance(motion_id, int) or motion_id <= 0:
        raise ValueError("`motion_id` should be an integer value greater than 0.")
    
    if not isinstance(num_frames, int):
        raise ValueError("`num_frames` should be an integer value.")
    
    if num_frames > 0 and not isinstance(frames_list, list):
        raise ValueError("`frames_list` should be provided and be of type list when `num_frames` is greater than 0.")
    
    # Construct lines
    lines = [
        "#************************************************************************",
        "#*********** Specify specified local frames to motion definition ********",
        "#************************************************************************",
        "",
        f"SET_MOTION_MOVING_FRAMES {motion_id} {num_frames}"
    ]
    
    if frames_list:
        lines.append(",".join(map(str, frames_list)))

    write_lines_to_file(script_filepath, lines)
    return


def set_motion_coordinate_system(script_filepath, motion_id, coordinate_system_id):
    """
    Writes specific lines to 'script_filepath' to set the coordinate system for a motion definition.
    
    # Example usage:
    # set_motion_coordinate_system('path_to_script2.txt', 1, 3)

    :param script_filepath: Path to the script file.
    :param motion_id: Index of the motion definition.
    :param coordinate_system_id: Index of the coordinate system.
    """
    
    # Type and value checking
    if not isinstance(motion_id, int) or motion_id <= 0:
        raise ValueError("`motion_id` should be an integer value greater than 0.")
    
    if not isinstance(coordinate_system_id, int) or coordinate_system_id <= 0:
        raise ValueError("`coordinate_system_id` should be an integer value greater than 0.")
    
    # Construct lines
    lines = [
        "#************************************************************************",
        "#********** Set the coordinate system for a motion definition ***********",
        "#************************************************************************",
        "",
        f"SET_MOTION_COORDINATE_SYSTEM {motion_id} {coordinate_system_id}"
    ]

    write_lines_to_file(script_filepath, lines)
    return

def set_motion_start_time(script_filepath, motion_id, start_time=0.0):
    """
    Writes specific lines to 'script_filepath' to set the start time for a motion definition.
    
    :param script_filepath: Path to the script file.
    :param motion_id: Index of the motion definition.
    :param start_time: Start time for the motion within the solver physical time.
    
    Example usage:
    set_motion_start_time('path_to_script.txt', 1, 2.5)
    """
    
    # Type and value checking
    if not isinstance(motion_id, int) or motion_id <= 0:
        raise ValueError("`motion_id` should be an integer value greater than 0.")
    
    if not isinstance(start_time, float) or start_time < 0.0:
        raise ValueError("`start_time` should be a non-negative float value.")
    
    lines = [
        "#************************************************************************",
        "#************** Set the start time for a motion definition **************",
        "#************************************************************************",
        "",
        f"SET_MOTION_START_TIME {motion_id} {start_time}"
    ]

    write_lines_to_file(script_filepath, lines)
    return

def set_motion_velocity(script_filepath, motion_id, vx=0.0, vy=0.0, vz=0.0):
    """
    Writes specific lines to 'script_filepath' to set the velocity vector for a motion definition.
    
    :param script_filepath: Path to the script file.
    :param motion_id: Index of the motion definition.
    :param vx, vy, vz: Velocity vector components in the motion definition coordinate system.
    
    Example usage:
    set_motion_velocity('path_to_script.txt', 1, 30.0, -10.0, 0.0)
    """
    
    # Type and value checking
    if not isinstance(motion_id, int) or motion_id <= 0:
        raise ValueError("`motion_id` should be an integer value greater than 0.")
    
    if not isinstance(vx, (int, float)) or not isinstance(vy, (int, float)) or not isinstance(vz, (int, float)):
        raise ValueError("`vx`, `vy`, and `vz` should be either integer or float values.")
    
    lines = [
        "#************************************************************************",
        "#************** Set the velocity vector for a motion definition *********",
        "#************************************************************************",
        "",
        f"SET_MOTION_VELOCITY {motion_id} {vx} {vy} {vz}"
    ]

    write_lines_to_file(script_filepath, lines)
    return 

def set_motion_acceleration(script_filepath, motion_id, ax, ay, az):
    """
    Writes specific lines to 'script_filepath' to set the acceleration vector for a motion definition.
    
    :param script_filepath: Path to the script file.
    :param motion_id: Index of the motion definition (> 0).
    :param ax: X component of the velocity vector.
    :param ay: Y component of the velocity vector.
    :param az: Z component of the velocity vector.
    
    Example usage:
    set_motion_acceleration('path_to_script.txt', 1, 0.5, -1.0, 2.5)
    """

    # Type and value checking
    if not isinstance(motion_id, int) or motion_id <= 0:
        raise ValueError("`motion_id` should be a positive integer.")
    
    if not all(isinstance(val, (int, float)) for val in [ax, ay, az]):
        raise ValueError("`ax`, `ay`, and `az` should be numeric values.")
    
    lines = [
        "#************************************************************************",
        "#*********** Set the acceleration vector for a motion definition ********",
        "#************************************************************************",
        "",
        f"SET_MOTION_ACCELERATION {motion_id} {ax} {ay} {az}"
    ]

    write_lines_to_file(script_filepath, lines)
    return


def set_motion_angular_velocity(script_filepath, motion_id, wx, wy, wz):
    """
    Writes specific lines to 'script_filepath' to set the angular velocity vector for a motion definition.
    
    :param script_filepath: Path to the script file.
    :param motion_id: Index of the motion definition (> 0).
    :param wx: X component of the angular velocity vector.
    :param wy: Y component of the angular velocity vector.
    :param wz: Z component of the angular velocity vector.
    
    Example usage:
    set_motion_angular_velocity('path_to_script.txt', 1, -450.5, 0.0, 0.0)
    """
    
    # Type and value checking
    if not isinstance(motion_id, int) or motion_id <= 0:
        raise ValueError("`motion_ID` should be a positive integer.")
    
    if not all(isinstance(val, (int, float)) for val in [wx, wy, wz]):
        raise ValueError("`wx`, `wy`, and `wz` should be numeric values.")
    
    lines = [
        "#************************************************************************",
        "#*********** Set the angular velocity vector for a motion definition ****",
        "#************************************************************************",
        "",
        f"SET_MOTION_ANGULAR_VELOCITY {motion_id} {wx} {wy} {wz}"
    ]

    write_lines_to_file(script_filepath, lines)
    return

def set_motion_angular_acceleration(script_filepath, motion_id, wax, way, waz):
    """
    Writes specific lines to 'script_filepath' to set the angular acceleration vector 
    for a motion definition.
    
    :param script_filepath: Path to the script file.
    :param motion_id: Index of the motion definition.
    :param wax: Angular acceleration in X.
    :param way: Angular acceleration in Y.
    :param waz: Angular acceleration in Z.
    
    Example usage:
        set_motion_angular_acceleration('path_to_script.txt', 1, 0.5, -1.0, 2.5)
    """
    
    # Type and value checking
    if not isinstance(motion_id, int) or motion_id <= 0:
        raise ValueError("`motion_id` should be an integer value greater than 0.")
    
    if not all(isinstance(val, (int, float)) for val in [wax, way, waz]):
        raise ValueError("Angular acceleration values should be integer or float values.")
    
    lines = [
        "#************************************************************************",
        "#*********** Set the acceleration vector for a motion definition ********",
        "#************************************************************************",
        "",
        f"SET_MOTION_ANGULAR_ACCELERATION {motion_id} {wax} {way} {waz}"
    ]
    
    write_lines_to_file(script_filepath, lines)
    return

def set_motion_is_rotor(script_filepath, motion_id, flag='ENABLE', axis='X'):
    """
    Writes specific lines to 'script_filepath' to specify if the motion definition 
    is a rotor or propeller.
    
    :param script_filepath: Path to the script file.
    :param motion_id: Index of the motion definition.
    :param flag: ENABLE or DISABLE.
    :param axis: Axis specification (X, Y or Z).
    
    Example usage:
        set_motion_is_rotor('path_to_script.txt', 1, 'ENABLE', 'X')
    """
    
    # Type and value checking
    if not isinstance(motion_id, int) or motion_id <= 0:
        raise ValueError("`motion_id` should be an integer value greater than 0.")
    
    if flag not in ['ENABLE', 'DISABLE']:
        raise ValueError("`flag` should be either 'ENABLE' or 'DISABLE'.")
    
    if axis not in ['X', 'Y', 'Z']:
        raise ValueError("`axis` should be one of 'X', 'Y', 'Z'.")
    
    lines = [
        "#************************************************************************",
        "#*********** Specify if motion definition is a rotor/propeller **********",
        "#************************************************************************",
        "",
        f"SET_MOTION_IS_ROTOR {motion_id} {flag} {axis}"
    ]
    
    write_lines_to_file(script_filepath, lines)
    return

def set_motion_custom_table(script_filepath, motion_type='VELOCITY-TIME', motion_id=1, filename=None):
    """
    Writes specific lines to 'script_filepath' to specify a custom motion definition table.
    
    :param script_filepath: Path to the script file.
    :param motion_type: Type of motion, either 'VELOCITY-TIME' or 'POSITION-TIME'.
    :param motion_id: Index of the motion definition (> 0).
    :param filename: Path to the text file containing the motion data.

    Example usage:
    set_motion_custom_table('path_to_script.txt', motion_type='VELOCITY-TIME', motion_id=1, 
                            filename='C:\\Users\\Desktop\\Models\\custom_motion.txt')
    """
    
    # Type and value checking
    valid_motion_types = ['VELOCITY-TIME', 'POSITION-TIME']
    if motion_type not in valid_motion_types:
        raise ValueError(f"`motion_type` should be one of {valid_motion_types}")

    if not isinstance(motion_id, int) or motion_id <= 0:
        raise ValueError("`motion_id` should be a positive integer value.")
    
    if filename is None or not isinstance(filename, str):
        raise ValueError("`filename` should be a valid string path to the motion data.")
    
    lines = [
        "#************************************************************************",
        "#*********** Specify custom motion definition table ********************",
        "#************************************************************************",
        "",
        f"SET_MOTION_CUSTOM_TABLE {motion_type} {motion_id}",
        filename
    ]

    write_lines_to_file(script_filepath, lines)
    return

def set_motion_mass_properties(script_filepath, motion_id, mass, ixx, iyy, izz, ixy, iyz, izx):
    """
    Writes specific lines to 'script_filepath' to specify motion mass properties.
    
    :param script_filepath: Path to the script file.
    :param motion_id: Index of the motion definition (> 0).
    :param mass: Mass (kg) of the geometry.
    :param ixx, iyy, izz: Moment of inertia components.
    :param ixy, iyz, izx: Product of inertia components.

    Example usage:
    set_motion_mass_properties('path_to_script.txt', motion_id=1, mass=1200.5, ixx=12.5, 
                               iyy=45.3, izz=0.3, ixy=0.0, iyz=12.4, izx=13.5)
    """
    
    # Type and value checking
    if not isinstance(motion_id, int) or motion_id <= 0:
        raise ValueError("`motion_id` should be a positive integer value.")
    
    if not all(isinstance(val, (int, float)) for val in [mass, ixx, iyy, izz, ixy, iyz, izx]):
        raise ValueError("Mass and inertia values should be numeric (int or float).")
    
    lines = [
        "#************************************************************************",
        "#*********** Specify motion mass properties ****************************",
        "#************************************************************************",
        "",
        f"SET_MOTION_MASS_PROPERTIES {motion_id} {mass} {ixx} {iyy} {izz} {ixy} {iyz} {izx}"
    ]

    write_lines_to_file(script_filepath, lines)
    return

def set_motion_gravity(script_filepath, motion_id, gx=0, gy=0, gz=-9.81):
    """
    Writes specific lines to 'script_filepath' to set the gravity force for a 6DOF motion definition.
    
    :param script_filepath: Path to the script file.
    :param motion_id: Index of the motion definition.
    :param gx: Gravity vector component in the reference coordinate system (X-direction).
    :param gy: Gravity vector component in the reference coordinate system (Y-direction).
    :param gz: Gravity vector component in the reference coordinate system (Z-direction).

    Example usage:
    set_motion_gravity('path_to_script.txt', 1)
    """
    
    # Type and value checking
    if not isinstance(motion_id, int) or motion_id <= 0:
        raise ValueError("`motion_id` should be an integer value greater than 0.")
    
    if not all(isinstance(val, (int, float)) for val in [gx, gy, gz]):
        raise ValueError("Gravity components `gx`, `gy`, and `gz` should be integers or float values.")
    
    lines = [
        "#************************************************************************",
        "#*********** Set the gravity force for a 6DOF motion definition *********",
        "#************************************************************************",
        "",
        f"SET_MOTION_GRAVITY {motion_id} {gx} {gy} {gz}"
    ]

    write_lines_to_file(script_filepath, lines)
    return


def set_motion_6dof_initial_velocity(script_filepath, motion_id, vx=10.0, vy=0, vz=-25.0):
    """
    Writes specific lines to 'script_filepath' to set the initial velocity conditions for a 6DOF motion.
    
    :param script_filepath: Path to the script file.
    :param motion_id: Index of the motion definition.
    :param vx: Initial velocity vector component in the body coordinate system (X-direction).
    :param vy: Initial velocity vector component in the body coordinate system (Y-direction).
    :param vz: Initial velocity vector component in the body coordinate system (Z-direction).

    Example usage:
    set_motion_6dof_initial_velocity('path_to_script.txt', 1)
    """
    
    # Type and value checking
    if not isinstance(motion_id, int) or motion_id <= 0:
        raise ValueError("`motion_id` should be an integer value greater than 0.")
    
    if not all(isinstance(val, (int, float)) for val in [vx, vy, vz]):
        raise ValueError("Velocity components `vx`, `vy`, and `vz` should be integers or float values.")
    
    lines = [
        "#************************************************************************",
        "#*********** Set the initial velocity conditions for a 6DOF motion ******",
        "#************************************************************************",
        "",
        f"SET_MOTION_6DOF_INITIAL_VELOCITY {motion_id} {vx} {vy} {vz}"
    ]

    write_lines_to_file(script_filepath, lines)
    return

def set_motion_6dof_initial_angular_velocity(script_filepath, motion_id, wx=0.0, wy=0.0, wz=0.0):
    """
    Writes specific lines to 'script_filepath' to set initial angular velocity conditions for a 6DOF motion.

    Example usage:
    set_motion_6dof_initial_angular_velocity('path_to_script.txt', 1, 0.0, 0, -0.25)
    
    :param script_filepath: Path to the script file.
    :param motion_id: Index of the motion definition.
    :param wx: X component of the initial angular velocity vector.
    :param wy: Y component of the initial angular velocity vector.
    :param wz: Z component of the initial angular velocity vector.
    """
    
    # Type and value checking
    if not isinstance(motion_id, int) or motion_id <= 0:
        raise ValueError("`motion_id` should be an integer value greater than 0.")
    
    if not all(isinstance(i, (int, float)) for i in [wx, wy, wz]):
        raise ValueError("Angular velocity components should be integer or float values.")
    
    lines = [
        "#************************************************************************",
        "#******* Set initial angular velocity conditions for a 6DOF motion ******",
        "#************************************************************************",
        "",
        f"SET_MOTION_6DOF_INITIAL_ANGULAR_VELOCITY {motion_id} {wx} {wy} {wz}"
    ]

    write_lines_to_file(script_filepath, lines)
    return


def set_motion_6dof_active_variables(script_filepath, motion_id, u='DISABLE', v='DISABLE', 
                                     w='DISABLE', p='DISABLE', q='DISABLE', r='DISABLE'):
    """
    Writes specific lines to 'script_filepath' to set the 6DOF motion active variables.

    Example usage:
    set_motion_6dof_active_variables('path_to_script.txt', 1, u='DISABLE', v='DISABLE', 
                                     w='DISABLE', p='DISABLE', q='ENABLE', r='ENABLE')
    
    :param script_filepath: Path to the script file.
    :param motion_id: Index of the motion definition.
    :param u: Enable or disable the U velocity component.
    :param v: Enable or disable the V velocity component.
    :param w: Enable or disable the W velocity component.
    :param p: Enable or disable the P angular velocity component.
    :param q: Enable or disable the Q angular velocity component.
    :param r: Enable or disable the R angular velocity component.
    """
    
    # Type and value checking
    if not isinstance(motion_id, int) or motion_id <= 0:
        raise ValueError("`motion_id` should be an integer value greater than 0.")
    
    valid_values = ['ENABLE', 'DISABLE']
    if any(i not in valid_values for i in [u, v, w, p, q, r]):
        raise ValueError(f"All parameters should be one of {valid_values}")
    
    lines = [
        "#************************************************************************",
        "#*********** Set the 6DOF motion active variables ***********************",
        "#************************************************************************",
        "",
        f"SET_MOTION_6DOF_ACTIVE_VARIABLES {motion_id}",
        f"U {u}",
        f"V {v}",
        f"W {w}",
        f"P {p}",
        f"Q {q}",
        f"R {r}"
    ]

    write_lines_to_file(script_filepath, lines)
    return

def set_6dof_motion_symmetry_loads(script_filepath, motion_id, symmetry_loads='ENABLE'):
    """
    Writes specific lines to 'script_filepath' to set 6DOF motion symmetry loads.
    
    :param script_filepath: Path to the script file.
    :param motion_id: Index of the motion definition.
    :param symmetry_loads: ENABLE or DISABLE the symmetry boundary loads option.
    
    Example usage:
    >>> set_6dof_motion_symmetry_loads('path_to_script.txt', 1)
    """
    
    # Type and value checking
    if not isinstance(motion_id, int) or motion_id <= 0:
        raise ValueError("`motion_id` should be a positive integer value.")
    
    valid_symmetry_loads = ['ENABLE', 'DISABLE']
    if symmetry_loads not in valid_symmetry_loads:
        raise ValueError(f"`symmetry_loads` should be one of {valid_symmetry_loads}")
    
    lines = [
        "#************************************************************************",
        "#*********** Convert the 6DOF motion into a longitudinal 3DOF ***********",
        "#************************************************************************",
        "",
        f"SET_3DOF_MOTION {motion_id} {symmetry_loads}"
    ]
    write_lines_to_file(script_filepath, lines)
    return

def create_new_6dof_external_force(script_filepath, motion_id, x, y, z, t_start, delta_t, fx, fy, fz):
    """
    Writes specific lines to 'script_filepath' to create a new 6DOF motion external force.
    
    :param script_filepath: Path to the script file.
    :param motion_id: Index of the motion definition.
    :param x, y, z: Coordinates of the 6DOF external force.
    :param t_start: Start time of the external force.
    :param delta_t: Operational time of the external force.
    :param fx, fy, fz: Force vector components.
    
    Example usage:
    >>> create_new_6dof_external_force('path_to_script.txt', 1, 0.0, -0.2, 1.2, 0, 0.25, -3000, 0, 0)
    """
    
    # Type and value checking
    if not isinstance(motion_id, int) or motion_id <= 0:
        raise ValueError("`motion_id` should be a positive integer value.")
    
    if not isinstance(t_start, (int, float)) or t_start < 0:
        raise ValueError("`t_start` should be a non-negative number.")
    
    if not isinstance(delta_t, (int, float)) or delta_t <= 0:
        raise ValueError("`delta_t` should be a positive number.")
    
    lines = [
        "#************************************************************************",
        "#*********** Create a new 6DOF motion external force ********************",
        "#************************************************************************",
        "",
        f"CREATE_NEW_6DOF_EXTERNAL_FORCE {motion_id} {x} {y} {z} {t_start} {delta_t} {fx} {fy} {fz}"
    ]
    write_lines_to_file(script_filepath, lines)
    return

def create_new_6dof_custom_force(script_filepath, motion_id, force_type, filename):
    """
    Writes specific lines to 'script_filepath' to create a new 6DOF motion custom external force profile.
    
    :param script_filepath: Path to the script file.
    :param motion_id: Index of the motion definition.
    :param force_type: Type of the custom motion. One of: 'FORCE_VS_TIME' or 'FORCE_VS_DISTANCE'.
    :param filename: Path to the text file containing the custom force profile.
    
    Example usage:
    create_new_6dof_custom_force('path_to_script.txt', 1, 'FORCE_VS_TIME', 'C:\\Users\\Desktop\\Models\\custom_force_profile.txt')
    """
    
    # Type and value checking
    if not isinstance(motion_id, int) or motion_id <= 0:
        raise ValueError("`motion_id` should be an integer value greater than 0.")
    
    valid_types = ['FORCE_VS_TIME', 'FORCE_VS_DISTANCE']
    if force_type not in valid_types:
        raise ValueError(f"`force_type` should be one of {valid_types}")
    
    lines = [
        "#************************************************************************",
        "#******** Create a new 6DOF motion custom external force profile ********",
        "#************************************************************************",
        "",
        f"CREATE_NEW_6DOF_CUSTOM_FORCE {motion_id} {force_type}",
        filename
    ]

    write_lines_to_file(script_filepath, lines)
    return

def create_new_6dof_spring_force(script_filepath, motion_id, x, y, z, nx, ny, nz, free_length, 
                                 solid_length, initial_length, spring_rate):
    """
    Writes specific lines to 'script_filepath' to create a new 6DOF motion external spring force.
    
    :param script_filepath: Path to the script file.
    :param motion_id: Index of the motion definition.
    :param x, y, z: Coordinates of the 6DOF external force in the body frame coordinate system.
    :param nx, ny, nz: Normal vector coordinates of the spring axis.
    :param free_length: Length of the uncompressed spring.
    :param solid_length: Fully-compressed spring length.
    :param initial_length: Initial compressed length of the spring.
    :param spring_rate: Force per unit length of the spring (in N/m).
    
    Example usage:
    create_new_6dof_spring_force('path_to_script.txt', 1, 0.0, -0.2, 1.2, 0, 0, -1, 0.1, 0.05, 0.06, 100000.0)
    """
    
    # Type and value checking
    if not isinstance(motion_id, int) or motion_id <= 0:
        raise ValueError("`motion_id` should be an integer value greater than 0.")
    
    for val in [free_length, solid_length, initial_length, spring_rate]:
        if not isinstance(val, (int, float)) or val <= 0:
            raise ValueError("All spring parameters should be positive numbers.")
    
    lines = [
        "#************************************************************************",
        "#*********** Create a new 6DOF motion external spring force *************",
        "#************************************************************************",
        "",
        f"CREATE_NEW_6DOF_SPRING_FORCE {motion_id} {x} {y} {z} {nx} {ny} {nz} {free_length} {solid_length} {initial_length} {spring_rate}"
    ]

    write_lines_to_file(script_filepath, lines)
    return

def delete_6dof_external_force(script_filepath, motion_id, force_id):
    """
    Writes specific lines to 'script_filepath' to delete an existing 6DOF Motion external force.
    
    :param script_filepath: Path to the script file.
    :param motion_id: Index of the motion definition.
    :param force_id: Index of the external force to be deleted.
    
    Example usage:
    delete_6dof_external_force('path_to_script.txt', 1, 4)
    """
    
    # Type and value checking
    if not isinstance(motion_id, int) or motion_id <= 0:
        raise ValueError("`motion_id` should be an integer value greater than 0.")
    
    if not isinstance(force_id, int) or force_id <= 0:
        raise ValueError("`force_id` should be an integer value greater than 0.")
    
    lines = [
        "#************************************************************************",
        "#*********** Delete an existing 6DOF Motion external force **************",
        "#************************************************************************",
        "",
        f"DELETE_6DOF_EXTERNAL_FORCE {motion_id} {force_id}"
    ]

    write_lines_to_file(script_filepath, lines)


def export_6dof_trajectory(script_filepath, motion_id, filename):
    """
    Writes specific lines to 'script_filepath' to export 6DOF Motion trajectory tables to external file.
    
    :param script_filepath: Path to the script file.
    :param motion_id: Index of the motion definition.
    :param filename: Path to the text file where the trajectory tables should be written.
    
    Example usage:
    export_6dof_trajectory('path_to_script.txt', 1, 'C:\\Users\\Desktop\\Models\\6DOF_Trajectory.txt')
    """
    
    # Type and value checking
    if not isinstance(motion_id, int) or motion_id <= 0:
        raise ValueError("`motion_id` should be an integer value greater than 0.")
    
    check_file_existence(filename)
    
    lines = [
        "#************************************************************************",
        "#*********** Export 6DOF Motion trajectory tables to external file ******",
        "#************************************************************************",
        "",
        f"EXPORT_6DOF_TRAJECTORY {motion_id}",
        filename
    ]

    write_lines_to_file(script_filepath, lines)
