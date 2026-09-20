from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from icecream import ic  # noqa: F401

import numpy as np
import utils.debug  # noqa: F401
from matplotlib.axes import Axes # noqa: F401

from utils.complex_numbers import to_polar, to_rect # noqa: F401
from utils.harmonic import (
    get_harmonic_oscillation,
    get_period, # noqa: F401
    get_phase_time_shift, # noqa: F401
    get_phase_at, # noqa: F401
)
from utils.fourier import discrete_fourier_transform # noqa: F401
from utils.plotting import show_multi_plot, show_plot, show_subplots # noqa: F401
from utils.sampling import get_linspace


def task_1_2() -> None:
    sampling_frequency = 1024
    start = 0
    stop = 1
    t = get_linspace(start=start, stop=stop, fs=sampling_frequency)
    
    # <------------------------------------>
    # 1) Необходимо сгенерировать и визуализировать непрерывный сигнал
    frequency = 4
    
    ic(
        frequency,
        sampling_frequency,
    )
    
    y_1 = get_harmonic_oscillation(1, frequency, np.pi/3, wave=np.cos)(t)
    y_2 = get_harmonic_oscillation(1, 2*frequency, 0, wave=np.sin)(t)
    y = y_1 + y_2  # 5 вариант

    show_plot(
        t=t,
        func_val=y,
        title="cos(2*pi*f*t + pi/3) + sin(4*pi*f*t)",
    )
    # >------------------------------------<
    

    # <------------------------------------>
    # 2) Определить максимальную частоту в спектре данного сигнала.
    max_freq = frequency * 2 
    # >------------------------------------<
    
    
    # <------------------------------------>
    # 3) Определить минимальную необходимую частоту дискретизации
    # полученного сигнала (теорема Котельникова)
    min_freq_kotelnikov = max_freq * 2
    
    ic(
        max_freq,
        min_freq_kotelnikov,
    )
    # >------------------------------------<
    
    
    # <------------------------------------>
    # 4) Оцифровать сигнал с полученной частотой дискретизации, выбрав
    # требуемое число отсчетов сигнала на длительности 1 секунда, сохранить
    # полученные значения в массив, пока не озадачиваясь разрядностью АЦП,
    # просто выбранные с частотой дискретизации значения с теми уровнями,
    # которые имеет функция в полученных точках.
    step = len(y) // int(min_freq_kotelnikov * (stop - start)) 
    y_sampled = y[::step]
    t_sampled = t[::step]
    
    ic(
        y_sampled,
        t_sampled,
    )
    # >------------------------------------<
    
    
    # <------------------------------------>
    # 5) Выполнить прямое дискретное преобразование Фурье для массива
    # временных отсчетов сигнала и оценить ширину данного спектра. А также
    # объем памяти, требуемый для хранения данного массива (тип переменных в
    # массиве – на ваше усмотрение, float, int и пр.).
    y_dft = discrete_fourier_transform(y_sampled)
    N = len(y_dft)
    freqs = np.arange(N) * min_freq_kotelnikov / N
    amp = np.abs(y_dft) / N
    
    ic(
        freqs,
        amp,
    )

    threshold = 1e-6
    half = N // 2 + 1  # без зеркальной части
    significant = np.array([freqs[k] for k in range(half) if amp[k] > threshold])
    spectrum_width = significant.max()
   
    ic(
        spectrum_width
    )

    def draw_signal(ax: Axes) -> None:
        ax.plot(t, y)
        ax.stem(t_sampled, y_sampled, linefmt="r-", markerfmt="ro", basefmt=" ")

    def draw_full_spectrum(ax: Axes) -> None:
        ax.stem(freqs, amp)

    def draw_half_spectrum(ax: Axes) -> None:
        ax.stem(freqs[:half], amp[:half])
        ax.axhline(threshold, color="gray", linestyle="--", label="порог")
        ax.axvline(spectrum_width, color="r", linestyle=":", label="ширина спектра")
        ax.legend()

    show_subplots(
        draw_funcs=[draw_signal, draw_full_spectrum, draw_half_spectrum],
        titles=[
            "Сигнал и отсчеты",
            "Амплитудный спектр, все N гармоник (зеркальная часть)",
            "Амплитудный спектр без зеркальной части",
        ],
        figsize=(9, 10),
    )
    # >------------------------------------<
                

def main() -> None:
    task_1_2()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass
