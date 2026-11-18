// gcc -o chal2 chal2.c -fno-stack-protector -no-pie
#include <stdio.h>
#include <stdlib.h>

char name[0x10] = "";

void win(long arg1, long arg2, long arg3) {
  long cmd = 0;
  if (arg1 == 0xcafecafecafecafe)
    cmd = 0x68732f;
  if (arg2 == 0x1337133713371337)
    cmd = cmd << 16 | 0x6e69;
  if (arg3 == 0xc0dec0dec0dec0de)
    cmd = cmd << 16 | 0x622f;
  system((char*)&cmd);
}

int main() {
  printf("name> ");
  fgets(name, 0x10, stdin);
  printf("hi %s\n", name);

  char buf[0x20];
  printf("input> ");
  fgets(buf, 0x100, stdin);
  puts("bye");
}

__attribute__((constructor))
void setup() {
    setvbuf(stdin, NULL, _IONBF, 0);
    setvbuf(stdout, NULL, _IONBF, 0);
    setvbuf(stderr, NULL, _IONBF, 0);
}
