package main

import "fmt"

func twoSum(nums []int, target int) []int {
    numsMap := make(map[int]int)
    for i, num := range nums {
        diff := target - num
        if index, ok := numsMap[diff]; ok {
			return []int{index, i}
		}
		numsMap[num] = i
    }
	return []int{}
}

func main() {
    nums := []int{2, 7, 11, 15}
    target := 9
    result := twoSum(nums, target)
    fmt.Println(result)
}
