from tkinter import *

def result():
     Out_of_Value_of_Marks = Out_of_Value.get()
     English_Marks = Eng.get()
     Hindi_Marks = Hin.get()
     Maths_Marks = Maths.get()
     Science_Marks = Science.get()
     SST_Marks = SST.get()
     French_Marks = French.get()

     Total = English_Marks + Hindi_Marks + Maths_Marks + Science_Marks + SST_Marks + French_Marks
     result = Total / (Out_of_Value_of_Marks*6) * 100

     Result_Widget.delete('1.0', END)
     Result_Widget.insert('1.0', f"Percentage: {result}")
     


if __name__ == "__main__":
     root = Tk()
     root.geometry('600x650')
     root['bg'] = '#29bb89'
     root.title("Percentage Finder")

     fontScheme = ['Arial Nova', 15]
     bgScheme = '#29bb89'
     boxBgScheme = '#abedd6'

     Label(root, text="Maximum Marks", font=fontScheme, bg=bgScheme).place(x=235, y=30)

     Out_of_Value = DoubleVar()
     Out_of_ValueW = Entry(root, width=30, textvariable=Out_of_Value, font=fontScheme, bg=boxBgScheme)
     Out_of_ValueW.place(x=150, y=60)

     Eng = DoubleVar()
     Hin = DoubleVar()
     Maths = DoubleVar()
     Science = DoubleVar()
     SST = DoubleVar()
     French = DoubleVar()

     Label(root, text="English:  ", font=fontScheme, bg=bgScheme).place(x=185-20, y=100)
     EngW = Entry(root, width=20, textvariable=Eng, font=fontScheme, bg=boxBgScheme)
     EngW.place(x=250, y=100)

     Label(root, text="Hindi:  ", font=fontScheme, bg=bgScheme).place(x=185-20, y=135)
     HinW = Entry(root, width=20, textvariable=Hin, font=fontScheme, bg=boxBgScheme)
     HinW.place(x=250, y=135)

     Label(root, text="Maths:  ", font=fontScheme, bg=bgScheme).place(x=185-20, y=160+10)
     MathW = Entry(root, width=20, textvariable=Maths, font=fontScheme, bg=boxBgScheme)
     MathW.place(x=250, y=160+10)

     Label(root, text="Science:  ", font=fontScheme, bg=bgScheme).place(x=185-20, y=170+35)
     ScienceW = Entry(root, width=20, textvariable=Science, font=fontScheme, bg=boxBgScheme)
     ScienceW.place(x=250, y=170+35)

     Label(root, text="SST:  ", font=fontScheme, bg=bgScheme).place(x=185-20, y=170+35+35)
     SSTW = Entry(root, width=20, textvariable=SST, font=fontScheme, bg=boxBgScheme)
     SSTW.place(x=250, y=170+35+40)

     Label(root, text="French:  ", font=fontScheme, bg=bgScheme).place(x=185-20, y=170+35+35+35)
     FrenchW = Entry(root, width=20, textvariable=French, font=fontScheme, bg=boxBgScheme)
     FrenchW.place(x=250, y=170+35+35+35+10)


     Submit = Button(root, text="Submit", bg='#20926a', padx=15, pady=15, font=fontScheme, activebackground='#289672', command=result)
     Submit.place(x=280-20,y=250+75)

     Result_Widget = Text(root, bg=boxBgScheme, width=35, height=5, font=fontScheme)
     Result_Widget.place(x=107,y=250+90+70)
     Result_Widget.tag_configure("center", justify='center')
     Result_Widget.tag_add("center", 1.0, "end")

     root.mainloop()