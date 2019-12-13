package main

import (
	"log"
	"io/ioutil"
	"strconv"
	"strings"
)

const (
	HALT =			99
	ADD =			1
	MULTIPLY =		2
	INPUT_FILE_PATH =	"./input.txt"
)

func main(){
	log.Println(process(input()))
	log.Println(part2())
}

func part2() int{
	for i := 0; i < 99; i++ {
		for j := 0; j < 99; j++ {
			arr := input()
			arr[1] = i
			arr[2] = j
			if process(arr) == 19690720 {
				return 100 * i + j
			}
		}
	}
	return 0
}

func process(arr []int) int {
	for i := 0; i < len(arr); i+=4 {
		if arr[i] == HALT {
			break
		}

		opcode := arr[i]
		a := arr[arr[i+1]]
		b := arr[arr[i+2]]
		dest := arr[i+3]
		var val int

		if opcode == ADD {
			val = a + b
		}
		if opcode == MULTIPLY {
			val = a * b
		}

		arr[dest] = val
	}

	return arr[0]
}

func input() []int {
	arr := make([]int, 0)

	data, err := ioutil.ReadFile(INPUT_FILE_PATH)
	if err != nil {
		log.Fatal(err)
	}


	strArr := strings.Split(strings.TrimSpace(string(data)), ",")
	for i := range strArr {
		num, err := strconv.Atoi(strArr[i])
		if err != nil {
			log.Fatal(err)
		}

		arr = append(arr, num)
	}

	arr[1] = 12
	arr[2] = 2
	return arr
}

