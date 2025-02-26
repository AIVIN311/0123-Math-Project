import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
import numpy as np
from math_models.model_0123 import logistic_wisdom_growth, adaptive_entropy_growth

class TestWisdomEvolution(unittest.TestCase):
    def test_logistic_wisdom_growth(self):
        """ 測試智慧密度增長模型 """
        result = logistic_wisdom_growth(10, 5, 0.3, 5, 1.0, 1)
        expected = 5 / (1 + np.exp(-0.3 * (10 - 5 + 1.0 * 0.2)))
        self.assertAlmostEqual(result, expected, places=5)

    def test_adaptive_entropy_growth(self):
        """ 測試熵的增長模型 """
        entropy = 2.0
        result = adaptive_entropy_growth(entropy, 2)  # 分裂階段
        self.assertAlmostEqual(result, entropy * 1.1, places=5)

if __name__ == "__main__":
    unittest.main()
