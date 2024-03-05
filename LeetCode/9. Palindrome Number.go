package main

import "fmt"

func isPalindrome(x int) bool {
	s := fmt.Sprintf("%d", x)
	o := []rune(s)
    i := len(o);
    for _, c := range s {
        i--;
        o[i] = c;
    }
	return s == string(o)
}

func main() {
    num := 11211
    result := isPalindrome(num)
    fmt.Println(result)
}
