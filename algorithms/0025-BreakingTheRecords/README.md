# Breaking the Records

Maria plays college basketball and wants to go pro. Each season she maintains a record of her play. She tabulates the number of times she breaks her season record for most points and least points in a game. Points scored in the first game establish her record for the season, and she begins counting from there.

For example, assume her scores for the season are represented in the array ```scores = [12, 24, 10, 24]```. Scores are in the same order as the games played. She would tabulate her results as follows:

| Game   | Score  | Minimum | Maximum | Min | Max |
| -----: |-------:| -------:| ------: | --: | --: |
| 0      | 12     | 12      | 12      | 0   | 0   |
| 1      | 24     | 12      | 24      | 0   | 1   |
| 2      | 10     | 10      | 24      | 1   | 1   |
| 3      | 24     | 10      | 24      | 1   | 1   |

Given Maria's scores for a season, find and print the number of times she breaks her records for most and least points scored during the season.

## Function Description

Implement the ```breakingRecords``` function. It must return a tuple containing the numbers of times she broke her records. Index ```0``` is for breaking most points records, and index ```1``` is for breaking least points records.

```breakingRecords``` has the following parameter(s):
* **scores:** an array of integers

## Constraints
```
1 <= n <= 1000
0 <= scores[i] <= 10^8
```

## Sample Input and Output 0
```python
breakingRecords([10, 5, 20, 20, 4, 5, 2, 25, 1])
# output: (2, 4)
```

## Explanation 0

The table below depicts the number of times Maria broke her best and worst records throughout the season:

| Game              | 0  | 1     | 2      | 3  | 4     | 5  | 6     | 7      | 8     |
| ----------------: |---:|------:|-------:|---:|------:|---:|------:|-------:|------:|
| **Score**         | 10 | 5     | 20     | 20 | 4     | 5  | 2     | 25     | 1     |
| **Highest Score** | 10 | 10    | **20** | 20 | 20    | 20 | 20    | **25** | 25    |
| **Lowest Score**  | 10 | **5** | 5      | 5  | **4** | 4  | **2** | 2      | **1** |

She broke her best record twice (after games ```2``` and ```7```) and her worst record four times (after games ```1```, ```4```, ```6```, and ```8```), so we return ```(2, 4)``` as our answer. Note that she did not break her record for best score during game ```3```, as her score during that game was not strictly greater than her best record at the time.

## Sample Input and Output 1
```python
breakingRecords([3, 4, 21, 36, 10, 28, 35, 5, 24, 42])
# output: (4, 0)
```

## Explanation 1

The table below depicts the number of times Maria broke her best and worst records throughout the season:

| Game              | 0  | 1     | 2      | 3      | 4  | 5  | 6  | 7  | 8  | 9      |
| ----------------: |---:|------:|-------:|-------:|---:|---:|---:|---:|---:|-------:|
| **Score**         | 3  | 4     | 21     | 36     | 10 | 28 | 35 | 5  | 24 | 42     |
| **Highest Score** | 3  | **4** | **21** | **36** | 36 | 36 | 36 | 36 | 36 | **42** |
| **Lowest Score**  | 3  | 3     | 3      | 3      | 3  | 3  | 3  | 3  | 3  | 3      |   

She broke her best record four times (after games ```1```, ```2```, ```3```, and ```9```) and her worst record zero times (no score during the season was lower than the one she earned during her first game), so we return ```(4, 0)``` as our answer.