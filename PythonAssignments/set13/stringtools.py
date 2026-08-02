__all__ = [
    "reverse",
    "is_palindrome",
    "count_vowels",
    "title_case",
    "remove_spaces"
]

def _clean(s):
    return s.lower().replace(" ", "")

def reverse(s):
    return s[::-1]

def is_palindrome(s):
    s = _clean(s)
    return s == s[::-1]

def count_vowels(s):
    count = 0
    vowels = "aeiouAEIOU"
    for ch in s:
        if ch in vowels:
            count += 1
    return count

def title_case(s):
    return s.title()

def remove_spaces(s):
    return s.replace(" ", "")