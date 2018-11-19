# Plus Minus

Given an array of integers, calculate the fractions of its elements that are positive, negative, and are zeros. Return an array containing the decimal value of each fraction.

**Note:** This challenge introduces precision problems. The test cases are scaled to six decimal places, though answers with absolute error of up to 10 ^ -4 are acceptable.

For example, given the array ```arr = [1, 1, 0, -1, -1]``` there are  elements, two positive, two negative and one zero. Their ratios would be ```2/5 = 0.400000, 2/5 = 0.400000 and 1/5 = 0.200000```. It should return the following array:

```python
[
  0.400000, # Index 0 contains the ration of negative numbers
  0.400000, # Index 1 contains the ratio of zeros
  0.200000  # Index 2 contains the ratio of positive numbers
]
```

## Sample Input
```python
[-4, 3, -9, 0, 4, 1]
```

## Sample Output
```python
[
  0.500000,
  0.333333,
  0.166667
]
```

## Explanation

There are 3 positive numbers, 2 negative numbers, and 1 zero in the array. 
The proportions of occurrence are ```positive: 3/6 = 0.500000, negative: 2/6 = 0.333333 and zeros: 1/6 = 0.166667```.