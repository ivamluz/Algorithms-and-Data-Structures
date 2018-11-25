# Knapsack

Given an array of integers and a target sum, determine the sum nearest to but not exceeding the target that can be created. To create the sum, use any element of your array zero or more times.

For example, if ```values = [2, 3, 4]``` and your target sum is ```10```, you might select ```[2, 2, 2, 2, 2]``` or ```[2, 2, 3, 3]```. In this case, you can arrive at exactly the target.

## Function Description

Create a function that receives an integer representing the target sum and a list of integers to calculate (and return) the nearest sum from.

## Input Format

```python
unboundedKnapsack(targetSum, values)
```

**targetSum:** an int representing the maximum sum expected.

**values:** a list of ints to calculate the nearest sum from.

## Constraints
```
1 <= t <= 10
1 <= n, k, arr[i] <= 200
```

## Output Format

An **int** representing the maximum sum which is as near as possible, but not exceeding, the target sum.

## Sample Input
```python
unboundedKnapsack(12, [1, 6, 9])
unboundedKnapsack(10, [3, 8])
```

## Sample Output
```python
12
9
```

## Explanation

In the first test case, one can pick [6, 6]. In the second, we can pick [3,3,3].