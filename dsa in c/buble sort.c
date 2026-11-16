#include<stdio.h>
void swap(int *x, int *y){
    int temp = *x;
    *x = *y;
    *y = temp;
}

int main(){
    int length = 8, arr[length];
    printf("Enter elements to sort: ");
    for(int *i = arr; i < arr+length;i++) scanf("%d", i);

    for(int a = 0; a < length-1; a++)
        for(int b = 0; b < length-a-1; b++)
            if(arr[b] > arr[b+1])
                swap(&arr[b], &arr[b+1]);

    for(int *i = arr; i < arr+length; i++) printf("%d ", *i);
    return 0;
} 