# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
# The overall run time complexity should be O(log (m+n)).
import unittest
from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        len_nums1, len_nums2 = len(nums1), len(nums2)
        if len_nums1 > len_nums2:
            return self.findMedianSortedArrays(nums2, nums1)

        low, high = 0, len_nums1
        while low <= high:
            partition_nums1 = (low + high) // 2
            partition_nums2 = (len_nums1 + len_nums2 + 1) // 2 - partition_nums1

            max_left_nums1 = float('-inf') if partition_nums1 == 0 else nums1[partition_nums1 - 1]
            min_right_nums1 = float('inf') if partition_nums1 == len_nums1 else nums1[partition_nums1]
            max_left_nums2 = float('-inf') if partition_nums2 == 0 else nums2[partition_nums2 - 1]
            min_right_nums2 = float('inf') if partition_nums2 == len_nums2 else nums2[partition_nums2]

            if max_left_nums1 <= min_right_nums2 and max_left_nums2 <= min_right_nums1:
                if (len_nums1 + len_nums2) % 2 == 0:
                    return (max(max_left_nums1, max_left_nums2) + min(min_right_nums1, min_right_nums2)) / 2
                else:
                    return float(max(max_left_nums1, max_left_nums2))
            elif max_left_nums1 > min_right_nums2:
                high = partition_nums1 - 1
            else:
                low = partition_nums1 + 1


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_findMedianSortedArrays(self):
        # Тестирование массивов разной длины
        nums1 = [1, 3]
        nums2 = [2]
        expected_result = 2.0
        self.assertEqual(self.solution.findMedianSortedArrays(nums1, nums2), expected_result)

        # Тестирование массивов одинаковой длины
        nums1 = [1, 2]
        nums2 = [3, 4]
        expected_result = 2.5
        self.assertEqual(self.solution.findMedianSortedArrays(nums1, nums2), expected_result)

        # Тестирование пустых массивов
        nums1 = []
        nums2 = [1]
        expected_result = 1.0
        self.assertEqual(self.solution.findMedianSortedArrays(nums1, nums2), expected_result)

        nums1 = []
        nums2 = [2, 3]
        expected_result = 2.5
        self.assertEqual(self.solution.findMedianSortedArrays(nums1, nums2), expected_result)

        # Тестирование массивов с одинаковыми элементами
        nums1 = [1, 1, 1, 1, 1]
        nums2 = [1, 1, 1, 1, 1]
        expected_result = 1.0
        self.assertEqual(self.solution.findMedianSortedArrays(nums1, nums2), expected_result)

if __name__ == "__main__":
    unittest.main()
