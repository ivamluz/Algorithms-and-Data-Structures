# Anagrams

Two strings are said to be **anagrams** of one another if you can turn the first string into
the second by rearranging its letters. For example, “table” and “bleat” are anagrams, as
are “tear” and “rate.” Your job is to write a function that takes in two strings as input and
determines whether they're anagrams of one another.

Source: [Stanford](https://web.stanford.edu/class/cs9/sample_probs/Anagrams.pdf)

## Things to keep in mind

### Do we need to worry about case­ sensitivity? Or, are the inputs guaranteed to be in lower­case?
Inputs aren't guaranteed to be in lowercase. The algorithm should take care of this cases. Ex: 
```
OpuS <=> sOup => True
````

### Do the strings just consist of letters, or can they have other characters in them?
Assume they're just letters.

### Are the strings necessarily the same length?
No, they can be different lengths.

### Is a string an anagram of itself?
Yes.

### Are all the letters from the English alphabet? 
Yes.

### May any of the strigs be empty? Or both be empty?
Yes, and in either case they shouldn't be considered anagrams of each other.

### May any of the strings be None? Or both None?
Yes, and in either case they shouldn't be considered anagrams of each other.

Examples:
```python
is_anagram('Heart', 'Earth') # True
```

```python
is_anagram('Era', 'Area') # False
```

```python
is_anagram('Area', 'area') # True
```

```python
is_anagram('Heart', '') # False
is_anagram('', 'Heart') # False
is_anagram('', '') # False
```

```python
is_anagram('Heart', None) # False
is_anagram(None, 'Heart') # False
is_anagram(None, None) # False
```