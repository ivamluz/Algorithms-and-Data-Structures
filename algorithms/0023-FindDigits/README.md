# Find Digits

An integer ```d``` is a divisor of an integer ```n``` if the remainder of ```n / d = 0```.

Given an integer, for each digit that makes up the integer determine whether it is a divisor. Count the number of divisors occurring within the integer.

**Note:** Each digit is considered to be unique, so each occurrence of the same digit should be counted (e.g. for ```n = 111```, ```1``` is a divisor of ```111``` each time it occurs so the answer is ```3```).

# Function Description

Write a function ```findDigits(number)``` that receives an integer containing the number to be analyzed and returns another integer representing the number of digits of ```number``` that are divisors of ```number```.

```findDigits``` has the following parameter(s):

* **n:** an integer to analyze

# Constraints
```
0 < n < 10^9
```
 
# Output Format

Return an integer representing the number of digits of ```number``` that are divisors of ```number```.

# Sample Input and output
```python
findDigits(12)
# output: 2

findDigits(1012)
# output: 3
```


# Explanation

The number ```12``` is broken into two digits, ```1``` and ```2```. When ```12``` is divided by either of those two digits, the remainder is ```0``` so they are both divisors.

The number ```1012``` is broken into four digits, ```1```, ```0```, ```1```, and ```2```. ```1012``` is evenly divisible by its digits ```1```, ```1```, and ```2```, but it is not divisible by ```0``` as division by zero is undefined.