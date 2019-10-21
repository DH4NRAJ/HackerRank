#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>
void calculate_the_maximum(int n, int k) {
  int max1=0,max2=0,max3=0,i,j,a,b,c;
  for(i=1;i<=n;i++){
    for(j=i+1;j<=n;j++)
  {
        a=i&j;
        if(k>a && max1<a)
        {
            max1=a;
        }
        b=i|j;
        if(k>b && max2<b)
        {
            max2=b;
        }
        c=i^j;
        if(k>c && max3<c)
        {
            max3=c;
        }
  }
  }
  printf("%d\n%d\n%d",max1,max2,max3);

}

int main() {
    int n, k;
    scanf("%d %d", &n, &k);
    calculate_the_maximum(n, k);
    return 0;
}
