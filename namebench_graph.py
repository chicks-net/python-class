#!/usr/local/bin/python

from scipy import *
#from scipy.signal import *
from matplotlib.pyplot import *

filename = 'namebench_2013-12-27_0205.csv'

data = loadtxt( filename, delimiter=',', skiprows=1,
	usecols=(1,5) ,
	dtype=[('server name','a'),('duration','f8')]
)
