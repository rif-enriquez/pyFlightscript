from .utils import *

def view_resize(script_filepath):
    """
    Writes specific lines to 'script_filepath' to resize the view in the scene.
    
    :param script_filepath: Path to the script file.
    
    Example usage:
    view_resize('path_to_script.txt')
    """
    
    lines = [
        "#************************************************************************",
        "#****************** Resizing the view in the scene **********************",
        "#************************************************************************",
        "",
        "VIEW_RESIZE"
    ]

    write_lines_to_file(script_filepath, lines)
    return

def change_scene_to(script_filepath, scene):
    """
    Writes specific lines to 'script_filepath' to change the scene.
    
    :param script_filepath: Path to the script file.
    :param scene: string to change the scene. Must be one of CAD, GEOMETRY, SOLVER, PLOTS
    
    Example usage:
    change_scene_to('path_to_script.txt', 'CAD')
    """

    valid_options = ["CAD", "GEOMETRY", "SOLVER", "PLOTS"]
    if scene not in valid_options:
        raise ValueError(f"Invalid scene: {scene}. Must be one of {', '.join(valid_options)}.")
    
    lines = [
        "#************************************************************************",
        "#************************ Change the Scene To ***************************",
        "#************************************************************************",
        "",
        f"CHANGE_SCENE_TO_{scene}"
    ]

    write_lines_to_file(script_filepath, lines)
    return

def set_scene_view(script_filepath, view_option='DEFAULTVIEW'):
    """
    Writes specific lines to 'script_filepath' to set the scene view.
    
    :param script_filepath: Path to the script file.
    :param view_option: Option for the view which can be one of the following:
                        'DEFAULTVIEW', 'XY_POSITIVE', 'XY_NEGATIVE', 
                        'XZ_POSITIVE', 'XZ_NEGATIVE', 'YZ_POSITIVE', 'YZ_NEGATIVE'
                        
    Example Usage:
    set_scene_view('path_to_script.txt', 'DEFAULTVIEW')
    set_scene_view('path_to_script.txt', 'XY_NEGATIVE')
    """
    
    # Define a dictionary to match the view_option to the appropriate function name
    view_commands = {
        'DEFAULTVIEW': 'SET_SCENE_DEFAULTVIEW',
        'XY_POSITIVE': 'SET_SCENE_XY_POSITIVE',
        'XY_NEGATIVE': 'SET_SCENE_XY_NEGATIVE',
        'XZ_POSITIVE': 'SET_SCENE_XZ_POSITIVE',
        'XZ_NEGATIVE': 'SET_SCENE_XZ_NEGATIVE',
        'YZ_POSITIVE': 'SET_SCENE_YZ_POSITIVE',
        'YZ_NEGATIVE': 'SET_SCENE_YZ_NEGATIVE'
    }
    
    # Check the view option validity
    if view_option not in view_commands:
        raise ValueError(f"Invalid view_option provided. Must be one of {list(view_commands.keys())}")
    
    # Write the command lines to the script
    lines = [
        "#************************************************************************",
        f"#****************** Setting Scene to {view_option} ************************",
        "#************************************************************************",
        "",
        view_commands[view_option]
    ]

    write_lines_to_file(script_filepath, lines)
    return

def set_scene_colormap_type(script_filepath, colormap='PRIMARY', 
                            type_value='BLACKBODY_STANDARD'):
    """
    Writes specific lines to 'script_filepath' to set the solver colormap type.
    
    :param script_filepath: Path to the script file.
    :param colormap: Either PRIMARY or SECONDARY.
    :param type_value: Type of colormap.
    
    Example usage:
    set_scene_colormap_type('path_to_script.txt', 'PRIMARY', 'BLACKBODY_STANDARD')
    """
    
    # Type and value checking
    valid_colormaps = ['PRIMARY', 'SECONDARY']
    if colormap not in valid_colormaps:
        raise ValueError(f"`colormap` should be one of {valid_colormaps}")
    
    valid_types = ['RAINBOW_STANDARD', 'GRAYSCALE', 'BENT_HOTCOOL', 
                   'BLACKBODY_STANDARD', 'BLACKBODY_EXTENDED', 'KINDLMANN',
                   'RAINBOW_LONG', 'BROWNBLUE', 'HOTCOOL']
    if type_value not in valid_types:
        raise ValueError(f"`type_value` should be one of {valid_types}")
    
    lines = [
        "#************************************************************************",
        "#****************** Set solver colormap type ****************************",
        "#************************************************************************",
        "",
        "SET_SCENE_COLORMAP_TYPE",
        f"COLORMAP {colormap}",
        f"TYPE {type_value}"
    ]
    
    write_lines_to_file(script_filepath, lines)
    return


def set_scene_colormap_size(script_filepath, colormap='PRIMARY', 
                            thickness=300, height=15):
    """
    Writes specific lines to 'script_filepath' to set the solver colormap size.
    
    :param script_filepath: Path to the script file.
    :param colormap: Either PRIMARY or SECONDARY.
    :param thickness: Thickness value in pixels.
    :param height: Height value in pixels.
    
    Example usage:
    set_scene_colormap_size('path_to_script.txt', 'PRIMARY', 300, 15)
    """
    
    # Type and value checking
    valid_colormaps = ['PRIMARY', 'SECONDARY']
    if colormap not in valid_colormaps:
        raise ValueError(f"`colormap` should be one of {valid_colormaps}")
    
    if not isinstance(thickness, int):
        raise ValueError("`thickness` should be an integer value.")
    
    if not isinstance(height, int):
        raise ValueError("`height` should be an integer value.")
    
    lines = [
        "#************************************************************************",
        "#****************** Set solver colormap size ****************************",
        "#************************************************************************",
        "",
        "SET_SCENE_COLORMAP_SIZE",
        f"COLORMAP {colormap}",
        f"THICKNESS {thickness}",
        f"HEIGHT {height}"
    ]
    
    write_lines_to_file(script_filepath, lines)
    return

def set_scene_colormap_position(script_filepath, colormap='PRIMARY', x=450, y=75):
    """
    Writes specific lines to 'script_filepath' to set the solver colormap position.
    
    Example usage:
        set_scene_colormap_position('path_to_script.txt', colormap='PRIMARY', x=450, y=75)
    
    :param script_filepath: Path to the script file.
    :param colormap: Either 'PRIMARY' or 'SECONDARY'.
    :param x: Value in pixels for the X-coordinate.
    :param y: Value in pixels for the Y-coordinate.
    """
    
    # Type and value checking
    valid_colormaps = ['PRIMARY', 'SECONDARY']
    if colormap not in valid_colormaps:
        raise ValueError(f"`colormap` should be one of {valid_colormaps}")

    if not isinstance(x, int):
        raise ValueError("`x` should be an integer value.")

    if not isinstance(y, int):
        raise ValueError("`y` should be an integer value.")
    
    lines = [
        "#************************************************************************",
        "#****************** Set solver colormap position ************************",
        "#************************************************************************",
        "",
        "SET_SCENE_COLORMAP_POSITION",
        f"COLORMAP {colormap}",
        f"X {x}",
        f"Y {y}"
    ]

    write_lines_to_file(script_filepath, lines)
    return

def set_scene_colormap_shading(script_filepath, colormap='PRIMARY', reverse='DISABLE', smooth='ENABLE'):
    """
    Writes specific lines to 'script_filepath' to set the solver colormap shading.
    
    Example usage:
        set_scene_colormap_shading('path_to_script.txt', colormap='PRIMARY', reverse='DISABLE', smooth='ENABLE')
    
    :param script_filepath: Path to the script file.
    :param colormap: Either 'PRIMARY' or 'SECONDARY'.
    :param reverse: Either 'ENABLE' or 'DISABLE'.
    :param smooth: Either 'ENABLE' or 'DISABLE'.
    """
    
    # Type and value checking
    valid_colormaps = ['PRIMARY', 'SECONDARY']
    if colormap not in valid_colormaps:
        raise ValueError(f"`colormap` should be one of {valid_colormaps}")

    valid_settings = ['ENABLE', 'DISABLE']
    if reverse not in valid_settings:
        raise ValueError(f"`reverse` should be one of {valid_settings}")

    if smooth not in valid_settings:
        raise ValueError(f"`smooth` should be one of {valid_settings}")
    
    lines = [
        "#************************************************************************",
        "#****************** Set solver colormap shading *************************",
        "#************************************************************************",
        "",
        "SET_SCENE_COLORMAP_SHADING",
        f"COLORMAP {colormap}",
        f"REVERSE {reverse}",
        f"SMOOTH {smooth}"
    ]

    write_lines_to_file(script_filepath, lines)
    return

def set_scene_colormap_custom_mode(script_filepath, colormap='PRIMARY', custom_range='ENABLE'):
    """
    Writes specific lines to 'script_filepath' to set the colormap custom mode.
    
    :param script_filepath: Path to the script file.
    :param colormap: Can be either 'PRIMARY' or 'SECONDARY'.
    :param custom_range: Can be either 'ENABLE' or 'DISABLE'.
    
    Example usage:
        set_scene_colormap_custom_mode('path_to_script.txt')
    """
    
    # Type and value checking
    valid_colormaps = ['PRIMARY', 'SECONDARY']
    if colormap not in valid_colormaps:
        raise ValueError(f"`colormap` should be one of {valid_colormaps}")
    
    valid_custom_ranges = ['ENABLE', 'DISABLE']
    if custom_range not in valid_custom_ranges:
        raise ValueError(f"`custom_range` should be one of {valid_custom_ranges}")
    
    lines = [
        "#************************************************************************",
        "#****************** Set solver colormap custom range mode ***************",
        "#************************************************************************",
        "",
        "SET_SCENE_COLORMAP_CUSTOM_MODE",
        f"COLORMAP {colormap}",
        f"CUSTOM_RANGE {custom_range}"
    ]

    write_lines_to_file(script_filepath, lines)
    return 

def set_scene_colormap_custom_range(script_filepath, colormap='PRIMARY', cut_off_mode='OFF', 
                                   maximum=1.0, minimum=-1.5):
    """
    Writes specific lines to 'script_filepath' to set the colormap custom range.
    
    :param script_filepath: Path to the script file.
    :param colormap: Can be either 'PRIMARY' or 'SECONDARY'.
    :param cut_off_mode: Mode for the custom range cut off.
    :param maximum: Maximum value of the custom range.
    :param minimum: Minimum value of the custom range.
    
    Example usage:
        set_scene_colormap_custom_range('path_to_script.txt')
    """
    
    # Type and value checking
    valid_colormaps = ['PRIMARY', 'SECONDARY']
    if colormap not in valid_colormaps:
        raise ValueError(f"`colormap` should be one of {valid_colormaps}")
    
    valid_cut_off_modes = ['OFF', 'ABOVE_AND_BELOW', 'ABOVE_MAX', 'BELOW_MIN']
    if cut_off_mode not in valid_cut_off_modes:
        raise ValueError(f"`cut_off_mode` should be one of {valid_cut_off_modes}")
    
    if not isinstance(maximum, (int, float)):
        raise ValueError("`maximum` should be an integer or float value.")
    
    if not isinstance(minimum, (int, float)):
        raise ValueError("`minimum` should be an integer or float value.")
    
    lines = [
        "#************************************************************************",
        "#****************** Set solver colormap custom range ********************",
        "#************************************************************************",
        "",
        "SET_SCENE_COLORMAP_CUSTOM_MODE",
        f"COLORMAP {colormap}",
        f"CUT_OFF_MODE {cut_off_mode}",
        f"MAXIMUM {maximum}",
        f"MINIMUM {minimum}"
    ]

    write_lines_to_file(script_filepath, lines)
    return

