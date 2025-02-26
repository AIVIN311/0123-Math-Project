import sys
import os

# 讓 Python 找到 math_models
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# 重新導入 math_models
from math_models.model_0123 import logistic_wisdom_growth, adaptive_entropy_growth
import unittest
from math_models.model_0123 import logistic_wisdom_growth, adaptive_entropy_growth

class Test0123Evolution(unittest.TestCase):
    def test_entropy_growth(self):
        self.assertGreater(adaptive_entropy_growth(1, 2), 1)

    def test_logistic_growth(self):
        self.assertGreater(logistic_wisdom_growth(10, 5, 0.3, 5, 1, 1), 0)

if __name__ == "__main__":
    unittest.main()
