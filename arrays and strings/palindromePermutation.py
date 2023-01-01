def palindromePermutation(str):
    hash = {}
    str = str.replace(" ", '')
    for i in str:
        if i not in hash:
            hash[i] = 1
        else:
            hash[i] += 1

    count = 0
    for i in hash:
        if hash[i] % 2 != 0:
            count += 1
            if count > 1:
                return False
    
    return True

print(palindromePermutation("tact coa"))
