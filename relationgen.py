def relationcreator(set1,set2):
    res = []
    res.append('R')
    res.append('=')
    res.append('{')
    for i in range(len(set1)):
        for j in range(len(set2)):
            res.append('(')
            res.append(set1[i])
            res.append(',')
            res.append(set2[j])
            res.append(')')
            if i != (len(set1) - 1) or j != (len(set2) - 1):
                res.append(',')
    res.append('}')
    return(''.join(res))