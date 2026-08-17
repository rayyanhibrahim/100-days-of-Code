# 3Sum - Find all unique triplets whose sum is zero

def three_sum(nums):
    nums.sort()
    result = []

    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        left = i + 1
        right = len(nums) - 1

        while left < right:
            total = nums[i] + nums[left] + nums[right]

            if total == 0:
                result.append([nums[i], nums[left], nums[right]])

                while left < right and nums[left] == nums[left + 1]:
                    left += 1

                while left < right and nums[right] == nums[right - 1]:
                    right -= 1

                left += 1
                right -= 1

            elif total < 0:
                left += 1
            else:
                right -= 1

    return result


# User input
nums = list(map(int, input("Enter numbers separated by spaces: ").split()))

triplets = three_sum(nums)

if triplets:
    print("Triplets with sum 0:")
    for triplet in triplets:
        print(triplet)
else:
    print("No triplets found.")

#Enter numbers separated by spaces: -1 0 1 2 -1 -4
Triplets with sum 0:
[-1, -1, 2]
[-1, 0, 1]
