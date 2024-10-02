with open('data.txt', 'r') as file:
    num=file.readlines()
    values=[int(i) for i in num]
    lent=int(values.__len__())
    print (sum(values)/lent)