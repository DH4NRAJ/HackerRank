//Playing With Characters
#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<math.h>
int main()
{
    char ch,s[50],sen[100];
    scanf("%c",&ch);
    fflush(stdin); //to clear input queue
    scanf("%s",&s); //takes string value
    scanf("\n");
    fflush(stdin);
    gets(sen);
    printf("%c\n",ch);
    printf("%s\n",s);
    printf("%s",sen);
    return 0;

}
