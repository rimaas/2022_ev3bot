# observer_main.py
#
# Main file designed to generate a (simulated) signal and evaluate the performance
# of various observers
#
# Rick van der Maas
# v001  10-03-2020      :   initial version

import numpy as np
import matplotlib.pyplot as plt
import random
import datetime

# import functions
from plotPosition import * # plot_absolute_position, plot_tracking_error, plot_positions_time
from get_simulation_data import * # get_simulation_data
from observerFunctions import * # kalmanFilterFun

# StudlyCaps - class names
# ALL_CAPS - constants
# snake_case - variables, methods, and functions

class DataObject:

    # constructor
    def __init__(self, trace_name, data):

        self.creation_date  = datetime.datetime.now()
        self.trace_name     = trace_name
        self.time_vector    = data[ 0,: ]
        self.trace_x        = data[ 1,: ]
        self.trace_y        = data[ 2,: ]

    # Method to perform Kalman Filter
    def kalman_filter( self ):

        dataSampleFiltered = np.zeros([3, len(self.time_vector)])

        for k in range( 0, len( self.time_vector ) ):

            # initialize variables
            dataSample          = np.zeros([3, 1])

            # get data from object
            dataSample[ 0 ]     = self.time_vector[k]
            dataSample[ 1 ]     = self.trace_x[k]
            dataSample[ 2 ]     = self.trace_y[k]

            # perform Kalman filter operation
            outData = kalmanFilterFun(dataSample)

            print(dataSampleFiltered[:][k])

            dataSampleFiltered[:][k] = outData

            a=b

        return dataSampleFiltered

    # Method to perform Extended Kalman Filter
    def extended_kalman_filter( self ):
        # for k = 1 : len( time_vector )
            #filter per sample



        FilteredDataObj = 0

        return FilteredDataObj

    # Method to perform Unscented Kalman Filter
    def unscented_kalman_filter( self ):
        # for k = 1 : len( time_vector )
            #filter per sample



        FilteredDataObj = 0

        return FilteredDataObj

    # Method to perform Particle Filter
    def particle_filter( self ):
        # for k = 1 : len( time_vector )
            #filter per sample



        FilteredDataObj = 0

        return FilteredDataObj

# get simulation data
sim_data = get_simulation_data()

# define object
DataObj = DataObject( 'ev3bot_test', sim_data )

# execute Kalman Filter
dataSampleFiltered = DataObj.kalman_filter()

print( dataSampleFiltered )

# do some plotting
plot_absolute_position( DataObj )

plot_positions_time( DataObj )