import sys
import os

# 讓 Python 找到 math_models
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# 重新導入 math_models
from math_models.model_0123 import logistic_wisdom_growth, adaptive_entropy_growth
import unittest
from math_models.exponential_growth import exponential_growth

class TestExponentialGrowth(unittest.TestCase):
    def test_growth(self):
        self.assertAlmostEqual(exponential_growth(1, 0.1, 10), 2.718, places=3)

if __name__ == "__main__":
    unittest.main()
