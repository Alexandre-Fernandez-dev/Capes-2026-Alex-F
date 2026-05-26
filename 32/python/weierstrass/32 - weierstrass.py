# %%
from matplotlib.pylab import plot
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import ticker

# %%

# from scipy.fft import rfft, rfftfreq
def somme_partielle(x: np.ndarray, a: float, b: int, N: int) -> np.ndarray:
    n = np.arange(N)  # (N,)
    tosum = a**n * np.cos(b**n * np.pi * (x[:, np.newaxis]))
    return np.sum(tosum, axis=1)


# %%
x = np.linspace(-1, 1, 1000)
y = somme_partielle(x, 0.3, 7, 30)

pp = plt.plot(x, y)
plt.show()
