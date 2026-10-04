from typing import Callable
import numpy as np


def discrete_fourier_transform(x: np.ndarray) -> np.ndarray:
    N = len(x)
    X = []
    for k in range(N):
        s = 0
        for n in range(N):
            s += x[n] * np.exp(-2j * np.pi * k * n / N)
        X.append(s)
    
    return np.array(X)
