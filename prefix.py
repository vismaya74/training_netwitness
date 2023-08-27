def strings_prefix(lis):
    length=[]
    for str in lis:
        length.append(len(str))
    min_length=min(length)
    prefix=""

    for i in range(min_length):
        letter=lis[0][i]
        for j in lis:
            if j[i]!=letter:
                return prefix
        prefix+=letter

    return prefix
#print(strings_prefix(["light","live","liver"]))
#print(strings_prefix(["light","racecar","car"]))