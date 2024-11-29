hex = input("Enter your hexadecimal number : ")

#FOR NUMBERS CONTAINING FRACTIONAL PART
if '.' in hex:
    l = []                             #TAKING EMPTY LIST TO SEPARATE INTEGER AND FRACTIONAL VALUES
    l2 = []
    l1 = hex.split('.')

    iv = l1[0]
    fv = l1[1]

    for i in range (len(iv)):
        l.append(iv[i])

    for m in range(len(fv)):
        l2.append(fv[m])

    d = {'0':'0000','1':'0001','2':'0010','3':'0011','4':'0100','5':'0101','6':'0110','7':'0111','8':'1000','9':'1001','A':'1010','B':'1011','C':'1100','D':'1101','E':'1110','F':'1111'}

    b = ""
    b1 = ""
    for j in l:
        for k,v in d.items():
            if j == k:
                b = b + v

    for z in l2:
        for x,y in d.items():
            if z == x:
                b1 = b1+y

    print("Binary of your given hexadecimal number is : ",b+'.'+b1)
# IF THERE IS NO FRACTIONAL PART IN THE HEXADECIMAL NUMBER
else:
    l = []
    for i in range(len(hex)):
        l.append(hex[i])
    d = {'0':'0000','1':'0001','2':'0010','3':'0011','4':'0100','5':'0101','6':'0110','7':'0111','8':'1000','9':'1001','A':'1010','B':'1011','C':'1100','D':'1101','E':'1110','F':'1111'}

    b = ""
    
    for j in l:
        for k,v in d.items():
            if j == k:
                b = b + v
    print(b)