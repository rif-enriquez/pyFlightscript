import os
from .utils import *    
from .script import script

def boolean_unite_geometry(bodies, openvsp_path, bodies_values=None):
    """
    Appends lines to script state to boolean unite a selection of geometry bodies.
    

    :param bodies: Number of geometry bodies being Boolean-united. Can be -1 to specifiy all.
    :param openvsp_path: Path to OpenVSP executable used for the CompGeom unite function call.
    :param bodies_values: List of tuples containing index values of the geometry surfaces 
                          and their volume types.

    Example usage:
    boolean_unite_geometry('path_to_script.txt', 5, r"\C\Test_folder\...\VSP\", 
                          bodies_values=[(1, 'POSITIVE'), (2, 'POSITIVE'), 
                                         (3, 'NEGATIVE'), (4, 'NEGATIVE'), (5, 'POSITIVE')])
                          
    """
    
    # Type and value checking
    if not isinstance(bodies, int):
        raise ValueError("`bodies` should be a positive integer value.")
    
    check_file_existence(openvsp_path)
    
    if bodies_values:
        if len(bodies_values) != bodies:
            raise ValueError("`bodies_values` list should match the number specified in `bodies`.")
        
        for item in bodies_values:
            if not isinstance(item, tuple) or len(item) != 2:
                raise ValueError("Each item in `bodies_values` should be a tuple of size 2.")
            
            index, volume_type = item
            if not isinstance(index, int) or index <= 0:
                raise ValueError("Index value in each tuple of `bodies_values` should be a positive integer.")
            
            valid_volume_types = ['POSITIVE', 'NEGATIVE']
            if volume_type not in valid_volume_types:
                raise ValueError(f"Volume type in each tuple of `bodies_values` should be one of {valid_volume_types}")
    
    lines = [
        "#************************************************************************",
        "#************* Boolean unite a selection of geometry bodies *************",
        "#************************************************************************",
        "#",
        "BOOLEAN_UNITE_GEOMETRY",
        f"BODIES {bodies}"
    ]

    # Add bodies values if provided
    if bodies_values:
        for index, volume_type in bodies_values:
            lines.append(f"{index} {volume_type}")

    lines.append(f"OPENVSP_PATH {openvsp_path}")

    script.append_lines(lines)
    return


