import os
from .utils import *

def delete_transition_trip(script_filepath, transition_trip_index):
    """
    Writes specific lines to 'script_filepath' to delete an existing transition trip edge set.
    
    :param script_filepath: Path to the script file.
    :param transition_trip_index: Index of the BL transition trip edges to be deleted.
    
    Example usage:
    delete_transition_trip('path_to_script.txt', 2)
    """

    # Type and value checking
    if not isinstance(transition_trip_index, int) or transition_trip_index <= 0:
        raise ValueError("`transition_trip_index` should be an integer greater than 0.")
    
    lines = [
        "#************************************************************************",
        "#************ Delete an existing transition trip edge set ***************",
        "#************************************************************************",
        "",
        f"DELETE_TRANSITION_TRIP {transition_trip_index}"
    ]

    write_lines_to_file(script_filepath, lines)
    return
