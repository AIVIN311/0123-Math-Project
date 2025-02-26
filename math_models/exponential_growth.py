def exponential_growth(initial_value, rate, time):
    """ 指數增長函數 P(t) = P0 * e^(rt) """
    import math
    return initial_value * math.exp(rate * time)
