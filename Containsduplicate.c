#include <stdbool.h>

bool containsDuplicate(int* nums, int numsSize) {
    for (int i = 0; i < numsSize - 1; i++) {
        for (int j = i + 1; j < numsSize; j++) {
            if (nums[i] == nums[j]) {
                return true;
            }
        }
    }

    return false;
}

## Output

Example 1:
Input: [1, 2, 3, 1]
Output: true

Example 2:
Input: [1, 2, 3, 4]
Output: false

Example 3:
Input: [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
Output: true
