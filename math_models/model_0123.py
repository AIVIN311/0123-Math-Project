import numpy as np

def logistic_wisdom_growth(time, W_max, r, t_0, entropy, stage):
    """智慧密度的 Logistic Growth 模型"""
    if stage == 0:
        stage_factor = 0.5  # 靈：較慢增長
    elif stage == 1:
        stage_factor = 1.0  # 存在：正常增長
    elif stage == 2:
        stage_factor = 1.5  # 分裂：加速增長
    elif stage == 3:
        stage_factor = 0.7  # 整合：增長放緩
    else:
        stage_factor = 1.0

    adjusted_time = time - t_0 + entropy * 0.2
    return W_max / (1 + np.exp(-r * stage_factor * adjusted_time))

def adaptive_entropy_growth(entropy, stage):
    """根據當前階段調整熵值增長速率"""
    if stage == 0:
        growth_factor = 1.05
    elif stage == 1:
        growth_factor = 1.07
    elif stage == 2:
        growth_factor = 1.10
    elif stage == 3:
        growth_factor = 1.05
    else:
        growth_factor = 1.05
    return entropy * growth_factor
