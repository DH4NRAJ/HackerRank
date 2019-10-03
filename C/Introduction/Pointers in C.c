//Pointers in C
#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<math.h>
void update(int *a,int *b) //dynamic allocation
{
    int temp;
    temp=*a;
    *a=abs(*a+*b);
    *b=abs(temp-*b);
}
int main() {
    int a, b;
    scanf("%d %d", &a, &b);
    update(&a, &b);
    printf("%d\n%d", a, b);
    return 0;
}


