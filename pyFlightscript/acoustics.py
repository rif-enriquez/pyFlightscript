from .utils import *    
from .script import script    

def acoustic_sources(status='ENABLE'):
    """
    Appends lines to script state to enable or disable acoustic sources during solver initialization.

    :param status: Either 'ENABLE' or 'DISABLE'.
    
    Example usage:
    acoustic_sources(, status='ENABLE')
    """
    
    # Type and value checking
    if status not in ['ENABLE', 'DISABLE']:
        raise ValueError("`status` should be either 'ENABLE' or 'DISABLE'")
    
    lines = [
        "#************************************************************************",
        "#******** Enable acoustic sources during solver initialization **********",
        "#************************************************************************",
        "#",
        f"ACOUSTIC_SOURCES {status}"
    ]

    script.append_lines(lines)
    return

def create_new_acoustic_observer(name, x=0.0, y=0.0, z=0.0):
    """
    Appends lines to script state to create a new acoustic observer.

    :param name: Name of the observer.
    :param x: X-coordinate of the observer.
    :param y: Y-coordinate of the observer.
    :param z: Z-coordinate of the observer.
    
    Example usage:
    create_new_acoustic_observer(, 'Observer-1', 0.0, -0.5, 2.0)
    """
    
    # Type and value checking
    if not isinstance(name, str):
        raise ValueError("`name` should be a string.")
    
    if not all(isinstance(val, (int, float)) for val in [x, y, z]):
        raise ValueError("Coordinates `x`, `y`, and `z` should be numeric values (int or float).")
    
    lines = [
        "#************************************************************************",
        "#******************* Create new acoustic observer ***********************",
        "#************************************************************************",
        "#",
        f"CREATE_NEW_ACOUSTIC_OBSERVER {name} {x} {y} {z}"
    ]

    script.append_lines(lines)
    return

def acoustic_observers_import(file_path):
    """
    Appends lines to script state to import acoustic observers from a file.
    

    :param file_path: Path to the observer file.
    
    Example usage:
        acoustic_observers_import(, 'C:/.../Observers.txt')
    """
    
    # Type and value checking
    if not isinstance(file_path, str):
        raise ValueError("`file_path` should be a string.")
    
    lines = [
        "#************************************************************************",
        "#****************** Import acoustic observers from file *****************",
        "#************************************************************************",
        "#",
        "ACOUSTIC_OBSERVERS_IMPORT",
        file_path
    ]
    
    script.append_lines(lines)
    return


def delete_acoustic_observer(observer_index):
    """
    Appends lines to script state to delete an acoustic observer by index.
    

    :param observer_index: Index of the observer in the acoustic toolbox UI tree.
    
    Example usage:
        delete_acoustic_observer(, 2)
    """
    
    # Type and value checking
    if not isinstance(observer_index, int):
        raise ValueError("`observer_index` should be an integer value.")
    
    lines = [
        "#************************************************************************",
        "#******************* Delete acoustic observer ***************************",
        "#************************************************************************",
        "#",
        "DELETE_ACOUSTIC_OBSERVER",
        str(observer_index)
    ]
    
    script.append_lines(lines)
    return

def delete_all_acoustic_observers():
    """
    Appends lines to script state to delete all acoustic observers.
    


    Example usage:
    >>> delete_all_acoustic_observers()
    """
    
    lines = [
        "#************************************************************************",
        "#******************* Delete all acoustic observers **********************",
        "#************************************************************************",
        "#",
        "DELETE_ALL_ACOUSTIC_OBSERVERS"
    ]

    script.append_lines(lines)
    return

def set_acoustic_observer_time(initial_time=0.0, final_time=0.2, time_steps=300):
    """
    Appends lines to script state to set acoustic observer time parameters.
    

    :param initial_time: Initial observer signal time (seconds).
    :param final_time: Final observer signal time (seconds).
    :param time_steps: Total number of time steps between initial and final times.

    Example usage:
    >>> set_acoustic_observer_time()
    """
    
    # Type and value checking
    if not isinstance(initial_time, (int, float)):
        raise ValueError("`initial_time` should be an integer or float value.")
    
    if not isinstance(final_time, (int, float)):
        raise ValueError("`final_time` should be an integer or float value.")
    
    if not isinstance(time_steps, int):
        raise ValueError("`time_steps` should be an integer value.")
    
    lines = [
        "#************************************************************************",
        "#******************* Set acoustic observer time parameters **************",
        "#************************************************************************",
        "#",
        f"SET_ACOUSTIC_OBSERVER_TIME {initial_time} {final_time} {time_steps}"
    ]

    script.append_lines(lines)
    return

def compute_acoustic_signals():
    """
    Appends lines to script state to compute acoustic signals at all observers.



    Example usage:
    compute_acoustic_signals()
    """
    
    lines = [
        "#************************************************************************",
        "#******************* Compute acoustic signals at all observers **********",
        "#************************************************************************",
        "#",
        "COMPUTE_ACOUSTIC_SIGNALS"
    ]
    
    script.append_lines(lines)
    return

def export_acoustic_signals(filename):
    """
    Appends lines to script state to export acoustic signals at all observers.


    :param filename: Path to the output file.

    Example usage:
    export_acoustic_signals(, 'C:\\path\\to\\output.txt')
    """
    
    # Type checking
    if not isinstance(filename, str):
        raise ValueError("`filename` should be a string.")
    
    lines = [
        "#************************************************************************",
        "#******* Export acoustic signals at all observers to external file ******",
        "#************************************************************************",
        "#",
        "EXPORT_ACOUSTIC_SIGNALS",
        f"{filename}"
    ]
    
    script.append_lines(lines)
    return

def create_acoustic_section(frame=1, plane='XZ', offset=-2.0,
                            radial_observers=20, azimuth_observers=40, inner_radius=0.0,
                            outer_radius=3.0, storage_path="C:\\...\\Acoustic_Output\\"):
    """
    Appends lines to script state to create and export acoustic section signals.
    

    :param frame: Index of the coordinate system to be used.
    :param plane: Section plane.
    :param offset: Offset distance of the plane.
    :param radial_observers: Number of observers in the radial direction.
    :param azimuth_observers: Number of observers in the azimuth direction.
    :param inner_radius: Inner radius of the acoustic section.
    :param outer_radius: Outer radius of the acoustic section.
    :param storage_path: Path to folder for exporting the individual files.
    
    Example usage:
    create_acoustic_section()
    """

    # Type and value checking
    if not isinstance(frame, int):
        raise ValueError("`frame` should be an integer value.")
    
    valid_planes = ['XY', 'XZ', 'YZ']
    if plane not in valid_planes:
        raise ValueError(f"`plane` should be one of {valid_planes}")
    
    if not all(isinstance(x, (int, float)) for x in [offset, inner_radius, outer_radius]):
        raise ValueError("`offset`, `inner_radius` and `outer_radius` should be numeric values.")
    
    if not all(isinstance(x, int) for x in [radial_observers, azimuth_observers]):
        raise ValueError("`radial_observers` and `azimuth_observers` should be integer values.")
    
    lines = [
        "#************************************************************************",
        "#******************* Create & export acoustic section signals ***********",
        "#************************************************************************",
        "#",
        "CREATE_ACOUSTIC_SECTION",
        f"FRAME {frame}",
        f"PLANE {plane}",
        f"OFFSET {offset}",
        f"RADIAL_OBSERVERS {radial_observers}",
        f"AZIMUTH_OBSERVERS {azimuth_observers}",
        f"INNER_RADIUS {inner_radius}",
        f"OUTER_RADIUS {outer_radius}",
        f"STORAGE_PATH {storage_path}"
    ]

    script.append_lines(lines)
    return
