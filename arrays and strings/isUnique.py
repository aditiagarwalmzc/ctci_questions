#ctci #dhorfhohrf -> false
#adit #mig -> true

def isUnique(word):
    for i in range(len(word)):
        for j in range(i + 1, len(word)):
            if word[i] == word[j]:
                return False
    
    return True
#O(n^2)

def isUnique(word):
    list_of_chars = list(word)
    set_of_chars = set(list_of_chars)
    list_of_set = list(set_of_chars)

    if len(list_of_chars) == len(list_of_set):
        return True
    return False
#O(n)

#Using Hashmap
def isUnique(word):
    hash_map = {}
    for i in word:
        if i in hash_map:
            return False 
        hash_map[i] = 0
    return True
#O(n)