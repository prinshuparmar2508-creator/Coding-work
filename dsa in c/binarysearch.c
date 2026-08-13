#include <stdio.h>

int main(){
    int N = 20, arr[N];
    for(int i = 0; i < N; i++) arr[i] = i+1;
    int middle, target, start = 0, end = N-1;
    printf("Enter number to search: ");
    scanf("%d", &target);
    while(start <= end){
        middle = (start+end)/2;
        if(arr[middle] == target){
            printf("%d found at index %d\n", target, middle);
            return 0;
        }
        else if(arr[middle] > target)   end = middle-1;
        else    start = middle+1;
    }
    printf("%d not found in array containing 1-20.\n", target);

    return 0;
}