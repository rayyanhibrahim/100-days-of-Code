# Container With Most Water

def max_area(height):
    left = 0
    right = len(height) - 1
    max_water = 0

    while left < right:
        width = right - left
        current_height = min(height[left], height[right])
        area = width * current_height

        max_water = max(max_water, area)

        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return max_water


# User input
height = list(map(int, input("Enter heights separated by spaces: ").split()))

print("Maximum water that can be contained:", max_area(height))


#Enter heights separated by spaces: 1 8 6 2 5 4 8 3 7
Maximum water that can be contained: 49
