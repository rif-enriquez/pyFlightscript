import os
from .utils import *

def create_new_inlet(script_filepath, surface_id, type_value, vx_or_velocity, vy=0.0, vz=0.0):
    """
    Writes specific lines to 'script_filepath' to create a new inlet boundary.
    
    :param script_filepath: Path to the script file.
    :param surface_id: Index of the boundary surface to be marked as inlet.
    :param type_value: Type of inlet specification.
    :param vx_or_velocity: If TYPE=1, then VX. If TYPE=2, then VELOCITY.
    :param vy: VY value (only used if TYPE=1).
    :param vz: VZ value (only used if TYPE=1).
    
    Example usage:
    create_new_inlet('path_to_script.txt', 3, 1, 100.0, 0.0, -10.0)
    create_new_inlet('path_to_script.txt', 3, 2, 100.498)
    """
    
    # Type and value checking
    if not isinstance(surface_id, int) or surface_id <= 0:
        raise ValueError("`surface_id` should be an integer value greater than 0.")
    
    if type_value not in [1, 2]:
        raise ValueError("`type_value` should be either 1 or 2.")
    
    if not isinstance(vx_or_velocity, (int, float)):
        raise ValueError("`vx_or_velocity` should be an integer or float value.")
    
    if type_value == 1:
        if not isinstance(vy, (int, float)):
            raise ValueError("`vy` should be an integer or float value.")
        
        if not isinstance(vz, (int, float)):
            raise ValueError("`vz` should be an integer or float value.")
    
    if type_value == 1:
        lines = [
            "#************************************************************************",
            "#****************** Create a new inlet boundary (TYPE=1) ****************",
            "#************************************************************************",
            "",
            f"CREATE_NEW_INLET {surface_id} {type_value} {vx_or_velocity} {vy} {vz}"
        ]
    else:  # type_value == 2
        lines = [
            "#************************************************************************",
            "#****************** Create a new inlet boundary (TYPE=2) ****************",
            "#************************************************************************",
            "",
            f"CREATE_NEW_INLET {surface_id} {type_value} {vx_or_velocity}"
        ]
    
    write_lines_to_file(script_filepath, lines)
    return

def set_inlet_custom_profile(script_filepath, inlet_id, filename):
    """
    Writes specific lines to 'script_filepath' to set a custom inlet profile 
    using an external file.
    
    Example usage:
    set_inlet_custom_profile('path_to_script.txt', 1, 'C:\\Users\\Desktop\\Models\\custom_inlet_profile.txt')
    
    :param inlet_id: Index of the inlet boundary.
    :param filename: Path to the file containing the motion data.
    """
    
    # Type and value checking
    if not isinstance(inlet_id, int) or inlet_id <= 0:
        raise ValueError("`inlet_id` should be an integer value greater than 0.")
    
    if not isinstance(filename, str):
        raise ValueError("`filename` should be a string.")
    
    # It's recommended to add a check for file existence here
    if not os.path.exists(filename):
        raise ValueError(f"File '{filename}' not found.")
    
    lines = [
        "#************************************************************************",
        "#******* Upload custom velocity inlet profile from external file ********",
        "#************************************************************************",
        "",
        "SET_INLET_CUSTOM_PROFILE",
        f"{inlet_id}",
        f"{filename}"
    ]

    write_lines_to_file(script_filepath, lines)
    return

def remesh_inlet(script_filepath, inlet, inner_radius=0.0, elements=10, 
                 growth_scheme=2, growth_rate=1.2):
    """
    Writes specific lines to 'script_filepath' to radial mesh an existing inlet boundary.
    
    Example usage:
    remesh_inlet('path_to_script.txt', 1)
    
    :param script_filepath: Path to the script file.
    :param inlet: Index of inlet boundary to be meshed.
    :param inner_radius: Inner radius of the inlet boundary.
    :param elements: Number of mesh faces in the radial direction.
    :param growth_scheme: Growth scheme type (1 or 2).
    :param growth_rate: Growth rate for radial distribution of mesh faces.
    """
    
    # Type and value checking
    if not isinstance(inlet, int) or inlet < 1:
        raise ValueError("`inlet` should be an integer value greater than or equal to 1.")
    
    if not isinstance(inner_radius, (int, float)) or inner_radius < 0.0:
        raise ValueError("`inner_radius` should be a non-negative integer or float value.")
    
    if not isinstance(elements, int) or elements < 1:
        raise ValueError("`elements` should be a positive integer value.")
    
    if growth_scheme not in [1, 2]:
        raise ValueError("`growth_scheme` should be either 1 (Successive) or 2 (Dual-side).")
    
    if not isinstance(growth_rate, (int, float)) or growth_rate <= 0:
        raise ValueError("`growth_rate` should be a positive integer or float value.")
    
    lines = [
        "#************************************************************************",
        "#****************** Radial mesh an existing inlet boundary **************",
        "#************************************************************************",
        "",
        "REMESH_INLET",
        f"INLET {inlet}",
        f"INNER_RADIUS {inner_radius}",
        f"ELEMENTS {elements}",
        f"GROWTH_SCHEME {growth_scheme}",
        f"GROWTH_RATE {growth_rate}"
    ]

    write_lines_to_file(script_filepath, lines)
    return

def delete_inlet(script_filepath, inlet):
    """
    Writes specific lines to 'script_filepath' to delete an existing inlet boundary.
    
    Example usage:
    delete_inlet('path_to_script.txt', 1)
    
    :param script_filepath: Path to the script file.
    :param inlet: Index of the inlet boundary to be deleted.
    """
    
    # Type and value checking
    if not isinstance(inlet, int) or inlet <= 0:
        raise ValueError("`inlet` should be an integer value greater than 0.")
    
    lines = [
        "#************************************************************************",
        "#****************** Delete an existing inlet boundary *******************",
        "#************************************************************************",
        "",
        "DELETE_INLET",
        f"INLET {inlet}"
    ]

    write_lines_to_file(script_filepath, lines)
    return


