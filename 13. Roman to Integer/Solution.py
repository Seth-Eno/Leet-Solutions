def romanToInt(s):

    order = 'MDCLXVI'

    value = {
        'M': 1000,
        'D': 500,
        'C': 100,
        'L': 50,
        'X': 10,
        'V': 5,
        'I': 1
    }

    total = 0

    s = list(s)

    for i in range(len(s)):
        #print(i)
        if len(s) >= 3:
            print(order.index(s[i + 1]))
        
        if order.index(s[i]) < order.index(s[i + 1]) and len(s) >= 3:
            total += value[s[i + 1]] - value[s[i]]
            s.pop(0)
            s.pop(0)
        else:
            total += value[s[i]]
            s.pop(0)
    
    return total

romanToInt("XXIV")