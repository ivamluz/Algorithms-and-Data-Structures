# Mini-Max Sum

Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers. Then return a tuple containing the respective minimum and maximum values.

For example, ```arr = [1, 3, 5, 7, 9]```. Our minimum sum is ```1 + 3 + 5 + 7 = 16``` and our maximum sum is ```3 + 5 + 7 + 9 = 24```. We would return
```python
(16, 24)
```

**Source:** [HackerRank](https://www.hackerrank.com/challenges/mini-max-sum/problem)

## Function Description

Write a function that receives an array of integers with 5 elements and returns a tuple containing the minimum sum and the maximum sum of ```4``` of ```5``` elements.

## Input Format

An array of ```5``` integers:
```python
arr = [1, 2, 3, 4, 5]
```

## Constraints
```1 <= arr[i] <= 10^9```

## Output Format

Return a tuple containing the respective minimum and maximum values that can be calculated by summing exactly four of the five integers. (The values can be greater than 32 bit integers.)

## Sample Input
```
[1, 2, 3, 4, 5]
```

## Sample Output
```
(10, 14)
```

## Explanation

Our initial numbers are ```1, 2, 3, 4, and 5```. We can calculate the following sums using four of the five integers:

If we sum everything except 1, our sum is ```2 + 3 + 4 + 5 = 14```.
If we sum everything except 2, our sum is ```1 + 3 + 4 + 5 = 13```.
If we sum everything except 3, our sum is ```1 + 2 + 4 + 5 = 12```.
If we sum everything except 4, our sum is ```1 + 2 + 3 + 5 = 11```.
If we sum everything except 5, our sum is ```1 + 2 + 3 + 4 = 10```.