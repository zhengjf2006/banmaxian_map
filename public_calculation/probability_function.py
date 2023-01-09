import numpy as np


def get_gaussian_probability(value, mean=0.0, sigma=15.0):
    probability = 1 / np.sqrt(2 * np.pi) / sigma * np.exp(-0.5 * pow((value - mean) / sigma, 2))
    standard_probability = 1 / np.sqrt(2 * np.pi) / sigma * np.exp(-0.5 * pow(0 / sigma, 2))
    uniform_probability = probability / standard_probability
    return uniform_probability
