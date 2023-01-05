def ft_len(list):
    count = 0
    for i in list:
        count+=1
    return(count)

def select(num,list):
    i = 0
    j = 0
    count = 0
    max = ft_len(list)
    print('"', end='')
    while i < max:
        while list[i] != ' ' and i < max - 1:
            count+=1
            i+=1
        if count >= num:
            j = (i - count) - 1
            while j < i:
                print(list[j], end='')
                j+=1
            if i == (max - 1):
                print(list[i], end='')
                i+=1
            else:
                print(' ', end='')
            count = 0
        else:
            i+=2
            count = 0
    print('"')

select(3,"La peur est le chemin vers le côté obscur la peur mène à la colère la colère mène à la haine la haine mène à la souffrance")
