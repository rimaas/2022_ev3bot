import numpy as np
import matplotlib.pyplot as plt

def checkplot(x,y):

    num_samples, num_axis = np.shape(y)

    if type(x) == int:

        x_axis = np.arange( 0, num_samples )

    else:

        x_axis = x

    # plot individual figures
    fig_id, DataArray = plt.subplots(3, sharex=True)
    for axis_num in range(num_axis):

        DataArray[axis_num].plot(x_axis, y[:,axis_num])
        DataArray[axis_num].set_ylabel('column ' + str( axis_num ))

    plt.xlabel('x axis [?]')
    plt.show()

    # plot combined figures
    for axis_num in range(num_axis):

        plt.plot(x_axis, y)

    plt.ylabel('all columns')
    plt.xlabel('x axis [?]')
    plt.show()

    return

def perform_sim(num, den, w, meas_info):

    # 1. convert time domain signals to frequency domain signals
    # 2. compute plant for same frequency spectrum as input signal
    # 3. multiply plant with input spectrum
    # 4. compute ifft of resulting frequency domain output signal(s)
    # 5. (optional) add noise to 'measurement'



    u = 1
    y = 1

    return u, y

# Define Object
class GenerateInjection:

    # Constructor
    def __init__(self, test_name, f_desired):

        # How to obtain these settings? User-defined hard coded?
        fs = 100  # [Hz]
        Ts = 6  # [s]
        meas_type = 'closed-loop'
        exp_type  = 'periodic' # 'non-periodic', 'periodic', 'LPA
        P = 3 # number of periods (periodic) or number of averages (non-periodic)

        ## end user-definitions ##

        ## compute injection signal ##

        # total number of samples per period
        N = int((fs * Ts) / P)

        # total number of excited frequencies
        num_of_excitations = len(f_desired)

        # spectral distance
        df = fs/N

        # full spectrum [Hz]
        full_spectrum = np.arange(0, fs/2 + df, df)

        # remove DC and Nyquist terms
        full_spectrum = np.delete(full_spectrum, len(full_spectrum) - 1) # Nyquist
        full_spectrum = np.delete(full_spectrum, 0) # DC

        # define excitation lines
        exlines_all = np.arange(1, len(full_spectrum) + 1, 1)

        # can loop below in a more elegant way?
        cnt = 0
        exlines = np.zeros(len(full_spectrum), dtype=bool)
        for k in range(len(f_desired)):
            for n in range(len(full_spectrum)):
                if full_spectrum[n] == f_desired[k]:
                    exlines[n] = 'True'

        # print(full_spectrum[exlines])

        ## compute realization (create a function which is called M times)

        # compute random phase
        phi = np.random.uniform(low=0, high=2*np.pi, size=(num_of_excitations,))

        # complex vector with random phases and unitary amplitude
        u_dr = np.zeros((1, 1, N))
        # u_dr[1,1,exlines] = np.exp(1j * phi) # three dimensional matrix will not work... how to do this?

        # create additional (phase) randomness vector
        u_dp = np.exp(1j * np.ones((1, N)))    # 1 should be replaced by nu (number of inputs)

        # define hadamard matrix (to create orthogonal inputs)
        T = 1 # currently only SISO support



        print(np.abs(u_dr))

        ## wrapup

        self.test_name = test_name
        self.measType = meas_type
        self.expType = exp_type
        self.Ts = Ts
        self.fs = fs
        self.P = int( P )

# Define Object
class TransferMeasurement:

    # Class attribute
    dataType = 'Frequency Domain'

    # Constructor
    def __init__(self, wData, uData, yData, time):
        self.time       = time
        self.wData      = wData
        self.uData      = uData
        self.yData      = yData

    # Method convert_time_to_freq
    def convert_time_to_freq(self, meas_info):

        # define local variables
        N               = int( meas_info.fs * meas_info.Ts )
        fs              = int(meas_info.fs)

        N_per           = int(N/meas_info.P)
        df              = int(fs / N_per)

        self.freq_ax    = np.arange( 0, (meas_info.fs/2), df )

        wData_reshaped, uData_reshaped, yData_reshaped = self._reshape_(meas_info.P)

        if meas_info.expType == 'non-periodic':

            HanningWindow = np.tile([np.hanning(N_per)], (meas_info.P,1)).T

            wData_preprocessed = np.multiply(wData_reshaped, HanningWindow)
            uData_preprocessed = np.multiply(uData_reshaped, HanningWindow)
            yData_preprocessed = np.multiply(yData_reshaped, HanningWindow)

        else:

            print(' ')
            print('No windowing required')
            print(' ')

            wData_preprocessed = wData_reshaped
            uData_preprocessed = uData_reshaped
            yData_preprocessed = yData_reshaped

        W_full = (2 / N_per) * np.fft.fft(wData_preprocessed, axis=0, norm=None)
        U_full = (2 / N_per) * np.fft.fft(uData_preprocessed, axis=0, norm=None)
        Y_full = (2 / N_per) * np.fft.fft(yData_preprocessed, axis=0, norm=None)

        index_delete = np.arange(int(N_per / 2), N_per, 1)

        self.W = np.delete(W_full, index_delete, axis=0)
        self.U = np.delete(U_full, index_delete, axis=0)
        self.Y = np.delete(Y_full, index_delete, axis=0)

    # Method plot_freq_domain
    def plot_freqdomain(self):
        fig_id, DataArray = plt.subplots(3, sharex=True)

        fig_id.suptitle('Frequency Domain Data')

        DataArray[0].plot(self.freq_ax, np.abs(self.W), 'o')
        DataArray[0].set_ylabel('|W| [unit]')

        DataArray[1].plot(self.freq_ax, np.abs(self.U), 'o')
        DataArray[1].set_ylabel('|U| [unit]')

        DataArray[2].plot(self.freq_ax, np.abs(self.Y), 'o')
        DataArray[2].set_ylabel('|Y| [unit]')

        plt.xlabel('Frequency [Hz]')
        plt.show()

        fig_id, DataArray = plt.subplots(3, sharex=True)

        fig_id.suptitle('Frequency Domain Data')
        DataArray[0].plot(self.freq_ax, np.angle(self.W)*(180/np.pi), 'o')
        DataArray[0].set_ylabel('|W| [unit]')

        DataArray[1].plot(self.freq_ax, np.angle(self.U)*(180/np.pi), 'o')
        DataArray[1].set_ylabel('|U| [unit]')

        DataArray[2].plot(self.freq_ax, np.angle(self.Y)*(180/np.pi), 'o')
        DataArray[2].set_ylabel('|Y| [unit]')

        plt.xlabel('Frequency [Hz]')
        plt.show()

    # Method plot_timedomain
    def plot_timedomain(self):
        fig_id, DataArray = plt.subplots( 3, sharex=True )

        fig_id.suptitle( 'Time Domain Data' )
        DataArray[0].plot( self.time, self.wData )
        DataArray[0].plot( self.time, np.mean( self.wData )*np.ones( len( self.wData ) ), '--' )
        DataArray[0].set_ylabel( 'wData' )

        DataArray[1].plot( self.time, self.uData )
        DataArray[1].plot( self.time, np.mean( self.wData )*np.ones( len( self.uData ) ), '--' )
        DataArray[1].set_ylabel( 'uData' )

        DataArray[2].plot( self.time, self.yData )
        DataArray[2].plot( self.time, np.mean( self.wData )*np.ones( len( self.yData ) ), '--' )
        DataArray[2].set_ylabel( 'yData' )

        plt.xlabel('Time [s]')
        plt.show()

    def compute_nonperiodic_frf(self, meas_info):
        pass

    def compute_periodic_frf(self):
        pass

    def _reshape_(self, p):

        N_per           = int(len(self.wData) / p)

        wData_reshaped = np.zeros((N_per, p))
        uData_reshaped = np.zeros((N_per, p))
        yData_reshaped = np.zeros((N_per, p))

        for period in range(p):

            index_start               = period * N_per
            index_end                 = (period + 1) * N_per

            wData_reshaped[:, period] = self.wData[index_start:index_end]
            uData_reshaped[:, period] = self.uData[index_start:index_end]
            yData_reshaped[:, period] = self.yData[index_start:index_end]

        return wData_reshaped, uData_reshaped, yData_reshaped

f_min = 1
f_max = 49
df = 2

f_tmp = np.arange(f_min, f_max+df, df)
f_desired = np.delete(f_tmp, [4, 5, 6])

# define object
inj_signal = GenerateInjection('test_name_blabla', f_desired)

m = 2
k = 2000
d = 0.7

num = k
den = [m,d,k]

# inj_signal.values     injection values (time-domain)
# inj_signal.time       time vector
#u, y = perform_sim(num, den, inj_signal)

#### start data collection ####

# mean and standard deviation
mu, sigma = 0, 0.4

f = 3 # Hz
time = np.arange(0, inj_signal.Ts, 1/inj_signal.fs)

w = 1.0 * np.sin(f * 2 * np.pi * time)              # amplitude 1.0
u = 1.2 * np.sin(f * 2 * np.pi * time + np.pi)      # amplitude 1.2
y = 0.8 * np.sin(f * 2 * np.pi * time + np.pi/2)    # amplitude 0.8

# add measurement noise
w = w + np.random.normal(mu, sigma, inj_signal.Ts*inj_signal.fs)
u = u + np.random.normal(mu, sigma, inj_signal.Ts*inj_signal.fs)
y = y + np.random.normal(mu, sigma, inj_signal.Ts*inj_signal.fs)

#### end data collection ####



#### start main sequence ####

# define object
debug_measurement           = TransferMeasurement( w, u, y, time)

# plot time domain signals
debug_measurement.plot_timedomain()

# compute frequency domain signals
debug_measurement.convert_time_to_freq( inj_signal )

# plot frequency domain signals
debug_measurement.plot_freqdomain()

# compute nonperiodic FRF
#debug_measurement.compute_nonperiodic_frf( meas_info )

# compute periodic FRF
debug_measurement.compute_periodic_frf()