from .utils import *

def new_probe_point(script_filepath, type_value='VOLUME', x1=1.3, y1=3.3, z1=-0.5):
    """
    Writes specific lines to 'script_filepath' to create a new probe point.
    
    Example usage:
    new_probe_point('path_to_script.txt', type_value='VOLUME', x1=1.3, y1=3.3, z1=-0.5)
    
    :param script_filepath: Path to the script file.
    :param type_value: Type of the probe point. Either 'VOLUME' or 'SURFACE'.
    :param x1, y1, z1: Coordinates of the probe point.
    """
    
    # Type and value checking
    valid_types = ['VOLUME', 'SURFACE']
    if type_value not in valid_types:
        raise ValueError(f"`type_value` should be one of {valid_types}")
    
    lines = [
        "#************************************************************************",
        "#****************** Create a new probe point ****************************",
        "#************************************************************************",
        "",
        f"NEW_PROBE_POINT {type_value} {x1} {y1} {z1}"
    ]

    write_lines_to_file(script_filepath, lines)
    return

def new_probe_line(script_filepath, numpts=15, x1=0, y1=0, z1=0, x2=1.5, y2=-1.0, z2=0):
    """
    Writes specific lines to 'script_filepath' to create a new probe survey line.
    
    Example usage:
    new_probe_line('path_to_script.txt', numpts=15, x1=0, y1=0, z1=0, x2=1.5, y2=-1.0, z2=0)
    
    :param script_filepath: Path to the script file.
    :param numpts: Number of probe vertices along survey line.
    :param x1, y1, z1: Coordinates of the starting point of survey line.
    :param x2, y2, z2: Coordinates of the ending point of survey line.
    """
    
    # Type and value checking
    if not isinstance(numpts, int):
        raise ValueError("`numpts` should be an integer value.")
    
    lines = [
        "#************************************************************************",
        "#****************** Create a new probe survey line **********************",
        "#************************************************************************",
        "",
        f"NEW_PROBE_LINE {numpts} {x1} {y1} {z1} {x2} {y2} {z2}"
    ]

    write_lines_to_file(script_filepath, lines)
    return

def update_probe_points(script_filepath):
    """
    Writes specific lines to 'script_filepath' to update probe point flow properties.
    
    Example usage:
        update_probe_points('path_to_script.txt')
    """
    
    lines = [
        "#************************************************************************",
        "#****************** Update probe point flow properties *****************",
        "#************************************************************************",
        "",
        "UPDATE_PROBE_POINTS"
    ]
    
    write_lines_to_file(script_filepath, lines)
    return


def probe_points_import(script_filepath, filepath, units='INCH', frame=1):
    """
    Writes specific lines to 'script_filepath' to import probe points from a file.
    
    :param script_filepath: Path to the script file.
    :param units: Units for the probe points.
    :param frame: Index of the coordinate system.
    :param filepath: Path to the probes file.
    
    Example usage:
        probe_points_import('path_to_script.txt', units='METER', frame=2, filepath="C:/.../My_Probes.txt")
    """
    
    check_valid_length_units(units)
    
    if not isinstance(frame, int):
        raise ValueError("`frame` should be an integer value.")
    
    lines = [
        "#************************************************************************",
        "#****************** Import probe points from file ***********************",
        "#************************************************************************",
        "",
        "PROBE_POINTS_IMPORT",
        f"UNITS {units}",
        f"FRAME {frame}",
        filepath
    ]
    
    write_lines_to_file(script_filepath, lines)
    return


def export_probe_points(script_filepath, filepath):
    """
    Writes specific lines to 'script_filepath' to export probe points to a file.
    
    :param script_filepath: Path to the script file.
    :param filepath: Path to the file where probe points will be exported.
    
    Example usage:
        export_probe_points('path_to_script.txt', filepath="C:/.../My_Probes_Export.txt")
    """
    
    lines = [
        "#************************************************************************",
        "#****************** Export probe points to file *************************",
        "#************************************************************************",
        "",
        "EXPORT_PROBE_POINTS",
        filepath
    ]
    
    write_lines_to_file(script_filepath, lines)
    return

def delete_probe_points(script_filepath):
    """
    Writes specific lines to 'script_filepath' to delete all existing probe points.
    
    :param script_filepath: Path to the script file.
    
    Example usage:
        delete_probe_points('path_to_script.txt')
    """
    
    lines = [
        "#************************************************************************",
        "#****************** Delete all existing probe points ********************",
        "#************************************************************************",
        "",
        "DELETE_PROBE_POINTS"
    ]

    write_lines_to_file(script_filepath, lines)
    return


