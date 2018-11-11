# Array chunk

Create a function that receives an array as input (first argument) and split it into smaller chunks of arrays with the length provided by size (second argument).

## Examples

```python
chunk(['a', 'b', 'c', 'd'], 2)
# output
[['a', 'b'], ['c', 'd']]
```

```python
chunk([0, 1, 2, 3, 4, 5], 3)
# output
[[0, 1, 2], [3, 4, 5]]
```

```python
chunk([0, 1, 2, 3, 4, 5], 2)
# output
[[0, 1], [2, 3], [4, 5]]
```

```python
chunk([0, 1, 2, 3, 4, 5], 4)
# output
[[0, 1, 2, 3], [4, 5]]
```

```python
chunk(None)
# output
[]
```

```python
chunk([])
# output
[]
```