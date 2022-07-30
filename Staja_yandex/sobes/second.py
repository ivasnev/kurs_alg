# Find sub_str in str Time(O(t)+O(s))

from collections import Counter


def main(s, t):
    dict_s = Counter(s)
    counter = len(dict_s)
    s_len = len(s)
    if len(t) < len(s):
        return -1
    for i in range(s_len):
        ch = t[i]
        if dict_s.get(ch):
            dict_s[ch] -= 1
            if dict_s[ch] == 0:
                counter -= 1
            elif dict_s[ch] == -1:  # {"a" : 0} aaaab
                counter += 1
    if counter == 0:
        return 0
    for i in range(1, len(t) - s_len + 1, 1):
        if counter == 0:
            return i
        # remove
        ch = t[i - 1]
        if dict_s.get(ch):
            dict_s[ch] += 1
            if dict_s[ch] == 0:
                counter -= 1  # буква начала совпадать
            elif dict_s[ch] == 1:  # буква перестала совпадать
                counter += 1
        # add
        ch = t[i + s_len - 1]
        if dict_s.get(ch):
            dict_s[ch] -= 1
            if dict_s[ch] == 0:
                counter -= 1
            elif dict_s[ch] == -1:  # {"a" : 0} aaa
                counter += 1
    if counter == 0:
        return len(t) - 1
    else:
        return -1


if __name__ == "__main__":
    _t = "a "
    _s = " "
    print(_t.find(_s), main(_s, _t))
    assert _t.find(_s) == main(_s, _t)
