from tkinter import *
import tkinter.messagebox
import backend
class Fruit:
    def __init__(self,root):
        self.root = root
        self.root.title("Devil Fruit from One Piece Database")
        self.root.geometry("1350x750+0+0")
        self.root.config(bg="Light Blue")

        WikiLink = StringVar()
        FruitNumber = StringVar()
        Name = StringVar()
        Type = StringVar()
        FruitStrength = StringVar()
        Owner = StringVar()

# --------------------------------------FUNCTIONS-------------------------------------------------------------------

        def iExit():
            iExit = tkinter.messagebox.askyesno("Devil Fruit from One Piece Database", "Confirm if you want to exit")
            if iExit > 0:
                root.destroy()
                return

        def clearData():
            self.txtFrtNum.delete(0, END)
            self.txtNam.delete(0, END)
            self.txtTyp.delete(0, END)
            self.txtOwn.delete(0, END)
            self.txtFrtStr.delete(0, END)
            
        def addData():
            if(len(FruitNumber.get())!=0):
                backend.addFruitRec(FruitNumber.get(), Name.get(), Type.get() , Owner.get(), FruitStrength.get())
                fruitlist.delete(0, END)
                fruitlist.insert(END, (FruitNumber.get(), Name.get(), Type.get(), Owner.get(), FruitStrength.get()))

        def DisplayData():
            fruitlist.delete(0,END)
            for row in backend.viewData():
                fruitlist.insert(END, row, str(""))

        def FruitRec(event):
            searchFruit = fruitlist.curselection()[0]
            self.sd = fruitlist.get(searchFruit)

            self.txtFrtNum.delete(0, END)
            self.txtFrtNum.insert(END, sd[1])

            self.txtNam.delete(0, END)
            self.txtNam.insert(END, sd[2])

            self.txtTyp.delete(0, END)
            self.txtTyp.insert(END, sd[3])

            self.txtOwn.delete(0, END)
            self.txtOwn.insert(END, sd[4])

            self.txtFrtStr.delete(0, END)
            self.txtFrtStr.insert(END, sd[5])

        def DeleteData(sd):
            if(len(FruitNumber.get())!=0):
                backend.deleteRec(sd)
                clearData()
                DisplayData()

        def CreateWindow():
            window = tkinter.messagebox.askyesno("Wikipedia unavailable: poor internet connection", "Confirm if you want to exit")
            if window > 0:
                root.destroy()
                return

        def searchDatabase():
            fruitlist.delete(0,END)
            for row in backend.searchData(FruitNumber.get(), Name.get(), Type.get() , Owner.get(), FruitStrength.get()):
                fruitlist.insert(END, row, str(""))

        def update(sd):
            if (len(FruitNumber.get()) != 0):
#                backend.deleteRec(sd[0])
#            if (len(FruitPrice.get()) != 0):
                backend.dataUpdate(FruitNumber.get(), Name.get(), Type.get(), Owner.get(), FruitStrength.get())
#                backend.addFruitRec(Name.get(), Type.get(), Owner.get())
#                fruitlist.delete(0, END)
#                fruitlist.insert(END, (Name.get(), Type.get(), Owner.get()))

        def searchWiki():
            fruitlist.delete(0,END)
            for row in backend.searchWikiLink(Name.get(), WikiLink.get()):
                fruitlist.insert(END, row, str(""))

#--------------------------------------Frames-----------------------------------------------------------------------

        MainFrame = Frame(self.root, bg="Light Blue")
        MainFrame.grid()
        TitFrame = Frame(MainFrame, bd=10, pady=6, bg="Ghost White", relief=RIDGE)
        TitFrame.pack(side=TOP)
        self.lblTit = Label(TitFrame ,font=('roboto',48,'bold'),text="Devil Fruit from One Piece Database",bg="Ghost White")
        self.lblTit.grid()
        ButtonFrame =Frame(MainFrame,bd=2,width=1350,height=70,padx=19,pady=10,bg="Ghost White",relief =RIDGE)
        ButtonFrame.pack(side=BOTTOM)
        DataFrame = Frame(MainFrame, bd=1, width=1300, height=400, padx=20, pady=20, relief=RIDGE,bg="Light Blue")
        DataFrame.pack(side=BOTTOM)
        DataFrameLEFT = LabelFrame(DataFrame, bd=1, width=1000, height=600, padx=20,relief=RIDGE,bg="Ghost White", font=('roboto',26,'bold'),text="Fruits Info\n")
        DataFrameLEFT.pack(side=LEFT)
        DataFrameRIGHT = LabelFrame(DataFrame, bd=1, width=450, height=300, padx=31, pady=3, relief=RIDGE,bg="Ghost White",font=('roboto',20,'bold'),text="Fruits Details\n")
        DataFrameRIGHT.pack(side=RIGHT)

#--------------------------------entries-------------------------------------------------------------------------------------------------

        self.lblFrtNum = Label(DataFrameLEFT, font=('roboto', 20, 'bold'), text="Fruit number:",padx=2,pady=2,bg="Ghost White")
        self.lblFrtNum.grid(row=0,column=0,sticky=W)
        self.txtFrtNum = Entry(DataFrameLEFT, font=('roboto', 20, 'bold'), textvariable=FruitNumber, width=39)
        self.txtFrtNum.grid(row=0, column=1)

        self.lblNam = Label(DataFrameLEFT, font=('roboto', 20, 'bold'), text="Fruit Name:", padx=2, pady=2,bg="Ghost White")
        self.lblNam.grid(row=1, column=0, sticky=W)
        self.txtNam = Entry(DataFrameLEFT, font=('roboto', 20, 'bold'), textvariable=Name, width=39)
        self.txtNam.grid(row=1, column=1)

        self.lblTyp = Label(DataFrameLEFT, font=('roboto', 20, 'bold'), text="Type:", padx=2, pady=2,bg="Ghost White")
        self.lblTyp.grid(row=2, column=0, sticky=W)
        self.txtTyp = Entry(DataFrameLEFT, font=('roboto', 20, 'bold'), textvariable=Type, width=39)
        self.txtTyp.grid(row=2, column=1)

        self.lblOwn = Label(DataFrameLEFT, font=('roboto', 20, 'bold'), text="Fruit Owner:", padx=2, pady=2,bg="Ghost White")
        self.lblOwn.grid(row=3, column=0, sticky=W)
        self.txtOwn = Entry(DataFrameLEFT, font=('roboto', 20, 'bold'), textvariable=Owner, width=39)
        self.txtOwn.grid(row=3, column=1)

        self.lblFrtStr = Label(DataFrameLEFT, font=('roboto', 20, 'bold'), text="Fruit Strength:", padx=2, pady=2,bg="Ghost White")
        self.lblFrtStr.grid(row=4, column=0, sticky=W)
        self.txtFrtStr = Entry(DataFrameLEFT, font=('roboto', 20, 'bold'), textvariable=FruitStrength, width=39)
        self.txtFrtStr.grid(row=4, column=1)

#--------------------------------------scroll bar and list box----------------------------------------------------------------------------

        scrollbar= Scrollbar(DataFrameRIGHT)
        scrollbar.grid(row=0,column=1,sticky='ns')

        fruitlist = Listbox(DataFrameRIGHT, width=41, height=16, font=('roboto', 12, 'bold'),yscrollcommand=scrollbar.set)
        fruitlist.bind('<<ListboxSelect>>',FruitRec)
        fruitlist.grid(row=0, column=0, padx=8)
        scrollbar.config(command=fruitlist.yview)

#--------------------------------------buttons-----------------------------------------------------------------------------------------------------------
        self.btnWiki = Button(DataFrameLEFT, text="Wiki", font=('roboto', 20, 'bold'), height=1, width=10, bd=10, command=searchWiki)
        self.btnWiki.grid(row=5, column=0)

        self.btnAddData = Button(ButtonFrame, text="Add New", font=('roboto', 20, 'bold'), height=1, width=10, bd=4, command=addData)
        self.btnAddData.grid(row=0, column =0)

        self.btnDisplayData = Button(ButtonFrame, text="Display", font=('roboto', 20, 'bold'), height=1, width=10, bd=4, command=DisplayData)
        self.btnDisplayData.grid(row=0, column=1)

        self.btnClearData = Button(ButtonFrame, text="Clear", font=('roboto', 20, 'bold'), height=1, width=10, bd=4,command=clearData)
        self.btnClearData.grid(row=0, column=2)

        self.btnDeleteData = Button(ButtonFrame, text="Delete", font=('roboto', 20, 'bold'), height=1, width=10, bd=4,command=lambda: DeleteData(int(self.txtFrtNum.get())))
        self.btnDeleteData.grid(row=0, column=3)

        self.btnSearchData = Button(ButtonFrame, text="Search", font=('roboto', 20, 'bold'), height=1, width=10, bd=4,command=searchDatabase)
        self.btnSearchData.grid(row=0, column=4)

        self.btnUpdateData = Button(ButtonFrame, text="Update", font=('roboto', 20, 'bold'), height=1, width=10, bd=4,command=lambda: update(int(self.txtFrtNum.get())))
        self.btnUpdateData.grid(row=0, column=5)

        self.btnExit = Button(ButtonFrame, text="Exit", font=('roboto', 20, 'bold'), height=1, width=10, bd=4, command=iExit)
        self.btnExit.grid(row=0, column=6)

if __name__=='__main__':
    root = Tk()
    application = Fruit(root)
    root.mainloop()
