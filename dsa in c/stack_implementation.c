#include <stdio.h>
#include <string.h>
int main(){
    int N = 7, arr[N], top = -1, number;
    printf("we have a stack with max capacity of 7 elements\n");
    char operation[5];
    while(1){
        printf("Enter operation to perform: ");
        scanf("%4s",operation);
        if(strcmp(operation,"push") == 0 || strcmp(operation, "p") == 0){
            if(top == N-1){
                printf("stack overflow\n");
                continue;
            }
            printf("Enter number: ");
            scanf("%d",&number);
            arr[++top] = number;
            printf("stack: ");
            for(int i = 0;i <=top; i++)printf("%d", arr[i]);
            printf("\n");
        }
        else if(strcmp(operation, "pop") == 0 || strcmp(operation,"0") == 0){
            if(top == -1){
                printf("stack underflow\n");
                continue;
            }
            top--;
            printf("stack: ");
            for(int i = 0; i <= top; i++) printf("%d", arr[i]);
            printf("\n");
        }
        else if(strcmp(operation, "quit") == 0 || strcmp(operation, "q") == 0) return 0;
        else printf("invalid input\n");
    }
    return 0;
}