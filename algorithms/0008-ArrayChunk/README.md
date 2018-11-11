# Array chunk

Create a function that receives an array as input (first argument) and split it into smaller chunks of arrays with the length provided by size (second argument).

## Examples

1. `(['a', 'b', 'c', 'd'], 2)` is expected to be `[['a', 'b'], ['c', 'd']]`
2. `([0, 1, 2, 3, 4, 5], 3)` is expected to be `[[0, 1, 2], [3, 4, 5]]`
3. `([0, 1, 2, 3, 4, 5], 2)` is expected to be `[[0, 1], [2, 3], [4, 5]]`
4. `([0, 1, 2, 3, 4, 5], 4)` is expected to be `[[0, 1, 2, 3], [4, 5]]`
5. `None` is expected to be `[]`
6. `[]`is expected to be `[]`