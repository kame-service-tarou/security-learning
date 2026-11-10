#include <stdio.h>

int main() {
    int array[10];
    int size = sizeof(array) / sizeof(array[0]);
    for (int i = 0; i < size; i++) {
        printf("%d番目の数値を入力してください", i + 1);
        scanf("%d", &array[i]);
    }
    for (int j = 9; j >= 0; j--) {
        printf("%d\n", array[j]);
    }
}