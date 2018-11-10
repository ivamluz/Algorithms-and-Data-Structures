# Maximum occurring character

**Objective:** Given a string, write an algorithm to find the character in string which occurs maximum number of times. If more than one character has maximum and same count then return all of them.

## Examples:
```python
# Single most occurring char
max_occurring_chars("tutorial horizon")
# output: 
{
  "o": 3
}
```

```python
# Multiple most occurring chars
max_occurring_chars("abcabcdefabcab")
# output:
{
  "a": 4,
  "b": 4
}
```

```python
# Empty string
max_occurring_chars("")
# output:
None
```

For more examples, see the [unit tests](https://github.com/ivamluz/Algorithms-and-Data-Structures/blob/master/algorithms/0007-MaxOccurringChar/test_max_occurring_chars.py).