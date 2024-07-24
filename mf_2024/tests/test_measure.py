import Measure

import numpy as np 

def calculate_angle():
    r1 = np.array([0,0,-1])
    r2 = np.array([0,0,0])
    r3 = np.array([1,0,0])

    exp_val = 90 

assert Measure.calculate_angle(r1,r2,r3, degree = True) == exp_val 