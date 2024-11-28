hex = input("Enter your hexadecimal number : ")

if '.' in hex:
    l = hex.split('.')

    a = l[0]
    b = l[1]

    d1 = 0
    d2 = 0
    n = len(a)-1
    n1 = -1
    for t in range(len(b)):
        if b[t] == 'A':
            c2 = '10'
        elif b[t] == 'B':
            c2 = '11'
        elif b[t] == 'C':
            c2 = '12'
        elif b[t] == 'D':
            c2 = '13'
        elif b[t] == 'E':
            c2 = '14'
        elif b[t] == 'F':
            c2 = '15'
        #elif a[i] in str(range(0,10)):
        #    c = a[i]
        else:
            c2 = b[t]
        c3 = int(c2)
        d2 = d2 + c3*(16**n1)
        n1 = n1 - 1

    for i in range(len(a)):
        if a[i] == 'A':
            c = '10'
        elif a[i] == 'B':
            c = '11'
        elif a[i] == 'C':
            c = '12'
        elif a[i] == 'D':
            c = '13'
        elif a[i] == 'E':
            c = '14'
        elif a[i] == 'F':
            c = '15'
        #elif a[i] in str(range(0,10)):
        #    c = a[i]
        else:
            c = a[i]
        c1 = int(c)
        d1 = d1 + c1*(16**n)
        n = n - 1

    dv = str(d1 + d2)
    print(dv)

    ld = dv.split('.')

    ld1 = int(ld[0])
    ld2 = ld[1]
    ld3 = int(ld2)
    bn = ""
    bn1 = ""
    dd = '0.'+ld2

    while ld1>0:
        bn = str(ld1%2) + bn
        ld1 = ld1//2

    dd1 = float(dd)
    print(bn)
    for dm in range(len(ld2)):
        cc = int(dd1*2)
        bn1 = bn1 + str(cc)
        dd1 = (dd1 * 2) - cc


    print(bn+'.'+bn1)

else:
    d1 = 0
    n = len(hex)-1
    bn = ""
    for i in range(len(hex)):
        if hex[i] == 'A':
            c = '10'
        elif hex[i] == 'B':
            c = '11'
        elif hex[i] == 'C':
            c = '12'
        elif hex[i] == 'D':
            c = '13'
        elif hex[i] == 'E':
            c = '14'
        elif hex[i] == 'F':
            c = '15'
        #elif a[i] in str(range(0,10)):
        #    c = a[i]
        else:
            c = hex[i]
        c1 = int(c)
        d1 = d1 + c1*(16**n)
        n = n - 1
    print(d1)
    while d1>0:
        bn = str(d1%2) + bn
        d1 = d1//2
    print(bn)