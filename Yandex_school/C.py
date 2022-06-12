import json
from datetime import datetime


input_json = input()
input_dict = json.loads(input_json)
for _ in range(5):
    inp = input().split()
    if inp[0] == "NAME_CONTAINS":
        NAME_CONTAINS = inp[1]
    elif inp[0] == "PRICE_GREATER_THAN":
        PRICE_GREATER_THAN = int(inp[1])
    elif inp[0] == "PRICE_LESS_THAN":
        PRICE_LESS_THAN = int(inp[1])
    elif inp[0] == "DATE_AFTER":
        DATE_AFTER = inp[1].split(".")
        date_after = datetime(int(DATE_AFTER[2]), int(DATE_AFTER[1]), int(DATE_AFTER[0]))
    elif inp[0] == "DATE_BEFORE":
        DATE_BEFORE = inp[1].split(".")
        date_before = datetime(int(DATE_BEFORE[2]), int(DATE_BEFORE[1]), int(DATE_BEFORE[0]))
res = []
for x in input_dict:
    if x['name'].lower().find(NAME_CONTAINS.lower()) != -1:
        if PRICE_GREATER_THAN <= x['price'] <= PRICE_LESS_THAN:
            cur_date = x["date"].split(".")
            cur_date = datetime(int(cur_date[2]), int(cur_date[1]), int(cur_date[0]))
            if date_after <= cur_date <= date_before:
                res.append(x)
res.sort(key=lambda x: x["id"])
res = json.dumps(res)
print(res)
