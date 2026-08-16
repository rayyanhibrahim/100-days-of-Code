def is_palindrome(s):
    # Keep only alphanumeric characters and convert to lowercase
    cleaned = ''.join(char.lower() for char in s if char.isalnum())

    # Check if the string is equal to its reverse
    return cleaned == cleaned[::-1]


# Example
s = "A man, a plan, a canal: Panama"

result = is_palindrome(s)

print("Input:", s)
print("Valid Palindrome:", result)

#output
Input: A man, a plan, a canal: Panama
Valid Palindrome: True
