#include <stdio.h>
int main()
{
    int a[10],i,item,flag=0;
    printf("\n enter 10 elements of array: ");
    for(i=0;i<10;i++)
    {
        scanf("%d",&a[i]);
    }
    printf("\n array elements are: ");
    for(i=0;i<10;i++)
    {
        printf("\n%d",a[i]);
    }
}