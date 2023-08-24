from .utils import *

def create_new_rectangle_volume_section(script_filepath, frame=1, plane='XZ', offset=0., size=-0.5, 
                                        x1=-2.5, y1=-1.0, x2=2.5, y2=1.0, prisms_type='PRISMS', 
                                        thickness=0.3, layers=20, growth_rate=1.2):
    """
    Writes specific lines to 'script_filepath' to create a new rectangle volume section.
    
    :param script_filepath: Path to the script file.
    :param frame: Index of the coordinate system used for this volume section.
    :param plane: Section plane.
    :param offset: Offset distance of the plane in the coordinate system.
    :param size: Refinement size.
    :param x1, y1: Diagonal corner 1 of the rectangle section.
    :param x2, y2: Diagonal corner 2 of the rectangle section.
    :param prisms_type: Option to select near-wall prismatic cells.
    :param thickness: Thickness of the near-wall prism cells layer.
    :param layers: Number of layers in the near-wall prism cells layer.
    :param growth_rate: Growth rate of prism cells.
    
    Example usage:
    create_new_rectangle_volume_section('path_to_script1.txt')
    """
    
    lines = [
        "#************************************************************************",
        "#****************** Create new volume section (rectangle) ***************",
        "#************************************************************************",
        "",
        f"CREATE_NEW_RECTANGLE_VOLUME_SECTION {frame} {plane} {offset} {size} {x1} {y1} {x2} {y2} {prisms_type} {thickness} {layers} {growth_rate}"
    ]

    write_lines_to_file(script_filepath, lines)
    return


def create_new_circle_volume_section(script_filepath, frame=1, plane='XZ', offset=0.1, ipts=20, 
                                     jpts=40, r1=0.0, r2=2.5, prisms_type='PRISMS', thickness=0.3, 
                                     layers=20, growth_rate=1.2):
    """
    Writes specific lines to 'script_filepath' to create a new circle volume section.
    
    :param script_filepath: Path to the script file.
    :param frame: Index of the coordinate system used for this volume section.
    :param plane: Section plane.
    :param offset: Offset distance of the plane in the coordinate system.
    :param ipts: Number of radial segments in the circular grid.
    :param jpts: Number of azimuth segments in the circular grid.
    :param r1, r2: Inner and outer radius of the circular section.
    :param prisms_type: Option to select near-wall prismatic cells.
    :param thickness: Thickness of the near-wall prism cells layer.
    :param layers: Number of layers in the near-wall prism cells layer.
    :param growth_rate: Growth rate of prism cells.
    
    Example usage:
    create_new_circle_volume_section('path_to_script2.txt')
    """

    lines = [
        "#************************************************************************",
        "#****************** Create new volume section (circle) ******************",
        "#************************************************************************",
        "",
        f"CREATE_NEW_CIRCLE_VOLUME_SECTION {frame} {plane} {offset} {ipts} {jpts} {r1} {r2} {prisms_type} {thickness} {layers} {growth_rate}"
    ]

    write_lines_to_file(script_filepath, lines)
    return

def volume_section_boundary_layer(script_filepath, index, setting='DISABLE'):
    """
    Writes specific lines to 'script_filepath' to toggle volume section boundary layer induction.
    
    :param script_filepath: Path to the script file.
    :param index: Index of the volume section for which the boundary-layer setting is being changed.
    :param setting: Setting value (ENABLE/DISABLE).
    
    Example usage:
        volume_section_boundary_layer('path_to_script.txt', 2)
    """
    
    # Type and value checking
    if not isinstance(index, int) or index <= 0:
        raise ValueError("`index` should be an integer value greater than 0.")
    
    valid_settings = ['ENABLE', 'DISABLE']
    if setting not in valid_settings:
        raise ValueError(f"`setting` should be one of {valid_settings}")
    
    lines = [
        "#************************************************************************",
        "#*************** Toggle volume section boundary layer induction *********",
        "#************************************************************************",
        "",
        f"VOLUME_SECTION_BOUNDARY_LAYER {index} {setting}"
    ]

    write_lines_to_file(script_filepath, lines)
    return

def volume_section_wireframe(script_filepath, index, setting='ENABLE'):
    """
    Writes specific lines to 'script_filepath' to toggle volume section wire-frame setting.
    
    :param script_filepath: Path to the script file.
    :param index: Index of the volume section for which the wire-frame setting is being changed.
    :param setting: Setting value (ENABLE/DISABLE).
    
    Example usage:
        volume_section_wireframe('path_to_script.txt', 2, 'DISABLE')
    """
    
    # Type and value checking
    if not isinstance(index, int) or index <= 0:
        raise ValueError("`index` should be an integer value greater than 0.")
    
    valid_settings = ['ENABLE', 'DISABLE']
    if setting not in valid_settings:
        raise ValueError(f"`setting` should be one of {valid_settings}")
    
    lines = [
        "#************************************************************************",
        "#****************** Toggle volume section wire-frame setting ************",
        "#************************************************************************",
        "",
        f"VOLUME_SECTION_WIREFRAME {index} {setting}"
    ]

    write_lines_to_file(script_filepath, lines)
    return

def update_all_volume_sections(script_filepath):
    """
    Writes specific lines to 'script_filepath' to update all volume sections.
    
    :param script_filepath: Path to the script file.
    
    Example usage:
    update_all_volume_sections('path_to_script.txt')
    """
    
    lines = [
        "#************************************************************************",
        "#****************** Update the volume sections **************************",
        "#************************************************************************",
        "",
        "UPDATE_ALL_VOLUME_SECTIONS"
    ]

    write_lines_to_file(script_filepath, lines)
    return

def export_volume_section_vtk(script_filepath, index, filename):
    """
    Writes specific lines to 'script_filepath' to export a volume section as a ParaView (VTK) file.
    
    :param script_filepath: Path to the script file.
    :param index: Index of the volume section to be exported.
    :param filename: Full path to the desired output VTK file.
    
    Example usage:
    export_volume_section_vtk('path_to_script.txt', 2, 'C:/.../Test_volume_sections.vtk')
    """
    
    # Type and value checking
    if not isinstance(index, int) or index <= 0:
        raise ValueError("`index` should be an integer value greater than 0.")
    
    lines = [
        "#************************************************************************",
        "#****************** Export volume section as ParaView (VTK) file ********",
        "#************************************************************************",
        "",
        f"EXPORT_VOLUME_SECTION_VTK {index}",
        filename
    ]

    write_lines_to_file(script_filepath, lines)
    return

def export_volume_section_2d_vtk(script_filepath, index, filename):
    """
    Writes specific lines to 'script_filepath' to export volume section as 2D ParaView (VTK) file.
    
    :param script_filepath: Path to the script file.
    :param index: Index of the volume section to be exported.
    :param filename: Filename with path for export.
    
    Example usage:
    export_volume_section_2d_vtk('path_to_script.txt', 2, 'C:/.../Test_volume_sections_2D.vtk')
    """

    # Type and value checking
    if not isinstance(index, int) or index <= 0:
        raise ValueError("`index` should be an integer value greater than 0.")

    lines = [
        "#************************************************************************",
        "#************* Export volume section as 2D ParaView (VTK) file **********",
        "#************************************************************************",
        "",
        f"EXPORT_VOLUME_SECTION_2D_VTK {index}",
        filename
    ]
    
    write_lines_to_file(script_filepath, lines)
    return


def export_volume_section_tecplot(script_filepath, index, filename):
    """
    Writes specific lines to 'script_filepath' to export volume section as Tecplot (DAT) file.
    
    :param script_filepath: Path to the script file.
    :param index: Index of the volume section to be exported.
    :param filename: Filename with path for export.
    
    Example usage:
    export_volume_section_tecplot('path_to_script.txt', 2, 'C:/.../Test_volume_sections.dat')
    """

    # Type and value checking
    if not isinstance(index, int) or index <= 0:
        raise ValueError("`index` should be an integer value greater than 0.")

    lines = [
        "#************************************************************************",
        "#****************** Export volume section as Tecplot (DAT) file *********",
        "#************************************************************************",
        "",
        f"EXPORT_VOLUME_SECTION_TECPLOT {index}",
        filename
    ]
    
    write_lines_to_file(script_filepath, lines)
    return

def delete_volume_section(script_filepath, index):
    """
    Writes specific lines to 'script_filepath' to delete a particular volume section.
    
    :param script_filepath: Path to the script file.
    :param index: Index of the volume section to be deleted (> 0).
    
    Example usage:
        delete_volume_section('path_to_script.txt', 2)
    """
    
    # Type and value checking
    if not isinstance(index, int) or index <= 0:
        raise ValueError("`index` should be an integer value greater than 0.")
    
    lines = [
        "#************************************************************************",
        "#****************** Delete a volume section *****************************",
        "#************************************************************************",
        "",
        f"DELETE_VOLUME_SECTION {index}"
    ]

    write_lines_to_file(script_filepath, lines)
    return

def delete_all_volume_sections(script_filepath):
    """
    Writes specific lines to 'script_filepath' to delete all volume sections.
    
    :param script_filepath: Path to the script file.
    
    Example usage:
        delete_all_volume_sections('path_to_script.txt')
    """
    
    lines = [
        "#************************************************************************",
        "#****************** Delete all volume sections **************************",
        "#************************************************************************",
        "",
        "DELETE_ALL_VOLUME_SECTIONS"
    ]

    write_lines_to_file(script_filepath, lines)
    return


