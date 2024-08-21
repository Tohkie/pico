from binascii import unhexlify

cache = ['80c9a04', '804007d', '65343863', '33663462', '5f597230', '6d334d5f', '50755f4e', '34656c43', '7b465443', '6f636970'] 
flag = ""
for pin in cache:
	try:
		flag += unhexlify(pin).decode()
	except:pass

print(flag[::-1])

