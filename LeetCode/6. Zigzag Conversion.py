import unittest


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s
        rows = [''] * numRows
        cur_row = 0
        direction = 1
        for char in s:
            rows[cur_row] += char
            if cur_row == 0:
                direction = 1
            elif cur_row == numRows - 1:
                direction = -1
            cur_row += direction
        return ''.join(rows)


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_convert(self):
        # Тестирование с numRows = 3
        s = "PAYPALISHIRING"
        numRows = 3
        expected_result = "PAHNAPLSIIGYIR"
        self.assertEqual(self.solution.convert(s, numRows), expected_result)

        # Тестирование с numRows = 4
        s = "PAYPALISHIRING"
        numRows = 4
        expected_result = "PINALSIGYAHRPI"
        self.assertEqual(self.solution.convert(s, numRows), expected_result)

        # Тестирование с numRows = 1
        s = "PAYPALISHIRING"
        numRows = 1
        expected_result = "PAYPALISHIRING"
        self.assertEqual(self.solution.convert(s, numRows), expected_result)

        # Тестирование с numRows >= len(s)
        s = "PAYPALISHIRING"
        numRows = 20
        expected_result = "PAYPALISHIRING"
        self.assertEqual(self.solution.convert(s, numRows), expected_result)


if __name__ == "__main__":
    unittest.main()