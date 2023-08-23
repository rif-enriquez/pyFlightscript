def write_lines_to_file(script_filepath, lines):
    """
    Writes a list of lines to the specified file.
    
    :param script_filepath: Path to the script file.
    :param lines: List of lines to write.
    """
    with open(script_filepath, 'a') as outfile:
        outfile.write('\n'.join(lines))
        outfile.write('\n')
        outfile.write('\n')
    return