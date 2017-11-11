from tkinter import *
from tkinter import ttk
import imagecreator as imgc
import relationgen as rgen
class img:
    count=0
    def imgcreation(event):
        picture = PhotoImage(file='')
        s1=list(map(str,(entr1.get()).split()))
        s2=list(map(str,(entr2.get()).split()))
        imgc.createimg(s1,s2)
        res=rgen.relationcreator(s1,s2)
        result.set(res)
    def disp(self):
        global picture3
        picture3 = PhotoImage(file='img.png')
        canvas.itemconfigure(picture2, image=picture3)

root=Tk()
result=StringVar()
root.geometry("900x630")
style=ttk.Style()
style.configure("TLabel",
                foreground="dark slate blue",
                font="Times 30 bold italic underline",
                padding=10,
                anchor=CENTER)
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(1, weight=1)
mainframe.rowconfigure(20, weight=3)
mainframe.columnconfigure(4, weight=3)
mainframe.rowconfigure(1, weight=1)
ttk.Label(mainframe,text="   CARTESIAN PRODUCT    ").grid(row=1,column=2,columnspan=3,sticky=W+E)
Label(mainframe,text="SET-1",height=5,width=5,font=(None,15)).grid(row=3,column=1,sticky=W+E)
entr1=Entry(mainframe,width=15)
entr1.grid(column=2,row=3,sticky=W+E)
Label(mainframe,text="SET-2",font=(None,15)).grid(row=4,column=1,sticky=W+E)
entr2=Entry(mainframe,font='large_font')
entr2.grid(column=2,row=4,sticky=W+E)
btn=Button(mainframe,text="GENERATE RELATION",font=(None,15))
btn.bind("<Button-1>",img.imgcreation)
btn.grid(column=4,row=5,sticky=E)
Label(mainframe,textvariable=result,font=(None,15)).grid(row=8,column=2,columnspan=3,sticky=E)
testButton = Button(mainframe,text=" GENERATE IMAGE ",font=(None,15))
testButton.bind("<Button-1>",img.disp)
testButton.grid(row=5,column=5,sticky=W)
canvas=Canvas(width=400, height=300, bg='black')
canvas.grid(row=20,ipadx=50,columnspan=5,sticky=E+W)
picture = PhotoImage(file='')
picture2=canvas.create_image(70, 10, image=picture,anchor=NW)
root.mainloop()