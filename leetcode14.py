# strs = ["flower","flow","flight"]
# strs = ["dog","racecar","car"]
# strs = ["",""]
# strs = [""]
strs = ["ab", "a"]

if len(strs) == 1:
    print(strs[0])
elif len(strs) == 0:
    print("")
else:
    new = sorted(strs, key = lambda i:len(i), reverse=False)
    strLen = len(new[0])
    prefix = []
    _prefix = ""
    for _i in range(strLen):
        _prefix += new[0][_i]
        prefix.append(_prefix)

    index = 0
    for item in prefix:
        check = 0
        for i in range(1, len(new)):
            # print(new[i] + " index is " + str(new[i].find(item)))
            if new[i].find(item) != 0:
                check = 1
                break;
        if (check == 1):
            break;
        else:
            index += 1

    if index == 0:
        print("")
    else:
        if len(prefix) > 0:
            print(prefix[index-1])
        else:
            print("")