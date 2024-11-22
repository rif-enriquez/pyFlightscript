# This is a real world script used. Shown here for illustration purposes. 
# DOES NOT WORK AS IS!!!!!
import os, pdb
import pyFlightscript as pyfs
import pandas as pd

def find_fsm_files(root_dir):
    """Find all files with '.fsm' in their name under root_dir."""
    fsm_files = []

    for dirpath, dirnames, filenames in os.walk(root_dir):
        for filename in filenames:
            if '.fsm' in filename and '_wing_' in filename:
                fsm_files.append(os.path.join(dirpath, filename))

    return fsm_files

if __name__ == '__main__':
    fsexe_path = r'C:\Users\username\AppData\Roaming\Research in Flight\FlightStream\FlightStream.exe' #I9
    
    f = "" # fsm filename

    sref = 3.6
    cref = 0.
    
    pyfs.hard_reset() # clear lines from local memory, delete existing script.txt
    V0 = 10 #m/sec
    alt = 10000
    cid = "001" # string id

    pyfs.open_fsm(fsm_filepath=f) # solver is setup already
    pyfs.air_altitude(altitude=alt)
    pyfs.initialize_solver(surfaces=-1, load_frame=2, symmetry_type='PLANE',
                      proximity_avoidance='DISABLE', stabilization='ENABLE', stabilization_strength=1.0,
                      fast_multipole='ENABLE', wake_termination_x=7)
    pyfs.boundary_layer_type(type_value='TRANSITIONAL')
    pyfs.viscous_coupling(mode='ENABLE') 
    pyfs.set_axial_separation_boundaries(3, boundaries=[5,6,7])
    pyfs.solver_settings(angle_of_attack=0.0, sideslip_angle=0.0, 
                        freestream_velocity=V0, iterations=450, 
                        convergence_limit=4e-05, forced_run='DISABLE', 
                        reference_velocity=V0, 
                        reference_area=sref, reference_length=cref, 
                        processors=12, wake_size=1000)
    
    outfile = f.replace('.fsm', "_cid_" + str(cid) + '.txt')
    pyfs.execute_solver_sweeper(results_filename=outfile, 
                              angle_of_attack='ENABLE', 
                              side_slip_angle='DISABLE', velocity='DISABLE', 
                              angle_of_attack_start=-10, angle_of_attack_stop=15, angle_of_attack_delta=2.5, 
                              angle_of_attack_start=2.5, angle_of_attack_stop=2.5, angle_of_attack_delta=2.5, 
                              side_slip_angle_start=0.0, side_slip_angle_stop=0.0, side_slip_angle_delta=1.0, 
                              velocity_start=0.0, velocity_stop=0.0, velocity_delta=1.0, 
                              export_surface_data_per_step='DISABLE', 
                              clear_solution_after_each_run='DISABLE', 
                              reference_velocity_equals_freestream='ENABLE', 
                              append_to_existing_sweep='DISABLE')
    pyfs.save_as_fsm(f)
    pyfs.close_flightstream
    # all macro commands done
    pyfs.write_to_file() # now write and run the script to script.txt
    pyfs.execute_fsm_script(fsexe_path=fsexe_path) # execute the script in FS
    pyfs.hard_reset()  # clear the lines from local memory and delete the script.txt file
        
