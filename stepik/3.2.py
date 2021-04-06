'''
def update_dictionary(d, key, value):
    if key in d:
        d[key].append(value)
    elif key is not d:
        if 2*key is d: 
            d[2*key].append(value)
        elif (2*key is not d) and d.get(2*key)==None:
            d[2*key]=[]
            d[2*key].append(value)
        elif (2*key is not d) and d.get(2*key)!=None:
            d[2*key].append(value)
    return     
    '''
'''
a=[i.lower() for i in input().split()]
for i in set(a):
    print(i,a.count(i))
'''
dict={}
n=int(input())
for i in range(n):
    x=int(input())
    if x in dict:
        print(dict[x])
    else:
        dict[x]=f(x)
        print(dict[x])
