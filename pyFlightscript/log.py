from .utils import *    
from .script import script

def clear_log():
    """
    Appends lines to script state to clear the log.
    

    
    Example usage:
    clear_log('path_to_script.txt')
    """
    
    lines = ["CLEAR_LOG"]
    script.append_lines(lines)
    return


def export_log(log_filepath):
    """
    Appends lines to script state to export log window messages.
    

    :param log_filepath: Path to the output log file.
    
    Example usage:
    export_log('path_to_script.txt', 'C:/.../Output_log.txt')
    """

    lines = [
        "#************************************************************************",
        "#****************** Export log window messages to file ******************",
        "#************************************************************************",
        "",
        "EXPORT_LOG",
        log_filepath
    ]
    
    script.append_lines(lines)
    return

