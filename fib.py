print('ciąg fibonacciego! ')
x = int(input("Wpisz która liczbe fibonacciego chcesz pokazać: "))
a = 0
b = 1

if x == 0:
    print ("0")
if x == 1:
    print("1")
if x>1:
    for i in range (0,x):
        c = a+b
        a=b
        b=c
    print(c)
