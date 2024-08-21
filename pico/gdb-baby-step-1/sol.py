from pwn import *

p = process('./debugger0_a')
pause()
p.interactive()

