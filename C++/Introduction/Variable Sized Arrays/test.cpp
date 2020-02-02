#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

int main() {
    int n, q, q_i, q_j, k, **k_arr, **q_arr;
    scanf("%d %d", &n, &q);
    k_arr = (int**) malloc(n * sizeof(int*));
    q_arr = (int**) malloc(q * sizeof(int*));
    for(int i = 0; i < n; i++) {
        scanf("%d", &k);
        k_arr[i] = (int*) malloc(k * sizeof(int));
        for(int j = 0; j < k; j++) scanf("%d", &k_arr[i][j]);
    }
    for(int i = 0; i < q; i++) {
        scanf("%d %d", &q_i, &q_j);
        q_arr[i] = new int[2] { q_i, q_j };
    }
    for(int i = 0; i < q; i++) printf("%d\n", k_arr[q_arr[i][0]][q_arr[i][1]]);
    free(k_arr);
    free(q_arr);
    return 0;
}
