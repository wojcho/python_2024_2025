import unittest
from main import cantor_set


class TestCantorSet(unittest.TestCase):

    def test_hardcoded(self):
        data = [1]
        rules = {1: [1, 0, 1], 0: [0, 0, 0]}
        self.assertEqual(cantor_set.iterate_rewrite(data, rules, 0), [1])
        self.assertEqual(cantor_set.iterate_rewrite(data, rules, 1), [1, 0, 1])
        self.assertEqual(cantor_set.iterate_rewrite(data, rules, 2), [1, 0, 1, 0, 0, 0, 1, 0, 1])
        with self.assertRaises(RuntimeError):
            cantor_set.iterate_rewrite(data, rules, -1)


if __name__ == '__main__':
    unittest.main()
