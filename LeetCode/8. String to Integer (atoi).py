# Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer (similar to C/C++'s atoi function).
import unittest


class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if not s:
            return 0
        modification = 1
        if s[0] == "-":
            modification = -1
            s = s[1:]
        elif s[0] == "+":
            s = s[1:]
        num = 0
        for char in s:
            if char.isdigit():
                num = num * 10 + int(char)
            else:
                break
        num *= modification
        if -2 ** 31 <= num < 2 ** 31:
            return num
        return -2 ** 31 if modification == -1 else 2 ** 31 - 1


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_myAtoi(self):
        # Тест 1
        string = "42"
        expected_result = 42
        self.assertEqual(self.solution.myAtoi(string), expected_result)

        # Тест 2
        string = "   -42"
        expected_result = -42
        self.assertEqual(self.solution.myAtoi(string), expected_result)

        # Тест 3
        string = "4193 with words"
        expected_result = 4193
        self.assertEqual(self.solution.myAtoi(string), expected_result)

        # Тест 4
        string = "words and 987"
        expected_result = 0
        self.assertEqual(self.solution.myAtoi(string), expected_result)

        # Тест 5
        string = ".1"
        expected_result = 0
        self.assertEqual(self.solution.myAtoi(string), expected_result)

        # Тест 6
        string = "+-12"
        expected_result = 0
        self.assertEqual(self.solution.myAtoi(string), expected_result)

        # Тест 7
        string = "-91283472332"
        expected_result = -2147483648
        self.assertEqual(self.solution.myAtoi(string), expected_result)

        # Тест 8
        string = "3.14159"
        expected_result = 3
        self.assertEqual(self.solution.myAtoi(string), expected_result)

        # Тест 9
        string = "-+12"
        expected_result = 0
        self.assertEqual(self.solution.myAtoi(string), expected_result)

        # Тест 9
        string = "00000-42a1234"
        expected_result = 0
        self.assertEqual(self.solution.myAtoi(string), expected_result)


if __name__ == "__main__":
    unittest.main()
