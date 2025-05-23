def f(s):
    res = []
    for i in range(len(s)):
        a = s[i]
        if a in s[i+1:]:
            res.append(a.upper()) # "ala8".upper() == "ALA8"
    if not res:
        res = list(s)
    return ''.join(res) + '!'
L = 3 * [0,1]
#L += list('ab')
#L.append( len(L) == 8 or L[99] == 9)
#L = []
#L.append( f('abc'))
#L.append( f('abcabcde') )
L += [2*[]]
print(L)