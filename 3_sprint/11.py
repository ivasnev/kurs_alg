import operator

global arr

def merge(arr, lf, mid, rg):
    left = arr[lf:mid-1]
    right = arr[mid-1:rg-1]
    left.sort()
    right.sort()
    compare = operator.lt
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if compare(left[i], right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    return arr[:lf] + result + arr[rg-1:]


def merge_sort(arr, lf, rg):
    if len(arr[lf:rg]) == 2:
        if arr[lf] > arr[rg-1]:
            arr[lf], arr[rg-1] = arr[rg-1], arr[lf]
        print("")
    elif len(arr[lf:rg]) == 1:
        pass
    else:
        middle = int(len(arr) / 2)
        merge_sort(arr[lf:rg], lf, middle)
        merge_sort(arr[lf:rg], middle, rg)
        tmp_arr = merge(arr[lf:rg], lf, middle, rg)


def test():
    a = [1, 4, 9, 2, 10, 11]
    b = merge(a, 0, 3, 6)
    expected = [1, 2, 4, 9, 10, 11]
    assert b == expected
    c = [1, 4, 2, 10, 1, 2]
    merge_sort(c, 0, 6)
    expected = [1, 1, 2, 2, 4, 10]
    assert c == expected


test()
