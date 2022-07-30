def validate(date):
    date.sort()
    if date[0] < 13 and date[1] < 13 and not (date[0] == 12 and date[1] == 12):
        return 0
    else:
        return 1



print(validate(list(map(int, input().split()))))
