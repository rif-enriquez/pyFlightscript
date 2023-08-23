import os
from .utils import *

def create_new_base_region(script_filepath, surface, base_pressure_coefficient):
    """
    Writes specific lines to 'script_filepath' to create a new base region.

    :param script_filepath: Path to the script file.
    :param surface: Index of the boundary surface to be marked as base region boundary.
    :param base_pressure_coefficient: Pressure coefficient to be applied in base regions.

    Example usage:
    create_new_base_region('path_to_script.txt', 3, -0.2)
    """
    
    # Type and value checking
    if not isinstance(surface, int) or surface <= 0:
        raise ValueError("`surface` should be an integer value greater than 0.")
    
    if not isinstance(base_pressure_coefficient, (int, float)):
        raise ValueError("`base_pressure_coefficient` should be an integer or float value.")
    
    lines = [
        "#************************************************************************",
        "#****************** Create a new base region ****************************",
        "#************************************************************************",
        "",
        "CREATE_NEW_BASE_REGION",
        f"SURFACE {surface}",
        f"BASE_PRESSURE_COEFFICIENT {base_pressure_coefficient}"
    ]

    write_lines_to_file(script_filepath, lines)
    return

def auto_detect_base_regions(script_filepath):
    """
    Writes specific lines to 'script_filepath' to auto-detect base regions on the geometry.

    Example usage:
    auto_detect_base_regions('path_to_script.txt')

    :param script_filepath: Path to the script file.
    """
    
    lines = [
        "#************************************************************************",
        "#****************** Auto-detect base regions on the geometry ************",
        "#************************************************************************",
        "",
        "AUTO_DETECT_BASE_REGIONS"
    ]

    write_lines_to_file(script_filepath, lines)
    return

def detect_base_regions_by_surface(script_filepath, boundary_index=1):
    """
    Example usage:
    detect_base_regions_by_surface('path_to_script.txt')
    
    Writes specific lines to 'script_filepath' to detect base regions by surface index.
    
    :param script_filepath: Path to the script file.
    :param boundary_index: Index of the mesh boundary to use for marking base regions.
    """
    
    # Type and value checking
    if not isinstance(boundary_index, int) or boundary_index <= 0:
        raise ValueError("`boundary_index` should be an integer value greater than 0.")
    
    lines = [
        "#************************************************************************",
        "#****************** Detect base regions by surface index ****************",
        "#************************************************************************",
        "",
        f"DETECT_BASE_REGIONS_BY_SURFACE {boundary_index}"
    ]

    write_lines_to_file(script_filepath, lines)
    return

def set_base_region_trailing_edges(script_filepath, base_region_boundary=-1):
    """
    Example usage:
    set_base_region_trailing_edges('path_to_script.txt')

    Writes specific lines to 'script_filepath' to set base region trailing edges.

    :param script_filepath: Path to the script file.
    :param base_region_boundary: Index of the base region boundary to use for marking trailing edges.
    """
    
    # Type and value checking
    if not isinstance(base_region_boundary, int):
        raise ValueError("`base_region_boundary` should be an integer value.")
    if base_region_boundary == 0:
        raise ValueError("`base_region_boundary` should be greater than 0 or -1.")
    
    lines = [
        "#************************************************************************",
        "#****************** Set base region trailing edges **********************",
        "#************************************************************************",
        "",
        f"SET_BASE_REGION_TRAILING_EDGES {base_region_boundary}"
    ]

    write_lines_to_file(script_filepath, lines)
    return

def delete_base_region(script_filepath, base_region_boundary):
    """
    Example usage:
    delete_base_region('path_to_script.txt', 2)
    
    Writes specific lines to 'script_filepath' to delete an existing base region.
    
    :param script_filepath: Path to the script file.
    :param base_region_boundary: Index of the base region boundary to be deleted.
    """
    
    # Type and value checking
    if not isinstance(base_region_boundary, int) or base_region_boundary <= 0:
        raise ValueError("`base_region_boundary` should be an integer value greater than 0.")
    
    lines = [
        "#************************************************************************",
        "#****************** Delete an existing base region **********************",
        "#************************************************************************",
        "",
        f"DELETE_BASE_REGION {base_region_boundary}"
    ]

    write_lines_to_file(script_filepath, lines)
    return
