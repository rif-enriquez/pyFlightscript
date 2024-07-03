# this script is an example of setting stability coefficients and then
# running an AOA sweep. Update the file paths accordingly.
import pyFlightscript as pyfs
import numpy as np


### SET CASE CONDITIONS
fsexe_path = 'path/to/FlightStream.exe'
V0 = 10.0 # m/s
sref = 1.0 # ref area, m^2
cref = 1.0 # ref length (chord), m
bref = 10.0 # span, m

### ANGLE OF ATTACK SWEEP
angle_array = np.linspace(0,16,5)
pyfs.script.hard_reset()

# Start script commands
### OPEN FSM WITH MESH READY TO GO
fsm_filepath = '/example/file.fsm'
pyfs.fsinit.open_fsm(fsm_filepath)

### CREATE A NEW CSYS AT THE CG (X-forward, Y-right, Z-down)
xcg = 1
ycg = 0
zcg = 1
pyfs.csys.create_new_coordinate_system()
pyfs.csys.edit_coordinate_system(2, "CG", xcg, ycg, zcg,
                                 -1, 0, 0, 
                                 0, 1, 0, 
                                 0, 0, -1)

### SET UP STABILITY COEFFICIENTS
pyfs.tools.stability_toolbox_settings(ROTATION_FRAME=2, UNITS='PER_RADIAN', CLEAR_SOLVER_PER_RUN='ENABLE', ANGULAR_RATE_INCREMENT=0.2)
pyfs.tools.stability_toolbox_new_coefficient(FRAME=2, UNITS='COEFFICIENTS', NUMERATOR='CL', DENOMINATOR='AOA', CONSTANT=1, NAME='CLA', BOUNDARIES=-1)
pyfs.tools.stability_toolbox_new_coefficient(FRAME=2, UNITS='COEFFICIENTS', NUMERATOR='CD', DENOMINATOR='AOA', CONSTANT=1, NAME='CDA', BOUNDARIES=-1)
pyfs.tools.stability_toolbox_new_coefficient(FRAME=2, UNITS='COEFFICIENTS', NUMERATOR='MOMENT_Y', DENOMINATOR='AOA', CONSTANT=1, NAME='CmA', BOUNDARIES=-1)

pyfs.tools.stability_toolbox_new_coefficient(FRAME=2, UNITS='COEFFICIENTS', NUMERATOR='FORCE_Y', DENOMINATOR='BETA', CONSTANT=1, NAME='CYB', BOUNDARIES=-1)
pyfs.tools.stability_toolbox_new_coefficient(FRAME=2, UNITS='COEFFICIENTS', NUMERATOR='MOMENT_X', DENOMINATOR='BETA', CONSTANT=1, NAME='ClB', BOUNDARIES=-1)
pyfs.tools.stability_toolbox_new_coefficient(FRAME=2, UNITS='COEFFICIENTS', NUMERATOR='MOMENT_Z', DENOMINATOR='BETA', CONSTANT=1, NAME='CnB', BOUNDARIES=-1)

pyfs.tools.stability_toolbox_new_coefficient(FRAME=2, UNITS='COEFFICIENTS', NUMERATOR='MOMENT_Y', DENOMINATOR='ROTY', CONSTANT=2*V0/cref, NAME='Cmq', BOUNDARIES=-1)
#  the following need to redimensionalize the moments by multiplying out the default reference_length, and dividing by span
pyfs.tools.stability_toolbox_new_coefficient(FRAME=2, UNITS='COEFFICIENTS', NUMERATOR='MOMENT_X', DENOMINATOR='ROTX', CONSTANT=2*V0/bref*cref/bref, NAME='Clp', BOUNDARIES=-1)
pyfs.tools.stability_toolbox_new_coefficient(FRAME=2, UNITS='COEFFICIENTS', NUMERATOR='MOMENT_Z', DENOMINATOR='ROTX', CONSTANT=2*V0/bref*cref/bref, NAME='Cnp', BOUNDARIES=-1)
pyfs.tools.stability_toolbox_new_coefficient(FRAME=2, UNITS='COEFFICIENTS', NUMERATOR='MOMENT_X', DENOMINATOR='ROTZ', CONSTANT=2*V0/bref*cref/bref, NAME='Clr', BOUNDARIES=-1)
pyfs.tools.stability_toolbox_new_coefficient(FRAME=2, UNITS='COEFFICIENTS', NUMERATOR='MOMENT_Z', DENOMINATOR='ROTZ', CONSTANT=2*V0/bref*cref/bref, NAME='Cnr', BOUNDARIES=-1)


### SET SOLVER SETTINGS
pyfs.set_solver.solver_settings(angle_of_attack=0.0, sideslip_angle=0.0, 
                                    freestream_velocity=V0, iterations=500, 
                                    convergence_limit=1e-05, forced_run='DISABLE', 
                                    compressibility='DISABLE', 
                                    reference_velocity=V0, 
                                    reference_area=sref, reference_length=cref, 
                                    processors=12, wake_size=1000)
pyfs.solver.initialize_solver(surfaces=-1, load_frame=2, symmetry_type='NONE',
                      proximity_avoidance='DISABLE', stabilization='ENABLE', stabilization_strength=1.0,
                      fast_multipole='ENABLE', wake_termination_x='DEFAULT')

for i in range(len(angle_array)):
    angle = angle_array[i]
    pyfs.set_solver.set_aoa(angle=angle)
    pyfs.tools.compute_stability_coefficients()

pyfs.exec_solver.close_flightstream()

# Script commands done
pyfs.script.write_to_file() # write out the script 
# pyfs.script.run_script(fsexe_path=fsexe_path, hidden=False) # uncomment to run