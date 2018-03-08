from ..max_profit import solution
import unittest


class MaxProfitTester(unittest.TestCase):

    def test_1(self):
        x = [0, 100]
        e = dict(buy_idx=0, sell_idx=1, max_profit=100)
        y = solution(x)
        self.assertEqual(e, y)

    def test_2(self):
        x = [100, 300, 20, 290]
        e = dict(buy_idx=2, sell_idx=3, max_profit=270)
        y = solution(x)
        self.assertEqual(e, y)
