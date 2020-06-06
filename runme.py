import ctypes
import sys
import numpy
import numpy.ctypeslib
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt

n = 1000

double_p = numpy.ctypeslib.ndpointer(dtype=float, ndim=1, flags='CONTIGUOUS')
double = ctypes.c_double

# connect to the module that does the calculation
try:
    libsim = ctypes.cdll.LoadLibrary('simulate.so')
except OSError:
    print('Missing simulate.so; aborting.')
    print('Did you forget to run "make" first?')
    sys.exit()

simulate = libsim.simulate
simulate.argtypes = [ctypes.c_int64, double_p, double_p, double_p, double, double, double]
simulate.restype = None


ax = plt.axes(projection='3d')

for x0, color in [(1, 'blue'), (1.01, 'red'), (1.02, 'green')]:
    xs = numpy.zeros(n)
    ys = numpy.zeros(n)
    zs = numpy.zeros(n)
    simulate(n, xs, ys, zs, x0, 0, 0)
    ax.plot3D(xs, ys, zs, color=color)

plt.show()
