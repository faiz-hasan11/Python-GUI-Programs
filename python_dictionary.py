from tkinter import *
import wikipedia
def getme():
    l.delete(1.0,END)
    x=e.get()
    try:
        ans=wikipedia.summary(x)
        l.insert(INSERT, ans)
    except:
        l.insert(INSERT,"Please check you input or internet connection")


root=Tk()
topf=Frame(root)
topf.pack(side=TOP)
e=Entry(topf)
e.pack()
b=Button(topf,text="Search",command=getme)
b.pack()


bottomf=Frame(root)
bottomf.pack(side=BOTTOM)
s=Scrollbar(bottomf)
s.pack(side=RIGHT,fill=Y)
l=Text(bottomf,width=20,height=10,yscrollcommand=s.set,wrap=WORD)
l.pack(side=LEFT)
s.config(command=l.yview)
root.mainloop()
