/*
Array Statistics Program
Calculates sum, average, minimum, and maximum of an array.
*/

#include <stdio.h>

int main() {
    int n, i;
    int arr[100];
    int sum = 0, min, max;

    printf("Enter number of elements: ");
    scanf("%d", &n);

    printf("Enter %d elements:\n", n);
    for (i = 0; i < n; i++) {
        scanf("%d", &arr[i]);
        sum += arr[i];
    }

    min = max = arr[0];
    for (i = 1; i < n; i++) {
        if (arr[i] < min) min = arr[i];
        if (arr[i] > max) max = arr[i];
    }

    printf("Sum = %d\n", sum);
    printf("Average = %.2f\n", (float)sum / n);
    printf("Minimum = %d\n", min);
    printf("Maximum = %d\n", max);

    return 0;
}
