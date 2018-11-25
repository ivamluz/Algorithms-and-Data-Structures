# Diagonal Difference

Given a square matrix, calculate the absolute difference between the sums of its diagonals.

For example, the square matrix  is shown below:

```
1 2 3
4 5 6
9 8 9
```  

The left-to-right diagonal = ```1 + 5 + 9 = 15```. The right to left diagonal = ```3 + 5 + 9 = 17```. Their absolute difference is ```|15 - 17| = 2```.

**Source:** [HackerRank](https://www.hackerrank.com/challenges/diagonal-difference/problem)

## Function description

Write a function that receives a squared matrix and return an integer representing the absolute diagonal difference.


## Sample Input
```python
[
  [11, 2,   4],
  [4,  5,   6],
  [10, 8, -12]
]
```

## Sample Output
```python
15
```

## Explanation

The primary diagonal is:
```
11
   5
     -12
````

Sum across the primary diagonal: 11 + 5 - 12 = 4

The secondary diagonal is:
```
     4
   5
10
````

Sum across the secondary diagonal: 4 + 5 + 10 = 19 

**Difference:** |4 - 19| = 15

Note: |x| is the [absolute value](https://www.mathsisfun.com/numbers/absolute-value.html) of x