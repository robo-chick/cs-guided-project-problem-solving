"""
Challenge #1:

Write a function that retrieves the last n elements from a list.


Examples:
- last([1, 2, 3, 4, 5], 1) ➞ [5]
- last([4, 3, 9, 9, 7, 6], 3) ➞ [9, 7, 6]
- last([1, 2, 3, 4, 5], 7) ➞ "invalid"
- last([1, 2, 3, 4, 5], 0) ➞ []

Notes:
- Return "invalid" if n exceeds the length of the list.
- Return an empty list if n == 0.

UPER
Understand
: inputs
-list of nums
- number of items from end of list
outputs: 
- list or 'invalid'
consider edge cases:
- if 'invalid', or edge case, wasn't given to you, what is a good question to ask? 
- what if n is larger than the list?
- what if n is 0? return nothing []

Plan
- pseudo code
- plain English
- how do we handle edge cases? 
 - invalid if n > len of list
 - [] if n = 0
- how to do main problem?
 - get last n elements of list
    - or get all elements starting at len - n
    - slice
    - arr[len(arr) -n : ]
"""


def last(arr, n):
    #edge cases
    if n > len(arr):
        return "invalid"
    elif n == 0:
        return []
    # main solution
    return arr[len(arr) - n : ]

print(last([1, 2, 3, 4, 5], 1))
print(last([4, 3, 9, 9, 7, 6], 3))
print(last([1, 2, 3, 4, 5], 7)) # invalid
print(last([1, 2, 3, 4, 5], 0)) # []