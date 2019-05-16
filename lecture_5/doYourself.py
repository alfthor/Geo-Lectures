import Lec5_geyserEx_functions as h
import matplotlib.pyplot as plt
import numpy as np


julianday, evclass = h.read_snuffler_marker("geyser_markers.txt",length=0)
julianday = np.sort(julianday)
tDiff = np.diff(julianday)*24*60
plt.figure(1)
plt.plot(julianday)

plt.figure(2)
plt.plot(tDiff,'.')
plt.show()