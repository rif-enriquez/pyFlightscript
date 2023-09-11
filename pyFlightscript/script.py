class State:
    def __init__(self):
        self.lines = []

    def append_lines(self, lines):
        """
        Append lines to the existing lines array in the object.

        Parameters:
            lines (str or list): The lines to be appended. It can be either a string or a list of strings.

        Returns:
            None
        """
        if isinstance(lines, str):
            self.lines.append(lines)
        elif isinstance(lines, list):
            self.lines.extend(lines)

    def display_lines(self):
        """
        Print each line stored in lines array.
        """
        for line in self.lines:
            print(line)

    def write_to_file(self, filename="script_out.txt"):
        """
        Writes the contents of the 'lines' attribute to a script file for use in FlightStream.

        Args:
            filename (str, optional): The name of the file to write to. Defaults to "script_out.txt".

        Returns:
            None
        """
        with open(filename, 'w') as file:
            for line in self.lines:
                file.write(line + '\n')
            file.write('\n')

    def clear_lines(self):
        """
        Clear the lines arrray of the object.

        Parameters:
            None

        Returns:
            None
        """
        self.lines = []

# create an instance of State to hold lines
script = State()

def display_lines():
    """
        Print each line stored in lines array.
    """
    script.display_lines()
    return

def write_to_file(filename="script_out.txt"):
    script.write_to_file(filename)
    print("pyscript lines written to: "+ filename)
    return

def clear_lines():
    script.clear_lines()
    print("pyscript lines cleared")
    return

def hard_reset(filename="script_out.txt"):
    """
    Resets the script lines and deletes the specified output file.

    Parameters:
        filename (str): The name of the output file. Defaults to "script_out.txt".

    Returns:
        None
    """
    import os
    script.clear_lines()
    # Check if file exists and then delete
    if os.path.exists(filename):
        try:
            os.remove(filename)
        except OSError as e:
            print(f"Error: {e.filename} - {e.strerror}")
    return

def run_script(fsexe_path, script_path=r'.\script_out.txt'):
    """
    Runs a script using FlightStream executable path and runs script path.

    Args:
        fsexe_path (str): The path to the external executable.
        script_path (str, optional): The path to the script file. Defaults to '.\script_out.txt'.

    Returns:
        None
    """
    import subprocess
    subprocess.run(fsexe_path+' -script ' + script_path, capture_output=True)
    return