from armorclass import *
class Charclass:
    def __init__(self,strg,dext,cons,intl,will,perc,chrm):
        self.strg=strg
        self.dext=dext
        self.cons=cons
        self.intl=intl
        self.will=will
        self.perc=perc
        self.chrm=chrm


        self.aslot1=Armour(0,"None",1)
        self.aslot2=Armour(0,"None",2)


    def changestat(self,stat,nval):
        self.__setattr__(stat,nval)


    def getstat(self,stat):
        return self.__getattribute__(stat)
    def getstatbonus(self,stat):
        return self.attomod(self.__getattribute__(stat))

    def attomod(self,stat):
        mod_dict={
            0:-3,1:-3,2:-3,3:-3,4:-3,5:-2,6:-2,7:-1,8:-1,9:0,10:0,11:0,
            12:0,13:1,14:1,15:2,16:2,17:3,18:3,19:4,20:4,21:4,22:4,23:4
        }
        return mod_dict.get(stat,0)


'''
p1=charclass(10,16,10,10,10,10,10)
print(p1.acscore)
p1.changestat('dext',13)
print(p1.acscore)
print(p1.getstat('dext'))
'''