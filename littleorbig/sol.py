from pwn import *

l = [0x63, 0x6b, 0x3a, 0x29, 0x64, 0x72, 0x6d, 0x68]

sh = remote("host3.dreamhack.games", 11889)

sh.recvuntil(b":")
sh.sendline("".join([chr(i) for i in reversed(l)]).encode())

sh.interactive()