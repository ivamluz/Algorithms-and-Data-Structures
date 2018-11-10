# Maximum occurring character

**Objective:** Given a string, write an algorithm to find the character in string which occurs maximum number of times. If more than one character has maximum and same count then print all of them

## Examples:
```python
# Single most occurring char
max_chars("tutorial horizon")
# output: 
{
  "o": 3
}
```

```python
# Multiple most occurring chars
max_chars("abcabcdefabcab")
# output:
{
  "a": 4,
  "b": 4
}
```

```python
# Empty string
max_chars("")
# output:
None
```

For more examples, see the [unit tests](#).