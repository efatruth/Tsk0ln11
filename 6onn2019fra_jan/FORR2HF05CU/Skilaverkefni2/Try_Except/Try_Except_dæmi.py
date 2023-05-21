import sys
""" 
listi = []
teljari = 0
while teljari < 10:
    try:
        tala = int(input("slaðu inn  tölu"))
        listi.append(tala)
        teljari = teljari +1
    except ValueError:
        print("það þarf að slá inn tölu")

print(listi)
"""
try:
    tala = int(input("sladu inn tölu" ))
except ValueError:
    print ("það þarf að slá inn tölu")

try:
    utkoma = 25/0
    print(utkoma)
except ZeroDivisionError:
    print(sys.exc_info())

'''
import sys
listi[]

for x in range (10):
tala = int(input(slaðu inn tíu tölu))
list.append(tala)

print(listi)

    try:
        print("þetta x er ", x)
        r= l/int(x)
        break
    except:
        print("þessi villa kom up")
        
    

    
'''

def tolur(*tolur):
    summa =0
    for x in tolur:
        summa+=x
        return summa

def setning (nafn="konni",nafn="",nafn="")
    print()


