from pwn import *
from ast import literal_eval

file = open('enc_flag', "r")
lines = file.readlines()
line = lines[2][11:]
l = literal_eval(line)
key = "trudeau"

for i in range(len(l)):
    l[i] = (int)(l[i]/311/12)

st = ""
for j in l:
    st = st + chr(j)

rev = ""
key_len = len(key)
for k in range(len(st)):
    key_char = key[k % key_len]
    unenc_char = chr(ord(st[k]) ^ ord(key_char))
    rev += unenc_char
print(rev[::-1])
