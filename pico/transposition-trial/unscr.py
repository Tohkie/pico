scr = 'heTfl g as iicpCTo{7F4NRP051N5_16_35P3X51N3_V091B0AE}2'
n = 3
arr = [scr[i:i+n] for i in range(0, len(scr), n)]
for i in range(len(arr)):
    arr[i] = arr[i][2] + arr[i][0] + arr[i][1]

flag = "".join(arr)
print(flag)
