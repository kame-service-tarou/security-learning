#!/usr/bin/env python3

from pwn import *

exe = ELF("./echo_patched")

context.log_level = 'info'
context.binary = exe
context.terminal = ['tmux', 'splitw', '-h']
host = 'addr'
port = 1337

gdbscript = '''
break main
continue
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
    r.sendline(b'12' + b'22')
    r.interactive()


if __name__ == "__main__":
    main()
