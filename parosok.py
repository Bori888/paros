# globális változo
also = int(input('Zárt intervallum alsó határa: '))
felso = int(input('Zárt intervallum felső határa: '))
if also > felso:
    seged = also
    also = felso
    felso = seged

def parosok_szama_1():
    paros_db = 0

    for i in range(also, felso+1):
        # ha páros
        if i % 2 == 0:
            paros_db += 1
    print("Az[", also, ",", felso, "] intervallumon a párosok száma", paros_db, ".")



def parosok_szama_2():
    # hatékonyabb megoldás
    paros_db = 0
    paros_also = also

    if also % 2 == 1:
        paros_also = also + 1
    for i in range(paros_also, felso + 1, 2):
        paros_db += 1
    print("Az[", also, ",", felso, "] intervallumon a párosok száma", paros_db, ".")

def parosok_szama_3():
    #ez a leghatékonyabb megoldás
    keplet = (felso - also) // 2
    if also % 2 == 1 and felso % 2 == 1:
        print("Az[", also, ",", felso, "] intervallumon a párosok száma", keplet, ".")
    else:
        print("Az[", also, ",", felso, "] intervallumon a párosok száma", keplet + 1, ".")