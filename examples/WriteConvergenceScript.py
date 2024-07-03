# example script of how to run a CCS based mesh convergence study
import pathlib, os
import shutil, pdb
import pyFlightscript as pyfs

#######USER VARS
refFrame = '2'
runU = False
uStart = 80
uInterval = 10 # delta step
uInts = 20 # total intervals

runV = True
vStart = 15
vInterval = 5 # delta step
vInts = 17 # total intervals

aoaVal = 15 # stop angle

######### 
cwd = str(pathlib.Path(__file__).parent.resolve()) + '\\'
uTable = []
vTable = []

#Write CCS files for the script
def write_ccs_files(uVal, input, UV="U"):
    #read input file, write corrected output
    name = "Analysis" + UV + str(uVal) + ".csv"
    path = cwd + name
    with open(path, "w") as output:
        input.seek(0)
        text = input.readlines()
        for line in text:
            #iterate through each line
             index = line.find("Mesh_" + UV)
             if index>=0:
                 writeline = "Mesh_"  + UV + ";" + str(uVal) + ";1;1;1\n"
                 output.write(writeline)
             else:
                output.write(line)
        output.close()                 

def import_run_export(path, xval, UV):
    ccsPath = path + "Analysis" + UV + str(xval) + ".csv"
    pyfs.mesh.ccs_import(ccsPath)
    pyfs.solver.solver_uninitialize()
    pyfs.analysis.set_vorticity_drag_boundaries(-1)
    pyfs.solver.initialize_solver(-1, 1, symmetry_periodicity=1,
              proximity_avoidance='DISABLE', stabilization='DISABLE', stabilization_strength=1.0,
              fast_multipole='ENABLE', wake_termination_x='DEFAULT', symmetry_type='PLANE')
    pyfs.scene.change_scene_to("PLOTS")
    pyfs.tools.execute_solver_sweeper(path + "results\\"+ "Analysis" + UV + str(xval) + ".txt", 
                   angle_of_attack='ENABLE',  angle_of_attack_start=0.0, 
                   angle_of_attack_stop=aoaVal, angle_of_attack_delta=aoaVal,
                   export_surface_data_per_step='DISABLE', 
                   clear_solution_after_each_run='DISABLE',
                   reference_velocity_equals_freestream='ENABLE',
                   append_to_existing_sweep='DISABLE')
    return

#Write & Run the FS script
def writerun_fs_script(path):
    fsexe_path = r'C:\Users\Danie\AppData\Roaming\Research in Flight\FlightStream\FlightStream.exe' #specify file path to FS exe
    pyfs.script.hard_reset() # (optional) clear lines from local memory, delete existing script.txt
    pyfs.fsinit.open_fsm(fsm_filepath=os.path.join(path, "base.fsm"))
    pyfs.mesh.surface_clearall()

    # import, run, and export each ccs file
    for x in uTable:
        import_run_export(path, x, UV="U")
            
    for x in vTable:
        import_run_export(path, x, UV="V")
            
    pyfs.exec_solver.close_flightstream()
    pyfs.script.write_to_file() # now write script_out.txt
    pyfs.execute_fsm_script(fsexe_path=fsexe_path) # execute the script in headless FS
    
#main function  
if __name__ == '__main__':
    # delete the folder results and all files within
    if False:
        shutil.rmtree(cwd + "results")
        pathlib.Path(cwd + "results").mkdir(parents=True, exist_ok=True)

    # Analysis.csv is the input CCS file
    # the file must contatin the parameters Mesh_U and Mesh_V
    with open(cwd + "Analysis.csv", "r") as read:
        uVal = uStart
        vVal = vStart
        uStop = uStart + (uInterval * uInts)
        vStop = vStart + (vInterval * vInts)

        if runU:
            while uVal <= uStop:
                uTable.append(uVal)
                write_ccs_files(uVal, read, UV="U")
                uVal += uInterval

        if runV:
            while vVal <= vStop:
                vTable.append(vVal)
                write_ccs_files(vVal,read, UV="V")
                vVal += vInterval

        #Write FS script
        writerun_fs_script(cwd)
        read.close()

