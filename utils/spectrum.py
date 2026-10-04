import numpy as np

from utils.fourier import discrete_fourier_transform


def get_spectrum(x: np.ndarray, fs: float) -> tuple[np.ndarray, np.ndarray]:
    N = len(x)
    # X = discrete_fourier_transform(x)
    X = np.fft.fft(x)
    half = N // 2 + 1  # без зеркальной части

    return np.arange(half) * (fs / N), np.abs(X[:half]) / N


def get_spectrum_width(freqs: np.ndarray, amp: np.ndarray, level: float = 0.01) -> float:
    return freqs[amp > level * amp.max()].max()
