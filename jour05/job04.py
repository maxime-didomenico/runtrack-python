mess = input("please enter a message : ")

def cesar(msg, clé=0):
    alpha = "abcdefghijklmnopqrstuvwxyz"
    modif = ""

    for l in msg.lower():
        pos = alpha.find(l)

        if pos != -1:
            modif += alpha[(pos + clé) % len(alpha)]
        else:
            modif += l
    return (modif)

print(cesar(mess, 3))
