def    ft_prime(nb):
    i = 2
    if (nb <= 1):
        return(0)
    while (nb % i != 0):
        i+=1
    if (i == nb):
        return(1)
    else:
        return(0)

def     ft_boucle(i,max):
    while (i <= max):
        if ft_prime(i) != 0:
            print(i, " is prime")
            i+=1
        elif ft_prime(i) == 0:
            i+=1

ft_boucle(1,1000)
