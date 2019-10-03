//Functions in C
#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<math.h>
int max_of_four(int a,int b,int c,int d);
int main()
{
    int a,b,c,d,max;
    scanf("%d%d%d%d",&a,&b,&c,&d);
    max=max_of_four(a,b,c,d);
    printf("%d",max);
}
int max_of_four(int a,int b,int c,int d)
{
    int max;
    // Find the greater number in a or b.
    max = (a > b? a : b);
    /* Find the greater number in c and d, and compare to the previously
       found maximum in a and b. */
    max = (c > d? (c > max? c : max) : (d > max? d : max));
    return max;
}
