package main

import "fmt"

func mySqrt(x int) int {
	low, high := 0, x
	for low <= high {
		mid := (low + high) / 2
		if mid * mid == x {
			return mid
		} else if mid * mid < x {
			low = mid + 1
		} else {
			high = mid - 1
		}
	}
	return high
}

func main() {
    num := 8
    result := mySqrt(num)
    fmt.Println(result)
}
