def oneAwayReplace(str1, str2):
    count = 0

    for i in range(len(str1)):
        if str1[i] != str2[i]:
            count += 1
            if count > 1:
                return False
    return True

def oneAwayInsertOrRemove(str1, str2):
    count = 0
    i = 0

    while i < len(str2):
        if str1[count + i] == str2[i]:
            i += 1
        else:
            count += 1
            if count > 1:
                return False
    
    return True

def one_away(str1, str2):
    if str1 == str2:
        return True

    if abs(len(str1) - len(str2)) > 1:
        return False
    elif len(str1) == len(str2):
        return oneAwayReplace(str1, str2)
    elif len(str1) > len(str2):
        return oneAwayInsertOrRemove(str1, str2)
    elif len(str1) < len(str2):
        return oneAwayInsertOrRemove(str2, str1)

print(one_away("pale", "ple"))
print(one_away("pales", "pale"))
print(one_away("pale", "bale"))
print(one_away("pale", "bake"))
print(one_away("pale", "bpale"))
print(one_away("bpale", "pale"))