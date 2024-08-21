from binascii import unhexlify

cache = ['80c9a04', '8049ee4', '8051339', '80e7000', '80e000a', '776f656d', '776f656d', '776f656d', '776f656d', '776f656d']
flag = ""
for pin in cache:
	try:
		flag += unhexlify(pin).decode()
	except:pass

print(flag[::-1])

