S = input()
Q = input()
let = {}
result = ["" for _ in range(len(S))]
for index, elem in enumerate(S):
    if let.get(elem):
        let[elem] += 1
    else:
        let[elem] = 1
    if elem == Q[index]:
        result[index] = "P"
        let[elem] -= 1
for index, elem in enumerate(Q):
    if result[index] == "P":
        continue
    if let.get(elem) and let.get(elem) != 0:
        let[elem] -= 1
        result[index] = "S"
    else:
        result[index] = "I"
print("".join(result))
