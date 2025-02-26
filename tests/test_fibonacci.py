import sys
import os

# 讓 Python 找到 math_models
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# 重新導入 math_models
from math_models.model_0123 import logistic_wisdom_growth, adaptive_entropy_growth
import unittest
from math_models.fibonacci import fibonacci

class TestFibonacci(unittest.TestCase):
    def test_fibonacci(self):
        self.assertEqual(fibonacci(0), 0)
        self.assertEqual(fibonacci(1), 1)
        self.assertEqual(fibonacci(5), 5)
        self.assertEqual(fibonacci(10), 55)

if __name__ == "__main__":
    unittest.main()
