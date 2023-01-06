def diag(nb):
    i = 1
    print("+", end="")
    print((nb + 1) * "-", end="")
    print("+")

    while i < nb:
        print("|", end="")
        print((nb - i) * "#", end="")
        print(' ', end="")
        print(i*"#",end="")
        print("|")
        i+=1


    print("+", end="")
    print((nb + 1) * "-", end="")
    print("+")

diag(10)
