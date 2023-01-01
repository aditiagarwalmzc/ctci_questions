#aabcccccaaa -> a2b1c5a3

def compressString(input_str):
    count = 1
    input_str += " "
    newStr = ""
    for i in range(len(input_str) - 1):
        if input_str[i] == input_str[i + 1]:
            count += 1
        else:
            newStr += input_str[i] + str(count)
            count = 1
    return newStr

print(compressString("aabcccccaaa"))
        