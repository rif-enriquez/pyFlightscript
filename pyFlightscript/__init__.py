from . import actuators
from . import analysis
from . import base
from . import boundary_layer
from . import cad
from . import csys
from . import exec_solver
from . import export_data
from . import freestream
from . import geometry
from . import fsinit
from . import inlets
from . import motion
from . import post_points
from . import post_surf
from . import post_volume
from . import post_streamlines
from . import scene
from . import set_solver
from . import solver
from . import tools
from . import unite
from . import wake
from . import wrapper
from . import script

import os
import subprocess

def execute_fsm_script(script_path=".\script_out.txt", fsexe_path=None):
    """
    Execute a Finite State Machine (FSM) script using the specified script path and FSM executable path.
    
    
    :param script_path (str): The path to the FSM script file.
    :param fsexe_path (str, optional): The path to the FSM executable. If not provided, the function will
            attempt to retrieve the path from the FS_EXE environment variable. Defaults to None.
    
    Returns:
        subprocess.CompletedProcess: The result of running the FSM script.
    
    Raises:
        ValueError: If neither fsexe_path argument nor FS_EXE environment variable is set.
        FileNotFoundError: If the specified FSM executable file is not found.
    """
    if fsexe_path is None:
        fsexe_path = os.environ.get('FS_EXE')
        if fsexe_path is None:
            raise ValueError("Neither fsexe_path argument nor FS_EXE environment variable is set.")
    
    if not os.path.exists(script_path):
        raise FileNotFoundError(f"The specified file '{script_path}' does not exist on path.")
    
    try:
        result = subprocess.run(f"{fsexe_path} -script {script_path}", capture_output=True)
        return result
    except FileNotFoundError:
        raise FileNotFoundError(f"The file {fsexe_path} was not found.")

