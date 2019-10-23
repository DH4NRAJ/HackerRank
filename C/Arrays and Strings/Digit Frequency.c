//Digit Frequency
#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int main() {    
    char str[1001];
    scanf("%s", str);
    int res[10] = {0, };
    for (int i = 0; i < strlen(str); ++i) {
        if (str[i] >= '0' && str[i] <= '9') {
            ++res[str[i] - '0'];
        }
    }
    for (int i = 0; i < 10; ++i) {
        printf("%d ", res[i]);
    }
    return 0;
}
