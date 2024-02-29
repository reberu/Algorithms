# Given a signed 32-bit integer x, return x with its digits reversed.
# If reversing x causes thevalue to go outside the signed 
# 32-bit integer range [-2 ** 31, 2 **31 - 1], then return 0.
import unittest


class Solution:
    def reverse(self, x: int) -> int:
        result = int(str(x)[::-1]) if x > 0 else int(str(x * -1)[::-1]) * -1
        return result if -2 ** 31 <= result < 2 ** 31 else 0


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_reverse(self):
        # Тестирование натурального числа
        num = 123
        expected_result = 321
        self.assertEqual(self.solution.reverse(num), expected_result)

        # Тестирование отрицательного числа
        num = -123
        expected_result = -321
        self.assertEqual(self.solution.reverse(num), expected_result)

        # Тестирование натурального числа, с 0 в конце
        num = 120
        expected_result = 21
        self.assertEqual(self.solution.reverse(num), expected_result)

        # Тестирование числа, переворот которого выходит за рамки int 32 bit
        num = 1534236469
        expected_result = 0
        self.assertEqual(self.solution.reverse(num), expected_result)


if __name__ == "__main__":
    unittest.main()
