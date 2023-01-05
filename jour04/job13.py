def ft_len(list):
    count = 0
    for i in list:
        count+=1
    return(count)

def ft_solo(list):
    i = 0
    j = 0
    k = 1
    dummy = list
    max = ft_len(list)
    while i < max:
        while j < max:
            while k < max:
                if list[j] == list[k]:
                    dummy[k] = 0
                    k+=1
                else:
                    k+=1
            k = j + 2
            j+=1
        i+=1
    return (dummy)

def check_z(list):
    i = 0
    sum = 0
    max = ft_len(list) 
    while i < max:
        if list[i] != 0:
            sum+=1
            i+=1
        else:
            i+=1
    return (sum)

def ft_dubble(list):
    i = 0
    j = 0
    dum = ft_solo(list)
    good_list = [0]*check_z(list)
    max = ft_len(list)
    while i < max:
        if dum[i] != 0:
            good_list[j] = dum[i]
            i+=1
            j+=1
        else:
            i+=1
    return (good_list)

L = [10,20,30,20,10,50,60,40,80,50,40]

print('before being a god = ', end='')
print(L)
print('after being a god = ', end='')
print(ft_dubble(L))
