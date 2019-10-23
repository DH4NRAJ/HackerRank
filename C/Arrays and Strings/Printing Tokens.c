#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int main() {

    char *s;
    s = malloc(1024 * sizeof(char));
    scanf("%[^\n]", s);
    s = realloc(s, strlen(s) + 1);
    int i=0;
    while(s[i]==' ')
    {
        i++;
    }
    for (int j = i; j < strlen(s); j++)
    {
        if( s[j]==' ')
            printf("\n");
        else
            printf("%c",s[j]);
    }
    return 0;
}

