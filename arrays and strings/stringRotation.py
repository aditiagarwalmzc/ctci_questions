def stringRotation(s1, s2):
    if len(s1) == len(s2):
        s1 += s1
        return isSubstring(s1, s2)
    return False

def isSubstring(s1, s2):
    if s2 in s1:
        return True
    return False

print(stringRotation("waterbottle", "erbottlewat"))
print(stringRotation("waterbottle", "rebottlewat"))