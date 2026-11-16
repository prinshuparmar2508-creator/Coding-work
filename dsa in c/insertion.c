#include <stdio.h>
 int main()
{
    int arr[20] = { 0 };
    int i, x, pos, n;
 	printf("\n Enter total no. of elements");
 	scanf("%d",&n);
 	if (n>20) printf("\n Array size cannot exceed 20");
    printf("\n Enter elements of an array");
    for (i = 0; i < n; i++)
        scanf("%d", &arr[i]);
    printf("\n Enter Data and Index");
 	scanf("%d%d",&x,&pos);
    n++;				// increase the size by 1
    for (i = n-1; i >= pos; i--)		// shift elements forward
        arr[i] = arr[i - 1];
     // insert x at pos
    arr[pos - 1] = x;
     // print the updated array
    for (i = 0; i < n; i++)
        printf("\n%d ", arr[i]);
    return 0;
}
