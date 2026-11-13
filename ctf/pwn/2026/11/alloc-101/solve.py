#!/usr/bin/env python3

from pwn import *

exe = ELF("./chall_patched")

context.log_level = 'debug'
context.binary = exe
context.terminal = ['tmux', 'splitw', '-h']
host = '34.170.146.252'
port = 52521

gdbscript = '''
b *main
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
    r.sendlineafter(b"choice> ", b"4")
    

    r.interactive()


if __name__ == "__main__":
    main()
