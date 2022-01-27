# ID 63465679
# Сложность по времени создания базы слов O(n*m) где n кол. исходных документов
# а m кол. слов в них
# Сложность по времени обработки запросов O(k*l) где k кол. исходных запросов
# а l кол. слов в них
# Общая временная сложность в худшем случае O(n*(m+l))
# так как колличество зпаросов и документов ограничено 10**4
# Сложность по памяти O(n+m) где n,m колличество уникальных слов в документах и запросах соответсвенно

# Я не знаю как сделать за О(5n),
# я пробовал заменить сортировку на поиск 5 максимумов,
# но становилось хуже хотя он работает за O(5n)
from collections import Counter

n = int(input())
base_words = {}
for i in range(n):
    for word in Counter(input().split()).items():
        if base_words.get(word[0]):
            base_words[word[0]].append((word[1], i))
        else:
            base_words[word[0]] = [(word[1], i)]
m = int(input())
task = set()
ans = []
for i in range(m):
    tmp_rev = [[0, x] for x in range(n)]
    new_task = set(input().split())
    if new_task == task:
        print(" ".join(map(str, ans)))
        continue
    else:
        task = new_task
        ans = []
    for j in task:
        if base_words.get(j):
            for i in base_words.get(j):
                tmp_rev[i[1]][0] = tmp_rev[i[1]][0] + i[0]
    tmp_rev.sort(reverse=True, key=lambda x: x[0])
    for j in range(5):
        if j < len(tmp_rev) and tmp_rev[j][0] != 0:
            ans.append(tmp_rev[j][1] + 1)
    print(" ".join(map(str,ans)))