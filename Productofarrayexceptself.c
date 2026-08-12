#include <stdio.h>

void productExceptSelf(int* nums, int numsSize, int* answer) {
    int prefix = 1;

    for (int i = 0; i < numsSize; i++) {
        answer[i] = prefix;
        prefix *= nums[i];
    }

    int suffix = 1;

    for (int i = numsSize - 1; i >= 0; i--) {
        answer[i] *= suffix;
        suffix *= nums[i];
    }
}

int main() {
    int nums[] = {1, 2, 3, 4};
    int n = 4;
    int answer[4];

    productExceptSelf(nums, n, answer);

    printf("Output: [");
    for (int i = 0; i < n; i++) {
        printf("%d", answer[i]);
        if (i < n - 1)
            printf(", ");
    }
    printf("]\n");

    return 0;
}
#output
#Output: [24, 12, 8, 6]
