import matplotlib.pyplot as plt
import numpy as np

N_max = 9
some_threshold = 50

x = np.linspace(-2, 1, 800)
y = np.linspace(-1.5, 1.5, 600)
c = x[:, np.newaxis] + 1j*y[np.newaxis, :]

z = c
for j in range(N_max):
    z = z**2 + c


mask = (abs(z) < some_threshold)

plt.imshow(mask.T, extent=[-2, 1, -1.5, 1.5])

plt.gray()
plt.savefig('mandelbrot.png')