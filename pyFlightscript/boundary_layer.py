import os
from .utils import *    
from .script_state import script

def delete_transition_trip(transition_trip_index):
    """
    Appends lines to script state to delete an existing transition trip edge set.
    

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

    script.append_lines(lines)
    return
