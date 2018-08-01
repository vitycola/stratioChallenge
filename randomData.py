from datetime import datetime
import random
import numpy as np
import scipy.stats as ss
import sys

dataVol = int(sys.argv[1]) # Number of lines to create
mu = 5 # Average call minutes duration

def calc_prob(): # Create a probabilistic array to speak X minutes
    massf = []
    for min in range(60):
        massf.append(ss.poisson.pmf(min, mu))
    return massf

def create_phone(): # Create random phone numbers with format 'XXX-XXX-XXX'
    phone = '%03d' % random.choice(range(0, 1000)) + "-" + '%03d' % random.choice(range(0, 1000)) + "-" + '%03d' % random.choice(range(0, 1000))
    return phone

if __name__ == '__main__':


    for i in range(dataVol):

        hour = np.random.choice(np.arange(0, 3), p=[0.85, 0.1,0.05]) # Calculate hours taking in account the probability to speak 0 or 1 hours
        minute = np.random.choice(np.arange(0, 60), p=calc_prob()) # Calculate speaked minutes taking in account a poisson probability
        second = random.choice(range(00, 59))
        birth_date = str(hour)+":"+str(minute)+":"+str(second)
        date = datetime(2018, 10, 1, hour, minute, second).strftime('%H:%M:%S')

        print(date + "," + create_phone())





