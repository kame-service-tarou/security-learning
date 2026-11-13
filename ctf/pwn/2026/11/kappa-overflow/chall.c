#include <stdio.h>
#include <windows.h>

void win() {
    SetConsoleOutputCP(65001);

    FILE *fp = fopen("flag.txt", "r");
    if (!fp) {
        puts("flag file not found");
        return;
    }
    char buf[128];
    fgets(buf, sizeof(buf), fp);
    puts(buf);
    fclose(fp);
}

LONG WINAPI handler(EXCEPTION_POINTERS *ExceptionInfo) {
    fprintf(stderr, "\nException code: 0x%lx\n", ExceptionInfo->ExceptionRecord->ExceptionCode);
    win();
    ExitProcess(0);
    return EXCEPTION_CONTINUE_SEARCH;
}

int main() {
    setvbuf(stdout, NULL, _IONBF, 0);
    SetUnhandledExceptionFilter(handler);

    struct {
        char buf[64];
        volatile int *target;
    } cache;

    int dummy = 0;
    cache.target = &dummy;

    puts("Input:");
    fflush(stdout);

    gets(cache.buf);

    *cache.target = 1;
    
    puts("OK");
    return 0;
}
