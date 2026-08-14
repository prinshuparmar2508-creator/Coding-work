#include <stdio.h>
int main(){
    int N = 20, arr[N], target;
    printf("Enter %d numbers: ", N);
    for(int i = 0; i < N; i++) scanf("%d", &arr[i]);
    printf("Enter number to find: ");
    scanf("%d", &target);
    int low = 0, high = N - 1;
    while(low <= high){
        int mid = (low + high) / 2;
        if(arr[mid] == target){
            printf("%d found at index %d.\n", target, mid);
            return 0;
        }
    }
    printf("%d not found in given array.\n", target);

    return 0;
