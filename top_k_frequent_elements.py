from collections import Counter
import heapq


def top_k_frequent(nums, k):
    # Count the frequency of each element
    frequency = Counter(nums)

    # Get the k most frequent elements
    return [num for num, count in frequency.most_common(k)]


# Example
nums = [1, 1, 1, 2, 2, 3]
k = 2

result = top_k_frequent(nums, k)

print("Input:", nums)
print("K:", k)
print("Top K Frequent Elements:", result)

#Input: [1, 1, 1, 2, 2, 3]
K: 2
Top K Frequent Elements: [1, 2]
