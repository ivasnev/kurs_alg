array_1 = [0]*26
array_2 = [0]*26
st_1 = input()
st_2 = input()
for i in st_1:
    array_1[ord(i)-97] += 1
for i in st_2:
    array_2[ord(i)-97] += 1
for i in range(len(array_1)):
    if array_1[i] != array_2[i]:
        print(chr(i+97))
        break