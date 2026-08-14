#include <stdio.h>
int main(){
    int N = 20, arr[N], target;
    printf("Enter %d numbers: ", N);
    for(int i = 0; i < N; i++) scanf("%d", &arr[i]);
    printf("Enter number to find: ");
    scanf("%d", &target);
    for(int j = 0; j < N; j++){
        if(arr[j] == target){
            printf("%d found at index %d.\n", target, j);
            return 0;
        }
    }
    printf("%d not found in given array.\n", target);

    return 0;
}
