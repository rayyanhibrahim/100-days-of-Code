# Minimum Window Substring

from collections import Counter


def minimum_window(s, t):
    if not s or not t:
        return ""

    required = Counter(t)
    window = {}

    left = 0
    formed = 0
    required_count = len(required)

    min_length = float("inf")
    min_start = 0

    for right in range(len(s)):
        char = s[right]
        window[char] = window.get(char, 0) + 1

        if char in required and window[char] == required[char]:
            formed += 1

        while formed == required_count:
            current_length = right - left + 1

            if current_length < min_length:
                min_length = current_length
                min_start = left

            left_char = s[left]
            window[left_char] -= 1

            if left_char in required and window[left_char] < required[left_char]:
                formed -= 1

            left += 1

    if min_length == float("inf"):
        return ""

    return s[min_start:min_start + min_length]


# User input
s = input("Enter the main string: ")
t = input("Enter the target string: ")

result = minimum_window(s, t)

if result:
    print("Minimum window substring:", result)
else:
    print("No valid window found.")

# Enter the main string: ADOBECODEBANC
Enter the target string: ABC
Minimum window substring: BANC
