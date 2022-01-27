dict = {
    2: 'abc',
    3: 'def',
    4: 'ghi',
    5: 'jkl',
    6: 'mno',
    7: 'pqrs',
    8: 'tuv',
    9: 'wxyz'
}


def generator(arr, str, ind):
    if len(arr) == ind:
        print(str,end=" ")
        return
    for i in arr[ind]:
        generator(arr,str+i,ind+1)


n = input()
arr = []
for i in n:
    arr.append(dict.get(int(i)))
generator(arr,"",0)

