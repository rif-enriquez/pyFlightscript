import os
from .utils import *

def cad_create_new_model(script_filepath, model_name):
    """
    Writes specific lines to 'script_filepath' to create a new CAD-->Model.
    
    :param script_filepath: Path to the script file.
    :param model_name: Name of the new CAD model.
    """
    lines = [
        "#************************************************************************",
        "#****************** Create a new CAD-->Model ****************************",
        "#************************************************************************",
        "#",
        f"CAD_CREATE_NEW_MODEL {model_name}"
    ]

    write_lines_to_file(script_filepath, lines)
    return

def cad_create_initialize(script_filepath, model_index=1):
    """
    Writes specific lines to 'script_filepath' to initialize the CAD-->Create pane window.
    
    :param script_filepath: Path to the script file.
    :param model_index: Input model_index for CAD_CREATE_INITIALIZE to which the CAD-->Create pane is linked.
    """
    lines = [
        "#************************************************************************",
        "#****************** Initialize the CAD-->Create pane window *************",
        "#************************************************************************",
        "#",
        f"CAD_CREATE_INITIALIZE {model_index}"
    ]

    write_lines_to_file(script_filepath, lines)
    return

def cad_create_import_curve_txt(script_filepath, txt_filepath, units='METER', dimension='2D', frame=1, plane='YZ'):
    """
    Writes specific lines to 'script_filepath' to import a CAD-->Create drawing curve from a txt file.
    
    :param script_filepath: Path to the script file.
    :param units: Units for CAD_CREATE_IMPORT_CURVE_TXT (must be one of the specified units).
    :param dimension: Dimension (either "2D" or "3D").
    :param frame: Frame as an integer.
    :param plane: Plane orientation (one of "YZ", "XZ", "XY").
    :param filepath: Path to the txt file to import.
    """
    if not os.path.exists(txt_filepath):
        raise FileNotFoundError(f"The specified file '{txt_filepath}' does not exist.")

    
    valid_dimensions = ["2D", "3D"]
    valid_planes = ["YZ", "XZ", "XY"]
    
    check_valid_units(units)
    
    if dimension not in valid_dimensions:
        raise ValueError(f"Invalid dimension: {dimension}. Must be one of {', '.join(valid_dimensions)}.")
    
    if plane not in valid_planes:
        raise ValueError(f"Invalid plane: {plane}. Must be one of {', '.join(valid_planes)}.")

    lines = [
        "#************************************************************************",
        "#*************** Import a CAD-->Create drawing curve from txt file ******",
        "#************************************************************************",
        "#",
        f"CAD_CREATE_IMPORT_CURVE_TXT {units} {dimension} {frame} {plane}",
        txt_filepath
    ]

    write_lines_to_file(script_filepath, lines)
    return

def cad_create_import_ccs(script_filepath, ccs_filepath):
    """
    Writes specific lines to 'script_filepath' to import a CAD-->Create drawing curve from a csv file.
    
    :param script_filepath: Path to the script file.
    :param ccs_filepath: Path to the csv file to import.
    """
    if not os.path.exists(ccs_filepath):
        raise FileNotFoundError(f"The specified file '{ccs_filepath}' does not exist.")
    
    lines = [
        "#************************************************************************",
        "#*************** Import a CAD-->Create drawing curve from CSV file ******",
        "#************************************************************************",
        "#",
        "CAD_CREATE_IMPORT_CURVE_CCS",
        ccs_filepath
    ]

    write_lines_to_file(script_filepath, lines)
    return

def cad_create_auto_cross_sections(script_filepath, frame=1, axis='Y', sections=20, body_index=1, 
                               growth_scheme=3, growth_rate=1.2, symmetry='NONE'):
    """
    Writes specific lines to 'script_filepath' to create a series of automatic cross-sections from mesh body.
    
    :param script_filepath: Path to the script file.
    :param frame: Index of coordinate system to be used.
    :param axis: Sweep direction for creating cross-section curves (X, Y, Z).
    :param sections: Number of cross-sections requested.
    :param body_index: Index of the mesh body to be used for creating cross-sections.
    :param growth_scheme: Clustering scheme to be used when positioning cross-sections along the sweep axis.
    :param growth_rate: Growth rate to be used with the selected growth_scheme.
    :param symmetry: Symmetry plane to be used for creating half-section curves (YZ, XZ, XY) or NONE for full section.
    """
    
    lines = [
        "#************************************************************************",
        "#****** Create a series of automatic cross-sections from mesh body ******",
        "#************************************************************************",
        "#",
        f"CAD_CREATE_AUTO_CROSS_SECTIONS {frame} {axis} {sections} {body_index} {growth_scheme} {growth_rate} {symmetry}"
    ]

    write_lines_to_file(script_filepath, lines)
    return

def cad_create_cross_section(script_filepath, frame=1, plane='XZ', offset=0.0, body_index=1, quadrant=3):
    """
    Writes specific lines to 'script_filepath' to create a cross-section from an existing mesh body.
    
    :param script_filepath: Path to the script file.
    :param frame: Index of coordinate system to be used.
    :param plane: Plane of the selected coordinate system to use for slicing the mesh faces (YZ, XZ, XY).
    :param offset: Offset distance of the selected plane along the normal axis of the plane.
    :param body_index: Index of the mesh body to be used for creating cross-section.
    :param quadrant: Quadrant information for creating cross-section.

    Value YZ  XZ  XY 
        1 +Y +X +X
        2 -Y -X -X
        3 +Z +Z +Y
        4 -Z -Z -Y   
    """
    
    # Type checks and validations
    if not isinstance(frame, int) or frame <= 0:
        raise ValueError("Frame should be an integer greater than 0.")
    
    if plane not in ['YZ', 'XZ', 'XY']:
        raise ValueError("Invalid plane value. Allowed values: YZ, XZ, XY.")
    
    if not isinstance(offset, (int, float)):
        raise ValueError("Offset should be a numeric value.")
    
    if not isinstance(body_index, int) or body_index <= 0:
        raise ValueError("Body index should be an integer greater than 0.")
    
    if not isinstance(quadrant, int) or quadrant not in [1, 2, 3, 4]:
        raise ValueError("Quadrant should be one of the following integer values: 1, 2, 3, 4.")
    
    lines = [
        "#************************************************************************",
        "#********** Create a cross-sections from an existing mesh body **********",
        "#************************************************************************",
        "#",
        f"CAD_CREATE_CROSS_SECTION {frame} {plane} {offset} {body_index} {quadrant}"
    ]

    write_lines_to_file(script_filepath, lines)
    return

def cad_create_point_curve(script_filepath, x=0.0, y=1.0, z=0.0):
    """
    Writes specific lines to 'script_filepath' to create a singular point curve in 3D.
    
    :param script_filepath: Path to the script file.
    :param x: X coordinate of the point curve.
    :param y: Y coordinate of the point curve.
    :param z: Z coordinate of the point curve.
    """
    
    # Type checks and validations
    if not isinstance(x, (int, float)):
        raise ValueError("X should be a numeric value.")
    
    if not isinstance(y, (int, float)):
        raise ValueError("Y should be a numeric value.")
    
    if not isinstance(z, (int, float)):
        raise ValueError("Z should be a numeric value.")
    
    lines = [
        "#************************************************************************",
        "#********** Create a singular point curve (3D) **************************",
        "#************************************************************************",
        "#",
        f"CAD_CREATE_CURVE_POINT {x} {y} {z}"
    ]

    write_lines_to_file(script_filepath, lines)
    return

def cad_create_curve_arc(script_filepath, x0=0.0, y0=0.0, z0=0.0, x1=-1.0, y1=0.0, z1=0.0, x2=0.0, y2=1.0, z2=0.0):
    """
    Writes specific lines to 'script_filepath' to create a circular arc curve in 3D.
    
    :param script_filepath: Path to the script file.
    :param x0, y0, z0: Vertex coordinates of the origin of the circular arc.
    :param x1, y1, z1: Vertex coordinates of the first vertex of the circular arc curve.
    :param x2, y2, z2: Vertex coordinates of the second vertex of the circular arc curve.
    """
    
    # Type checks and validations
    coords = [x0, y0, z0, x1, y1, z1, x2, y2, z2]
    if not all(isinstance(coord, (int, float)) for coord in coords):
        raise ValueError("All provided coordinates should be numeric values.")
    
    lines = [
        "#************************************************************************",
        "#********** Create a circular arc curve (3D) ****************************",
        "#************************************************************************",
        "#",
        f"CAD_CREATE_CURVE_ARC {x0} {y0} {z0} {x1} {y1} {z1} {x2} {y2} {z2}"
    ]

    write_lines_to_file(script_filepath, lines)
    return

# CAD_CREATE_CURVE_SELECT