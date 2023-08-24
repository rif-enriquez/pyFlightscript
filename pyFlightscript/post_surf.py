from .utils import *

def create_new_surface_section(script_filepath, frame=1, plane='XZ', offset=1.0, 
                               plot_direction=1, surfaces=[]):
    """
    Writes specific lines to 'script_filepath' to create a new surface section.
    
    :param script_filepath: Path to the script file.
    :param frame: Index of the coordinate system used for this surface section.
    :param plane: Section plane. One of the following: XY, XZ or YZ.
    :param offset: Offset distance of the plane in the coordinate system.
    :param plot_direction: Value to describe the plotting direction of the surface section.
    :param surfaces: List of geometry surfaces assigned to the surface section.
    
    Example usage:
        create_new_surface_section('path_to_script.txt', frame=1, plane='XZ', offset=1.0, 
                                   plot_direction=1, surfaces=[1,4,5])
    """
    
    # Type and value checking
    if not isinstance(frame, int):
        raise ValueError("`frame` should be an integer value.")
    
    valid_planes = ['XY', 'XZ', 'YZ']
    if plane not in valid_planes:
        raise ValueError(f"`plane` should be one of {valid_planes}")
    
    if not isinstance(offset, (int, float)):
        raise ValueError("`offset` should be an integer or float value.")
    
    if plot_direction not in [1, 2]:
        raise ValueError("`plot_direction` should be 1 or 2.")
    
    if not all(isinstance(surface, int) for surface in surfaces):
        raise ValueError("`surfaces` should be a list of integer values.")
    
    lines = [
        "#************************************************************************",
        "#****************** Create new surface section **************************",
        "#************************************************************************",
        "",
        "CREATE_NEW_SURFACE_SECTION",
        f"FRAME {frame}",
        f"PLANE {plane}",
        f"OFFSET {offset}",
        f"PLOT_DIRECTION {plot_direction}",
        f"SURFACES {len(surfaces)}",
        " ".join(map(str, surfaces))
    ]

    write_lines_to_file(script_filepath, lines)
    return

def new_surface_section_distribution(script_filepath, frame=1, plane='XZ', 
                                     num_sections=20, plot_direction=1, surfaces=[1, 4, 5]):
    """
    Writes specific lines to 'script_filepath' to create new surface section distribution.
    
    Example usage:
    >>> new_surface_section_distribution('path_to_script.txt')
    
    :param script_filepath: Path to the script file.
    :param frame: Index of the coordinate system to be used for this surface section.
    :param plane: Section plane.
    :param num_sections: Number of sections to be created.
    :param plot_direction: Plotting direction of the surface section.
    :param surfaces: List of geometry surfaces assigned to the surface section.
    """
    
    # Type and value checking
    if not isinstance(frame, int):
        raise ValueError("`frame` should be an integer value.")
    
    valid_planes = ['XY', 'XZ', 'YZ']
    if plane not in valid_planes:
        raise ValueError(f"`plane` should be one of {valid_planes}")

    if not isinstance(num_sections, int) or num_sections <= 0:
        raise ValueError("`num_sections` should be a positive integer value.")
    
    if plot_direction not in [1, 2]:
        raise ValueError("`plot_direction` should be 1 or 2.")
    
    if not isinstance(surfaces, list) or not all(isinstance(s, int) for s in surfaces):
        raise ValueError("`surfaces` should be a list of integer values.")
    
    lines = [
        "#************************************************************************",
        "#****************** Create new surface section distribution *************",
        "#************************************************************************",
        "",
        "NEW_SURFACE_SECTION_DISTRIBUTION",
        f"FRAME {frame}",
        f"PLANE {plane}",
        f"NUM_SECTIONS {num_sections}",
        f"PLOT_DIRECTION {plot_direction}",
        f"SURFACES {len(surfaces)}",
        " ".join(map(str, surfaces))
    ]

    write_lines_to_file(script_filepath, lines)
    return

def compute_surface_sectional_loads(script_filepath, units='NEWTONS'):
    """
    Writes specific lines to 'script_filepath' to compute sectional loads on existing surface sections.
    
    Example usage:
    >>> compute_surface_sectional_loads('path_to_script.txt')
    
    :param script_filepath: Path to the script file.
    :param units: Unit type.
    """
    
    check_valid_force_units(units)
    
    lines = [
        "#************************************************************************",
        "#********** Compute sectional loads on existing surface sections ********",
        "#************************************************************************",
        "",
        f"COMPUTE_SURFACE_SECTIONAL_LOADS {units}"
    ]

    write_lines_to_file(script_filepath, lines)
    return

def export_surface_sectional_loads(script_filepath, filename):
    """
    Writes specific lines to 'script_filepath' to export sectional loads on existing surface sections.
    
    :param script_filepath: Path to the script file.
    :param filename: Filename with path.
    
    Example usage:
    export_surface_sectional_loads('path_to_script_1.txt')
    """
    
    lines = [
        "#************************************************************************",
        "#********** Export sectional loads on existing surface sections *********",
        "#************************************************************************",
        "",
        "EXPORT_SURFACE_SECTIONAL_LOADS",
        f"{filename}"
    ]

    write_lines_to_file(script_filepath, lines)
    return


def update_all_surface_sections(script_filepath):
    """
    Writes specific lines to 'script_filepath' to update the surface sections.
    
    :param script_filepath: Path to the script file.
    
    Example usage:
    update_all_surface_sections('path_to_script_2.txt')
    """
    
    lines = [
        "#************************************************************************",
        "#****************** Update the surface sections *************************",
        "#************************************************************************",
        "",
        "UPDATE_ALL_SURFACE_SECTIONS"
    ]

    write_lines_to_file(script_filepath, lines)
    return

def export_all_surface_sections(script_filepath, filename):
    """
    Writes specific lines to 'script_filepath' to export all surface sections to a file.
    
    :param script_filepath: Path to the script file.
    :param filename: Filename with path for the surface sections.
    
    Example usage:
    export_all_surface_sections('path_to_script.txt', 'C:/.../Test_surface_sections.txt')
    """
    
    # Type and value checking
    if not isinstance(filename, str):
        raise ValueError("`filename` should be a string value.")
    
    lines = [
        "#************************************************************************",
        "#****************** Export all surface sections to file *****************",
        "#************************************************************************",
        "",
        "EXPORT_ALL_SURFACE_SECTIONS",
        f"{filename}"
    ]
    
    write_lines_to_file(script_filepath, lines)
    return

def delete_surface_section(script_filepath, index):
    """
    Writes specific lines to 'script_filepath' to delete a surface section.
    
    :param script_filepath: Path to the script file.
    :param index: Index of the surface section to be deleted.
    
    Example usage:
    delete_surface_section('path_to_script.txt', 2)
    """
    
    # Type and value checking
    if not isinstance(index, int) or index <= 0:
        raise ValueError("`index` should be an integer greater than 0.")
    
    lines = [
        "#************************************************************************",
        "#****************** Delete a surface section ****************************",
        "#************************************************************************",
        "",
        f"DELETE_SURFACE_SECTION {index}"
    ]
    
    write_lines_to_file(script_filepath, lines)
    return

def delete_all_surface_sections(script_filepath):
    """
    Writes specific lines to 'script_filepath' to delete all existing probe points.
    
    :param script_filepath: Path to the script file.
    
    Example usage:
        delete_probe_points('path_to_script.txt')
    """
    
    lines = [
        "#************************************************************************",
        "#******************** Delete all surface sections ***********************",
        "#************************************************************************",
        "",
        "DELETE_ALL_SURFACE_SECTIONS"
    ]

    write_lines_to_file(script_filepath, lines)
    return
