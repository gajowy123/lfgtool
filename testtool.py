from tkinter import *
from cmmds import *
import re

window=Tk()
window.title("testapp")

window.geometry('900x900')
window.tk.call('tk','scaling',2.0)

mybox=IntVar()

dexnum=IntVar()


def btncancel_clicked():
    window.destroy()




def dexnumchange(*args):
    dxn=int(dexnum.get())
    print(dxn)

    acscoren=acscorelistchange('dex',dxn,'dex modifier')
    aclbl.config(text=acscoren)


def checknum(nv):
    return re.match('^[0-9]*$',nv) is not None and len(nv)<=2
checknumwrap=(window.register(checknum),'%P')






lbl=Label(window,text='this is some text')
lbl.grid(column=0,row=0)

attributeFrame=Frame(window,relief='raised',borderwidth=2)
attributeFrame.grid(column=0,row=1)

attributelbl=Label(attributeFrame,text='Attributes')
attributelbl.grid(column=0,row=0)
attributescore=Label(attributeFrame,text='Score')
attributescore.grid(column=1,row=0)
attributestrength=Label(attributeFrame,text='Strength')
attributestrength.grid(column=0,row=1)
attributedex=Label(attributeFrame,text='Dexterity')
attributedex.grid(column=0,row=2)



entrystrength=Entry(attributeFrame,textvariable=mybox,width=2)
entrystrength.grid(column=1,row=1)
entrydex=Entry(attributeFrame,width=2,textvariable=dexnum,validate='key',validatecommand=checknumwrap)
entrydex.grid(column=1,row=2)

dexnum.trace_add('write',dexnumchange)

acframe=Frame(window,relief='solid',borderwidth=2)
acframe.grid(column=1,row=1)
aclbln=Label(acframe,text="AC")
aclbln.grid(column=0,row=0)
aclbl=Label(acframe,text=acscore)
aclbl.grid(column=0,row=1)


window.mainloop()