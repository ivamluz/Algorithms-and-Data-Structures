# Birthday Chocolate

Lily has a chocolate bar that she wants to share it with Ron for his birthday. Each of the squares has an integer on it. She decides to share a contiguous segment of the bar selected such that the length of the segment matches Ron's birth month and the sum of the integers on the squares is equal to his birth day. You must determine how many ways she can divide the chocolate.

Consider the chocolate bar as an array of squares, ```s = [2, 2, 1, 3, 2]```. She wants to find segments summing to Ron's birth day, ```d = 4``` with a length equalling his birth month, ```m = 2```. In this case, there are two segments meeting her criteria: ```[2, 2]``` and ```[1, 3]```.

## Function Description

Write the ```birthday``` function. It should return an integer denoting the number of ways Lily can divide the chocolate bar.

```birthday``` has the following parameter(s):

* **numbers:** an array of integers, the numbers on each of the squares of chocolate
* **day:** an integer, Ron's birth day
* **month:** an integer, Ron's birth month

## Constraints
```
1 <= numbers[i] <= 5
1 <= day <= 31
1 <= month <= 12
```

## Output Format

Return an integer denoting the total number of ways that Lily can portion her chocolate bar to share with Ron.

## Sample Input and Output 0
```python
birthday(numbers = [1, 2, 1, 3, 2], day = 3, month = 2)
# output: 2
```

## Explanation 0

Lily wants to give Ron ```month = 2``` squares summing to ```day = 3```. The following two segments meet the criteria:


|<----|---->|     |     |     |
|:---:|:---:|:---:|:---:|:---:|
|**1**|**2**|**1**|  3  |  2  |
|     |<----|---->|     |     |
```
1 + 2 = 3
2 + 1 = 3
```

## Sample Input and Output 1
```python
birthday(numbers = [1, 1, 1, 1, 1, 1], day = 3, month = 2)
# output: 0
```

## Explanation 1

Lily only wants to give Ron ```month = 2``` consecutive squares of chocolate whose integers sum to ```day = 3```. There are no possible pieces satisfying these constraints:

|     |     |     |     |     |     |
|:---:|:---:|:---:|:---:|:---:|:---:|
|  1  |  1  |  1  |  1  |  1  |  1  |
|     |     |     |     |     |     |

Thus, we return ```0``` as our answer.

## Sample Input and output 2
```python
birthday(numbers = [4], day = 4, month = 1)
# output: 1
```

## Explanation 2

Lily only wants to give Ron ```month = 1``` square of chocolate with an integer value of ```day = 4```. Because the only square of chocolate in the bar satisfies this constraint, we return ```1``` as our answer.