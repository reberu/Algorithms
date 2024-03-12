package main

import "fmt"

func searchInsert(nums []int, target int) int {
	left, right := 0, len(nums) - 1
	for left <= right {
		middle := left + (right - left) / 2
		value := nums[middle]
		switch {
			case value < target:
				left = middle + 1
			case value > target:
				right = middle - 1
			default:
				return middle
		}
	}
	return left
}

func main() {
    nums, target := []int{1, 3, 5, 6}, 5
	fmt.Println(searchInsert(nums, target))
}
