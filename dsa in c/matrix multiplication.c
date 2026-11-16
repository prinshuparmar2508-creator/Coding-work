#include <stdio.h>

int main()
{
    int m, n, p, q, c, d, k, sum;
    int first[10][10], second[10][10], multiply[10][10];

    printf("Enter number of rows and columns of first matrix: ");
    scanf("%d%d", &m, &n);

    printf("Enter elements of first matrix:\n");
    for (c = 0; c < m; c++)
        for (d = 0; d < n; d++)
            scanf("%d", &first[c][d]);

    printf("Enter number of rows and columns of second matrix: ");
    scanf("%d%d", &p, &q);

    if (n != p)
    {
        printf("The multiplication isn't possible.\n");
        return 0;
    }

    printf("Enter elements of second matrix:\n");
    for (c = 0; c < p; c++)
        for (d = 0; d < q; d++)
            scanf("%d", &second[c][d]);

    for (c = 0; c < m; c++)
    {
        for (d = 0; d < q; d++)
        {
            sum = 0;

            for (k = 0; k < n; k++)
            {
                sum += first[c][k] * second[k][d];
            }

            multiply[c][d] = sum;
        }
    }

    printf("\nProduct of the matrices:\n");

    for (c = 0; c < m; c++)
    {
        for (d = 0; d < q; d++)
            printf("%d\t", multiply[c][d]);

        printf("\n");
    }

    return 0;
}