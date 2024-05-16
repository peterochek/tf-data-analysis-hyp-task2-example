import pandas as pd
import numpy as np
from scipy.stats import ks_2samp


chat_id = 285458518  # Ваш chat ID, не меняйте название переменной


def solution(x: np.array, y: np.array) -> bool:
    res = ks_2samp(x, y)
    return res.pvalue <= 0.1
