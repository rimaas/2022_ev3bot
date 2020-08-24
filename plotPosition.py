import matplotlib.pyplot as plt

def plot_absolute_position( DataObj ):

    pos_x    = DataObj.trace_x
    pos_y    = DataObj.trace_y

    # plot the data
    plt.plot( pos_x, pos_y, label='Absolute Position')

    # add a legend
    plt.legend()

    # add a title
    plt.title( DataObj.creation_date )

    # show the plot
    plt.show()

def plot_tracking_error( setp, pos ):
    pass

def plot_positions_time( DataObj ):

    time_vec = DataObj.time_vector
    pos_x    = DataObj.trace_x
    pos_y    = DataObj.trace_y

    # plot the data
    plt.plot( time_vec, pos_x, label='Trace X' )
    plt.plot( time_vec, pos_y, label='Trace Y')

    # add a legend
    plt.legend()

    # add a title
    plt.title( DataObj.creation_date )

    # show the plot
    plt.show()


#def plot_timedomain(self):
#    fig_id, DataArray = plt.subplots(3, sharex=True)
#
#    fig_id.suptitle('Time Domain Data')
#    DataArray[0].plot(self.time, self.wData)
#    DataArray[0].plot(self.time, np.mean(self.wData) * np.ones(len(self.wData)), '--')
#    DataArray[0].set_ylabel('wData')
#
#    DataArray[1].plot(self.time, self.uData)
#    DataArray[1].plot(self.time, np.mean(self.wData) * np.ones(len(self.uData)), '--')
#    DataArray[1].set_ylabel('uData')
#
#    DataArray[2].plot(self.time, self.yData)
#    DataArray[2].plot(self.time, np.mean(self.wData) * np.ones(len(self.yData)), '--')
#    DataArray[2].set_ylabel('yData')
#
#    plt.xlabel('Time [s]')
#    plt.show()