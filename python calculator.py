from tkinter import *
root=Tk()
root.title("Calculator")
root.geometry("400x500+200+100")
root.resizable(FALSE,FALSE)
entry_box=Entry(width=43,justify=RIGHT)
entry_box.insert(0,"0")
entry_box.place(x=70,y=50)

def enternumber(x):
    k = entry_box.get()
    i = k[-1:]
    if x==i:
        pass
    else:
        if entry_box.get() == "0":
            if x =='.':
                entry_box.insert(1,'.')
            else:
                entry_box.delete(0,END)
                entry_box.insert(0,str(x))
        else:
            length=len(entry_box.get())
            entry_box.insert(length,str(x))
def enterop(x):
    if entry_box.get() !="0":
        length=len(entry_box.get())
        k=entry_box.get()
        i=k[-1:]
        if i in ["+","-","*","/"]:
            pass
        else:
            entry_box.insert(length,btnop[x]['text'])


def clr():
    entry_box.delete(0,END)
    entry_box.insert(0,"0")

def dele():
    length=len(entry_box.get())
    entry_box.delete(length-1,END)
    if length == 1:
        entry_box.insert(0,"0")
def eq():
    c=entry_box.get()
    r=eval(c)
    entry_box.delete(0,END)
    entry_box.insert(0,r)
btn=[]
for i in range(10):
    btn.append(Button(width=6,text=str(i),bd=6,command=lambda x=i:enternumber(x)))
btntext=1
for i in range (3):
    for j in range(3):
        btn[btntext].place(x=30+j*90,y=90+i*70)
        btntext+=1
btnzero=Button(width=32,text="0",bd=6,command=lambda x=0:enternumber(x))
btnzero.place(x=30,y=290)
btnop=[]
for i in range(4):
    btnop.append(Button(width=6,bd=6,command=lambda x=i:enterop(x)))


btnop[0]['text'] = '+'
btnop[1]['text'] = '-'
btnop[2]['text'] = '*'
btnop[3]['text'] = '/'

for i in range(4):
    btnop[i].place(x=290,y=80+i*70)

btnc=Button(width=20,text="C",bd=6,command=clr)
btnc.place(x=30,y=350)

btnd=Button(width=20,text=".",bd=6,command=lambda x=".":enternumber(x))
btnd.place(x=30,y=400)

btne=Button(width=20,text="=",bd=6,command=eq)
btne.place(x=200,y=400)

btndel=Button(width=20,text="DEL",bd=6,command=dele)
btndel.place(x=200,y=350)

root.mainloop()
