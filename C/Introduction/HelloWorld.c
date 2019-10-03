//helloworldprogram
#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<math.h>
int main()
{
    char c[50];       //in C string is a array of character
    scanf("%[^\n]%*c", &c); //taking string input && considering white_space
    printf("Hello, World!\n%s",c);
}
