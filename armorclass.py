
class Armour:
    def __init__(self,ac,desc,type):
        self.ac=ac          # armour class modifier of item
        self.desc=desc      # description of item
        self.type=type      # type of item 1 = armor, 2 = shield

    def getac(self):
        return(self.ac)
    def getdesc(self):
        return(self.desc)