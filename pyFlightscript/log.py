from .utils import *

def clear_log(script_filepath):
    """
    Writes specific lines to 'script_filepath' to clear the log.
    
    :param script_filepath: Path to the script file.
    
    Example usage:
    clear_log('path_to_script.txt')
    """
    
    lines = ["CLEAR_LOG"]
    write_lines_to_file(script_filepath, lines)
    return


def export_log(script_filepath, log_filepath):
    """
    Writes specific lines to 'script_filepath' to export log window messages.
    
    :param script_filepath: Path to the script file.
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
    
    write_lines_to_file(script_filepath, lines)
    return

