'''
Example application of MSET to a scalar time series 
by applying a time delayed embedding. The time series used 
here is a noisy sinusoid with a transition in its period 
halfway through the observation period.
'''

import numpy as np
import mset
import tde

n = 10000 # making 10000 iterations 
thresh = 0.1 # threshold of 0.1

t = np.linspace(0, 10*np.pi, n) #function to generate a general sequence out of the range of numbers provided 
x = np.sin(t) + 0.1*np.random.randn(n) #sine funtion with noise added 

# introduce a new type of signal halfway through.
heavy = (1 + np.tanh( 0.5*(t-5*np.pi) ))/2.
x += heavy*np.sin(t/2) + heavy*(-np.sin(t))

# time delayed embedding based on analytical 
# zero-autocorrelation time of pi/2 for a sinusoid.
# generically this requires you have some knowledge of 
# your problem of interest, or additional observation time 
# sufficient to get a numerical zero-autocorrelation time.
delay = int((np.pi/2)/(t[1] - t[0]))

ms = mset.MSET() # mset module 
X = tde.tde(x) #synthetic dataset 
fig,ax = ms.visualize_mset(x,thresh,delay, verbosity=1)
fig.show()

