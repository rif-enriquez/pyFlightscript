import os
from .utils import *

def physics(script_filepath, auto_trail_edges=False, auto_wake_nodes=False, end=True):
    """
    Writes specific lines to 'script_filepath' to set the physics conditions.

    :param script_filepath: Path to the script file.
    :param auto_trail_edges: If True, launches trailing-edge auto-detection tool.
    :param auto_wake_nodes: If True, launches wake termination node auto-detection tool.
    :param end: If True, adds an "END" line.

    Example usage:
    physics('path_to_script.txt', auto_trail_edges=True, auto_wake_nodes=True)
    """
    
    # List to store the lines
    lines = [
        "#************************************************************************",
        "#****************** Set the physics conditions if needed ****************",
        "#************************************************************************",
        "#",
        "PHYSICS"
    ]

    if auto_trail_edges:
        lines.append("AUTO_TRAIL_EDGES")

    if auto_wake_nodes:
        lines.append("AUTO_WAKE_NODES")

    if end:
        lines.append("END")

    write_lines_to_file(script_filepath, lines)
    return

def detect_trailing_edges_by_surface(script_filepath, surfaces=[1]):
    """
    Example usage:
    detect_trailing_edges_by_surface('path_to_script.txt', [2, 4])

    Writes specific lines to 'script_filepath' to detect trailing edges by surface.

    :param script_filepath: Path to the script file.
    :param surfaces: List of surface indices to be checked for trailing edge detection.
    """

    # Type and value checking
    if not isinstance(surfaces, list) or not all(isinstance(s, int) for s in surfaces):
        raise ValueError("`surfaces` should be a list of integer values.")

    lines = [
        "#************************************************************************",
        "#****************** Detect Trailing Edges by Surface ********************",
        "#************************************************************************",
        "#",
        "DETECT_TRAILING_EDGES_BY_SURFACE",
        f"SURFACES {len(surfaces)}",
        ",".join(map(str, surfaces))
    ]

    write_lines_to_file(script_filepath, lines)
    return

def trailing_edges_import(script_filepath, file_path):
    """
    Writes specific lines to 'script_filepath' to import trailing edges from a given file.
    
    :Example usage:
        trailing_edges_import('path_to_script.txt', 'C:/.../Custom_TE.txt')
        
    :param script_filepath: Path to the script file.
    :param file_path: Path to the CSV text file containing the vertices on which the trailing edges are to be marked.


    ----------------------------
    Sample File Format: 
    10
    MILLIMETER
    1,X1,Y1,Z1
    2,X2,Y2,Z2
    3,X3,Y3,Z3
    ...
    10,X10,Y10,Z10
    
    UNIT_TYPE is one of the following:
    INCH, MILLIMETER, FEET, MILE, METER, KILOMETER, MILS, MICRON, CENTIMETER, MICROINCH
    """
    
    # Type and value checking
    if not isinstance(file_path, str):
        raise ValueError("`file_path` should be a string value.")
    
    # Check if the file path has the correct extension
    if not file_path.lower().endswith('.txt'):
        raise ValueError("`file_path` should end with '.txt'")
    
    lines = [
        "#************************************************************************",
        "#************** Import custom trailing edge marking from file ***********",
        "#************************************************************************",
        "#",
        "TRAILING_EDGES_IMPORT",
        file_path
    ]

    write_lines_to_file(script_filepath, lines)
    return

def detect_wake_termination_nodes_by_surface(script_filepath, surface_id=1):
    """
    Writes specific lines to 'script_filepath' to detect wake termination nodes by surface.

    Example usage:
    detect_wake_termination_nodes_by_surface('path_to_script.txt')
    
    :param script_filepath: Path to the script file.
    :param surface_id: Index of the surface on which the wake termination nodes should be detected.
    """
    
    # Type and value checking
    if not isinstance(surface_id, int):
        raise ValueError("`surface_id` should be an integer value.")
    
    lines = [
        "#************************************************************************",
        "#****************** Detect wake termination nodes by surface ************",
        "#************************************************************************",
        "#",
        f"DETECT_WAKE_TERMINATION_NODES_BY_SURFACE {surface_id}"
    ]

    write_lines_to_file(script_filepath, lines)
    return
