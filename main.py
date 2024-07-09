
import charclass
import armorclass

class charsheet:
    def __init__(self,strg,dext,cons,intl,will,perc,chrm,lvl,clas,race):
        # basics
        self.lvl=lvl
        self.clas=clas
        self.race=race

        self.maxluck()
        self.luck=self.mxluck


        # set attributes
        attributes=charclass.Charclass(strg,dext,cons,intl,will,perc,chrm)

        # set armour
        self.arms1=armorclass.Armour(0,'None',1)
        self.arms2=armorclass.Armour(0,'None',2)

        # calculate bonuses
        self.ac=10+attributes.getstatbonus('dext')+self.arms1.getac()+self.arms2.getac()
        self.conbonus=attributes.getstatbonus('cons')
        self.tohit=attributes.getstatbonus('strg')



    def donarmour(self,newarm):
        if newarm.type==1:
            if self.arms1.getdesc()=='None':
                droparm=0
                self.arms1=newarm
            else:
                droparm=self.arms1
                self.arms1=newarm
        else:
            if self.arms2.getdesc()=='None':
                droparm=0
                self.arms2=newarm
            else:
                droparm=self.arms2
                self.arms2=newarm
        return droparm
        # sets new armour, returns old armour, recalculates ac

    def maxluck(self):
        self.mxluck=10+self.lvl//2
    def maxreroll(self):
        self.mxreroll=self.lvl
        if self.race=='human':
            self.mxreroll+=1



chara=charsheet(10,13,17,10,10,10,10,1,'bard','human')
print(chara.conbonus)

