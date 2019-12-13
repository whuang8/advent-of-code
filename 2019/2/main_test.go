package main

import (
	"testing"
	"github.com/stretchr/testify/assert"
)

var processTests = []struct{
	name		string
	input		[]int
	expected	int
}{
	{
		name: "test_1",
		input: []int{1,9,10,3,2,3,11,0,99,30,40,50},
		expected: 3500,
	},
	{
		name: "test_2",
		input: []int{1,0,0,0,99},
		expected: 2,
	},
	{
		name: "test_3",
		input: []int{2,3,0,3,99},
		expected: 2,
	},
	{
		name: "test_4",
		input: []int{1,1,1,4,99,5,6,0,99},
		expected: 30,
	},
}

func TestProcess(t *testing.T) {
	for _, test := range processTests {
		t.Run(test.name, func(t *testing.T){
			actual := process(test.input)
			assert.Equal(t, test.expected, actual)
		})
	}
}
