# Between Two Sets

You will be given two arrays of integers and asked to determine all integers that satisfy the following two conditions:

1. The elements of the first array are all factors of the integer being considered
2. The integer being considered is a factor of all elements of the second array

These numbers are referred to as being between the two arrays. You must determine how many such numbers exist.

For example, given the arrays ```a = [2, 6]``` and ```b = [24, 36]```, there are two numbers between them: ```6``` and ```12```. ```6 % 2 = 0```, ```6 % 6```, ```24 % 6 = 0``` and ```36 % 6 = 0``` for the first value. Similarly, ```12 % 2 = 0```, ```12 % 6 = 0``` and ```24 % 12 = 0```, ```36 % 12 = 0```.

## Function Description```

Implement the ```getTotalX``` function. It should return the number of integers that are betwen the sets.

getTotalX has the following parameter(s):

* **a:** an array of integers
* **b:** an array of integers

## Constraints
```
1 < n, m < 10
1 < a[i] < 100
1 < b[j] < 100
```

## Output Format

Return an integer representing the number of integers that are considered to be between ```a``` and ```b```.

## Sample Input and Output
```python
getTotalX([2, 4], [16, 32, 96])
# output: 3
```

## Explanation

2 and 4 divide evenly into 4, 8, 12 and 16. 
4, 8 and 16 divide evenly into 16, 32, 96.

4, 8 and 16 are the only three numbers for which each element of a is a factor and each is a factor of all elements of b.