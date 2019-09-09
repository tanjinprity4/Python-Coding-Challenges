def anagrams(str1, str2):
    if len(str2) != len(str1):
     return False
    dict1 = {}
    dict2 = {}
    for i in str1:
        dict1[i] = dict1.get(i, 0) + 1
    for i in str2:
        dict2[i] = dict2.get(i, 0) + 1

    for i in str1:
        if i not in dict2.keys():
            return False
        elif dict1[i] != dict2[i]:
            return False
        else:
            return True


print(anagrams("abc", "dbc"), "fg")
print(anagrams("abc", "bac"))
