fiyats = {
    "çay" : 2,
    "kahve" : 3,
    "çikolata" : 5,
    "laptop" : 7,
    "other" : 11
}
"""q1 carries the quickest solution which includes less number of items but may return some money left"""
q1 = {
    "çay" : 0,
    "kahve" : 0,
    "çikolata" : 0,
    "laptop" : 0,
    "other" : 0
}
"""q2 carries the best solution that returns absolutely 0 if there is an item in q2 exists also may have much more item quantity"""
q2 = {
    "çay" : 0,
    "kahve" : 0,
    "çikolata" : 0,
    "laptop" : 0,
    "other" : 0
}
sortedfiyat = sorted(fiyats, key = fiyats.get, reverse=True)
def otomat(para, istek):
    """Function that imitates the behaviour of basic otomat(vending machine in English) ;
    Takes 2 argument : First is the amount of money , Second is item that wanted
    Returns amount of money if sale had happended
    Returns false if sale is interrupted for several reasons"""
    if not istek in fiyats:
        return -1
    elif para - fiyats[istek] < 0:
        return -1
    else:
        return  para - fiyats[istek]
def recur(para):
    """Function that checks if the result can be 0
    returns False when it cant
    returns True if there is a solution"""
    if para == 0:
        return True
    else:
        for item in sortedfiyat:
            value = otomat(para,item)
            if value != -1:
                nextval = recur(value)
                if nextval == True:
                    q2[item] += 1
                    return True
        return False
def check(para):
    kalan = para
    for item in sortedfiyat:
        while True:
            temp = otomat(kalan , item)
            if temp != -1:
                kalan = temp
                q1[item] += 1
            else:
                break
    print("En hizli çözüm ;")
    print (q1)
    if recur(para) and kalan != 0:
        print("En iyi cözum ;")
        print (q2)
check(12)
