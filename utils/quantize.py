import numpy as np


def quantize(x: np.ndarray, bits: int) -> np.ndarray:
    levels = 2**bits - 1  # самый большой код АЦП, например 7 для 3 бит
    x_min = min(x)
    x_max = max(x)
    step = (x_max - x_min) / levels  # на сколько меняется сигнал при переходе на следующий код

    result = []
    for value in x:
        # 1) сколько шагов помещается между минимумом и текущим значением
        code = (value - x_min) / step

        # 2) округляем до целого - это и есть код АЦП
        code = int(code + 0.5)

        # 3) всё, что вышло за диапазон 0..levels, обрезаем
        if code < 0:
            code = 0
        if code > levels:
            code = levels

        # 4) переводим код обратно в амплитуду
        result.append(x_min + code * step)

    return np.array(result)


def quantize_np(x: np.ndarray, bits: int) -> np.ndarray:
    levels = 2**bits - 1
    x_min, x_max = x.min(), x.max()

    # растягиваем сигнал на диапазон 0..levels и округляем до кода АЦП
    code = np.round((x - x_min) / (x_max - x_min) * levels)
    code = np.clip(code, 0, levels)

    # возвращаем в исходный масштаб
    return code / levels * (x_max - x_min) + x_min
