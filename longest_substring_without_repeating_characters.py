# Longest Substring Without Repeating Characters

def longest_substring(s):
    char_index = {}
    left = 0
    max_length = 0
    longest = ""

    for right in range(len(s)):
        char = s[right]

        if char in char_index and char_index[char] >= left:
            left = char_index[char] + 1

        char_index[char] = right

        current_length = right - left + 1

        if current_length > max_length:
            max_length = current_length
            longest = s[left:right + 1]

    return longest, max_length


# User input
s = input("Enter a string: ")

substring, length = longest_substring(s)

print("Longest substring:", substring)
print("Length:", length)

# Enter a string: abcabcbb
Longest substring: abc
Length: 3
