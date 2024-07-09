

acscore=10
acscorelist=[['base',10,'base modifier']]

def acscorecalc():
    acscorec=0
    for i in(acscorelist):
        acscorec+=i[1]
    print(acscorelist)
    print(acscorec)
    acscore=acscorec
    return(acscore)



def acscorelistchange(name,mod,desc):
    acch=0
    for i in range(len(acscorelist)):
        if(acscorelist[i][0]==name):
            if(mod==0):
                acscorelist.pop(i)
                acch=1
                break
            else:
                acscorelist[i][1]=mod
                acch=1
                break
    if(acch==0):
        acscorelist.append([name,mod,desc])
    return(acscorecalc())