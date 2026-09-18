#include<stdio.h>
int partition(int a[], int start, int end)
{
    int pivot = a[end];
    int i = (start - 1);
    for (int j = start; j <= end - 1; j++)
    {
        // if current element is smaller than pivot
        if (a[j]<pivot)
        {
            i++;// increment index of smaller element
            int t = a[i];
            a[i] = a[j];
            a[j] = t;
        }
    }
    int t = a[i + 1];
    a[i +  1] = a[end];
    a[end] = t;
    return (i + 1);
}
/* function to implement quick sort*/
void quick(int a[],int start,int end)
/*a[]= array to be sorted, start = starting index, end = ending index*/
{
    if (start < end)
    {
        int p = partition(a, start, end);
        // p is partitioning index
        quick(a, start, p-1);
        quick(a, p + 1, end);

    }
}
/* function to implement quick sort*/
void printArr(int a[], int n)
{
    int i;
    for(i = 0; i < n; i++)
    {
        printf("%d\n ", a[i]);
    }
}
int main()
{
    int a[] = { 10, 7 , 8 , 9, 1, 5};
    int n = sizeof(a) / sizeof(a[0]);
    printf("Before sorting array elementsare -\n");
    printArr(a,n);
    quick(a,0,n-1);
    printf("After sorting array elements are -\n");
    printArr(a, n);
    return 0;
}