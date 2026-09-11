# 5 вариант

import matplotlib.pyplot as plt
from scipy.fftpack import fftfreq, fft
import numpy as np
from numpy import cos, sin, pi

f = 3
y = lambda t: cos(2*pi*f*t + pi/3) + sin(4+pi*f*t)

x = np.linspace(0, 10, 1000)

y_x = y(x)

fig, ax = plt.subplots()
ax.plot(x, y_x)
ax.set(xlabel='t', ylabel='y', title='y = cos(2*pi*f*t + pi/3) + sin(4+pi*f*t)')

plt.show()

max_freq = f*2

min_freq_kotelnikov = max_freq * 2

