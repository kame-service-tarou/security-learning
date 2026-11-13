#!/usr/bin/env python3

from pwn import *

exe = ELF("./chal_patched")

context.log_level = 'debug'
context.binary = exe
context.terminal = ['tmux', 'splitw', '-h']
host = '34.170.146.252'
port = 9422

gdbscript = '''
b *vuln+102
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


def main():
    r = conn()

    r.sendlineafter(b"Select an alpaca function index: ", b"5")

    r.interactive()


if __name__ == "__main__":
    main()
