'''
def f(x):
    if (x <= -2):
        return 1 - (x + 2) ** 2
    elif (-2 < x <= 2):
        return -x / 2
    else:
        return (x - 2) ** 2 + 1
        '''
'''
def modify_list(l):
    le = len(l)-1
    i = le
    while i!=-1:
        if l[i]%2:
            del l[i]
        else:
            l[i]=l[i]//2
        i -=1
    return
    '''
