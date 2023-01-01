#input -> "Mr John Smith    ", 13
#Output -> "Mr%20John%20Smith"

from typing import final


def urlify(str1, size):
    str1 = str1[0:size]
    str1 = str1.replace(" ", "%20")
    return str1

#O(n)

def urlify(str1, size):
    result = []
    for char in str1[0:size]:
        if char is " ":
            temp = "%20"
        else:
            temp = char
        result.append(temp)
        final_string = "".join(result)
    return final_string
#O(n)

print(urlify("Mr John Smith    ", 13))
