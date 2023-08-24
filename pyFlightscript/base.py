import os
from .utils import *    
from .script_state import script

def create_new_base_region(surface, base_pressure_coefficient):
    """
    Appends lines to script state to create a new base region.


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

    script.append_lines(lines)
    return

def auto_detect_base_regions():
    """
    Appends lines to script state to auto-detect base regions on the geometry.

    Example usage:
    auto_detect_base_regions('path_to_script.txt')


    """
    
    lines = [
        "#************************************************************************",
        "#****************** Auto-detect base regions on the geometry ************",
        "#************************************************************************",
        "",
        "AUTO_DETECT_BASE_REGIONS"
    ]

    script.append_lines(lines)
    return

def detect_base_regions_by_surface(boundary_index=1):
    """
    Example usage:
    detect_base_regions_by_surface('path_to_script.txt')
    
    Appends lines to script state to detect base regions by surface index.
    

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

    script.append_lines(lines)
    return

def set_base_region_trailing_edges(base_region_boundary=-1):
    """
    Example usage:
    set_base_region_trailing_edges('path_to_script.txt')

    Appends lines to script state to set base region trailing edges.


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

    script.append_lines(lines)
    return

def delete_base_region(base_region_boundary):
    """
    Example usage:
    delete_base_region('path_to_script.txt', 2)
    
    Appends lines to script state to delete an existing base region.
    

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

    script.append_lines(lines)
    return
