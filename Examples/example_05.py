# ----------- Example_05 --------------
# Run and plot a simple simple step wind simulation
# -------------------------------------
#
# In this example:
#   - Load turbine from saved pickle
#   - Tune a controller
#   - Run and plot a simple step wind simulation
#
# Note - you will need to have a compiled controller in ROSCO, and 
#        properly point to it in the `controller_path` variable

# Python modules
import matplotlib.pyplot as plt 
import numpy as np
import yaml 
# ROSCO toolbox modules 
from ROSCO_toolbox import controller as wtc_controller
from ROSCO_toolbox import turbine as wtc_turbine
from ROSCO_toolbox import sim as wtc_sim
from ROSCO_toolbox import utilities as wtc_utilities
from ROSCO_toolbox import control_interface as wtc_ci

# Specify controller dynamic library path and name
lib_name = ('../ROSCO/build/libdiscon.dylib')

# Load turbine model from saved pickle
turbine = wtc_turbine.Turbine
turbine = turbine.load('NREL5MW_saved.p')

# Load controller library
controller_int = wtc_ci.ControllerInterface(lib_name)

# Load the simulator
sim = wtc_sim.Sim(turbine,controller_int)

# Define a wind speed history
dt = 0.1
tlen = 1000      # length of time to simulate (s)
ws0 = 7         # initial wind speed (m/s)
t= np.arange(0,tlen,dt) 
ws = np.ones_like(t) * ws0
# add steps at every 100s
for i in range(len(t)):
    ws[i] = ws[i] + t[i]//100

# Run simulator and plot results
sim.sim_ws_series(t,ws,rotor_rpm_init=4)
plt.show()

