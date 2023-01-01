#god, dog -> true
#god, dawg -> false

def isPermutation(word1, word2):
    if len(word1) != len(word2):
        return False
    list1 = sorted(list(word1))
    list2 = sorted(list(word2))
    if list1 == list2:
        return True
    return False

print(isPermutation("god", "gdd"))
#O(nlogn)

def isPermutation(word1, word2):
    if len(word1) != len(word2):
        return False
    
    hash = {}
    for i in word1:
        if i in hash:
            hash[i] += 1
        else:
            hash[i] = 1

    for i in word2:
        if i in hash and hash[i] != 0:
            hash[i] -= 1
        else:
            return False
    
    return True

print(isPermutation("", ''))
print(isPermutation("god", 'dog'))
print(isPermutation("god", 'dgg'))
print(isPermutation("abcc", 'cabc'))
print(isPermutation("sos", 'os'))
#O(n)