#livinus felix bassey
#Skilaverkefni2
#10.09.2018

import csv

class Lager_hlutur:
    #býr til nýjan hlut á lager
    def __init__(self, numer,tegund,fjoldi,verd):
        self.numer = numer
        self.tegund = tegund
        self.fjoldi = fjoldi
        self.verd = verd

        alltsedla = Lager_hlutur.alltsedla+1

    #Reiknar heildarverðmæti hlutar
    def verdReikhlut(self):
        result = self.fjoldi * self.verd #her er koda sem vantaði
        return result

    #Prentar út upplýsingar
    def prenta_lager_hlut(self):
        print(self.numer,self.tegund,self.fjoldi,self.verd) #her er koda sem vantaði self.tala1 * self.tala2
            
