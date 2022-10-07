"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    items2 = []
    items = list(map(str, items))
    # Your code goes here
    for item in items:
        if item not in items2:
            items2.append(item)
    for item in items2:
        if item in items:
            frequencies[item] = items.count(item)
    return frequencies
