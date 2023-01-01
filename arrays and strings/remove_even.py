def removeEvenNums(my_list):
    return [i for i in my_list if i % 2 != 0]

print(removeEvenNums([1,2,4,5,10,6,3]))


def mergeLists(lst1, lst2):
    return sorted(lst1 + lst2)

print(mergeLists([1,3,4,5], [2,6,7,8]))


def findSum(lst, k):
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if lst[i] + lst[j] == k:
                return [lst[i], lst[j]]

print(findSum([1,21,3,14,5,60,7,6], 81))

def findMinimum(lst):
    mini = lst[0]
    for i in lst:
        if i < mini:
            mini = i
    return mini

print(findMinimum([9,2,3,6]))

def firstUnique(lst):
    hash = {}
    for i in lst:
        if i not in hash:
            hash[i] = 1
        else:
            hash[i] += 1
    
    for i in lst:
        if hash[i] == 1:
            return i

print(firstUnique([9,2,3,2,6,6]))

def secondMax(lst):
    return sorted(list(set(lst)))[-2]

print(secondMax([9,9,2,3,6]))

def rightRotate(lst, k):
    for i in range(k - 1):
        lst.append(lst[i])
        lst.remove(lst[i])
    return lst

print(rightRotate([10,20,30,40,50], 8))