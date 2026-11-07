#include <stdio.h>

int olympic(int year) {
    if (year % 4 == 0) {
        printf("オリンピック夏\n");
    } else if (year % 4 == 2) {
        printf("オリンピック冬\n");
    } else {
        printf("開かれないぞ。かす！！\n");
    }
}

int main() {
int year;
scanf("%d", &year);
olympic(year);
return 0;
}