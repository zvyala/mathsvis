
from oct2py import Oct2Py

def compute_data():

    octave = Oct2Py()
    
    octave.addpath('octave_scripts')
    
    result = octave.compute_sine_wave()
    
    return result

