#include <stdio.h>

void merge(int intervals[][2], int n) {
    // Sort intervals by starting time
    for (int i = 0; i < n - 1; i++) {
        for (int j = 0; j < n - i - 1; j++) {
            if (intervals[j][0] > intervals[j + 1][0]) {
                int temp0 = intervals[j][0];
                int temp1 = intervals[j][1];

                intervals[j][0] = intervals[j + 1][0];
                intervals[j][1] = intervals[j + 1][1];

                intervals[j + 1][0] = temp0;
                intervals[j + 1][1] = temp1;
            }
        }
    }

    int index = 0;

    for (int i = 1; i < n; i++) {
        if (intervals[index][1] >= intervals[i][0]) {
            if (intervals[i][1] > intervals[index][1])
                intervals[index][1] = intervals[i][1];
        } else {
            index++;
            intervals[index][0] = intervals[i][0];
            intervals[index][1] = intervals[i][1];
        }
    }

    printf("Merged Intervals:\n");

    for (int i = 0; i <= index; i++) {
        printf("[%d, %d]", intervals[i][0], intervals[i][1]);

        if (i < index)
            printf(", ");
    }

    printf("\n");
}

int main() {
    int intervals[][2] = {
        {1, 3},
        {2, 6},
        {8, 10},
        {15, 18}
    };

    int n = sizeof(intervals) / sizeof(intervals[0]);

    merge(intervals, n);

    return 0;
}
#output
Merged Intervals:
[1, 6], [8, 10], [15, 18]
