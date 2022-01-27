st = input()
st_new =""
for i in range(len(st)):
    if st[i].isalpha():
        st_new += st[i].lower()
Flag = True
for i in range(int(len(st_new)/2)):
    if st_new[i] != st_new[-1-i]:
        Flag = False
if Flag:
    print("True")
else:
    print("False")