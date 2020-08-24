
import numpy as np


def get_simulation_data():

    SAMPLE_FREQUENCY = 50 # Hz
    MEASUREMENT_TIME = 10   # s

    SINE_FREQUENCY   = 0.2  # Hz
    PHASE_SHIFT      = np.pi/4 # rad

    time_vector = np.arange( 0, MEASUREMENT_TIME + 1/SAMPLE_FREQUENCY, 1/SAMPLE_FREQUENCY )

    pos_x = np.random.uniform(low=-0.04, high=0.04, size=len(time_vector)) + np.sin( 2*np.pi*SINE_FREQUENCY*time_vector + PHASE_SHIFT )
    pos_y = np.random.uniform(low=-0.04, high=0.04, size=len(time_vector)) + np.sin( 0.7*np.pi*SINE_FREQUENCY*time_vector )

    data = np.zeros( [3,len(time_vector)] )

    data[ 0,: ] = time_vector
    data[ 1,: ] = pos_x
    data[ 2,: ] = pos_y

    return data