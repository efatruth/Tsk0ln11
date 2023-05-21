flag=True
while flag:
    print("1. Innkaupalisti")
    print("2. Random tölur")
    print("3. Fyrsta og síðasta")
    print("4. Nemendur")
    print("5. Hætta")
    val=input("Sláðu inn val 1,2,3,4 og 5 til að hætta")
    if val=="1":
        print("þú hefur valið innkaupalista")
    elif val=="2":
         print("þú hefur valið Randomtölur")
    elif val=="3":
         print("þú hefur valið fyrsta og síðasta")
    elif val=="4":
         print("Nemendur")
         nafnalisti=["anna","konni","diddi","villi"]
         x=0
         while x < 3:
             nafn=input("Sláðu inn nafn á nemenda ")
             if nafn in nafnalisti:
                 print("þetta nafn er komið í listann")
                 x=x-1
             else:
                 nafnalisti.append(nafn)
                 print("Nafn hefur verið sett í listann")
             x=x+1
         print(nafnalisti)
         nafnalisti.reverse()
         print(nafnalisti)
    elif val=="5":
        print("bless bless")
        flag=False
    else:
        print("Þú verður að velja 1,2,3,4 eða 5")

'''
#strengjarallý
#Höfundur Konráð Guðmundsson
#innsláttur
def fjodi_orda(strengur):
    ord=0
    bil=0
    for stafur in strengur:
        if stafur==" ":#ef kemur bil
            bil+=1#telur bilin
    ord=bil+1
    return "Fjöldi orða í þessum texta er "+str(ord)
def fyrstu_5(strengur):
    return strengur[0:5]
def sidustu_4(strengur):
    return strengur[-4:]
def midja(strengur):
    tel=len(strengur)
    if tel % 2==0:#ef lengdin er slétttala
        return "hér er enginn miðjustafur"
    else:#það er miðstafur
        mid=int(tel/2-0.5)#finn númerið á miðstaf og breyti í heiltölu int
        return"Miðstafurinn er númer "+str(mid+1)+" sem er stafurinn "+strengur[mid]
def finna_s(strengur):
    temp=""
    for stafur in strengur:
        if stafur=="s" or stafur=="S":
            temp+=stafur
        else:
            temp+="$"
    return temp
#aðalforrit
flag=True
while flag:
    texti=input("sláðu inn texta ")
    print("1.liður 1")
    print("2.liður 2")
    print("3.liður 3")
    print("4. liður 4")
    print("5. liður 5")
    print("6 hætta")
    val=input("Veldu 1 til 5")
    if val=="1":
        print(fjodi_orda(texti))#kalla í fallið
    elif val=="2":
        print(fyrstu_5(texti))#kalla í fyrstu_5
    elif val=="3":
        print(sidustu_4(texti))#kalla í sidustu_4
    elif val=="4":
        print(midja(texti))#kalla í midja
    elif val=="5":
        print(finna_s(texti))#kalla í finna_s
    elif val=="6":
        print("bless bless bless")
        flag=False
'''
