from pwn import *

sh = remote("host3.dreamhack.games", 20985)

for _ in range(50):
    eq = sh.recvline(timeout=1).decode().strip()
    a, b = eq.split('=')[0].split('+')
    sh.sendline(str(int(a) + int(b)).encode())

print(sh.recvall())