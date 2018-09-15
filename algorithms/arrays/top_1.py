"""
this algorithms receive array and check most_frequent_value(a.k.a mode). Also, sometimes it can be have numerous most_frequent_value,
so this funtion returns list. This result can be used as finding representative value on array.

This algorithms get array, and make dictionary of it, find most frequent count, and make result list.

For example) top_1([1, 1, 2, 2, 3, 4]) will return [1, 2]

Complexity: O(n)
"""
def top_1(arr):
    values = {}
    #reserve each value which first appears on keys
    #reserve how many time each value appears by index number on values
    result = []
    f_val = 0

    for i in arr:
        if i in values:
            values[i] += 1
        else:
            values[i] = 1

    f_val = max(values.values())
        
    for i in values.keys():
        if values[i] == f_val:
            result.append(i)
        else:
            continue
    
    return result


def top_1_v2(arr):
    # Once Iteration
    ans = []
    mostcount = 0
    count = {}
    for x in arr:
        count[x] = count.get(x, 0) + 1
        if count[x] > mostcount:
            ans = [x]
            mostcount = count[x]
        elif count[x] == mostcount:
            ans.append(x)
    return ans