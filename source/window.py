import tkinter as tk
from mode import Calculator
from tkinter import PhotoImage
from PIL import Image, ImageTk
from history import savefromHistory

'''
    initial class and functions calls
'''
class Apliccation(): 
    def __init__(self):
        self.root = root
        self.classCalc = Calculator()
        self.screen()
        self.frame()
        self.buttons()
        self.delButton()
        self.checkbutton()
        self.label()
        self.entry()
        self.take()
        self.copyButton()
        self.copyText()
        self.offerLabel()
        self.logo()
        self.radiosFull()
        self.fullCalc()
        self.saveAs()
    

    '''
        backscreen
    '''
    def screen(self):

        self.root.title("CalcoPy MarketCalc by Mayra Pereira")
        self.root.configure(background= "#363636")
        self.root.geometry("480x450")
        self.root.resizable(False, False)

    '''
        set images
    '''
    def logo(self):

        self.bgImage = Image.open('source\img\logo.png')
        self.resizedImage = self.bgImage.resize((500,180))
        self.imageB = ImageTk.PhotoImage(self.resizedImage)

        self.img = PhotoImage(file='source\img\icon.png')
        self.root.iconphoto(False, self.img)
        
        self.bgImageLabel = tk.Label(self.root, image=self.imageB, bd=0, bg="#000000")
        self.bgImageLabel.place(relheight=0.21, relwidth=1, anchor=tk.CENTER, relx=0.5, rely=0.1)


    def frame(self):

        self.frameBack = tk.Frame(self.root, relief="solid", bg="#4F4F4F")
        self.frameBack.place(relx=0.5, rely=0.59, relheight= 0.78,relwidth=0.95, anchor=tk.CENTER)

        self.str = tk.Label(
                        self.frameBack, 
                        text="CalcoPy MarketCalc Calculadora | Preço Comercial e Estoque", 
                        bg="#4F4F4F", 
                        font=("verdana", 9, "bold")
                        )
        self.str.place(relheight=0.09, relwidth=1, relx=0.5, rely=0.037, anchor=tk.CENTER)
       

    def checkbutton(self): 

        self.choice = tk.Label(self.frameBack, text="Selecione qual porcentagem utilizar", bg="#4F4F4F", font=("Verdana", 11, "bold"))
        self.choice.place(relheight=0.08, relwidth=1, relx=0.5, rely=0.10, anchor=tk.CENTER)

        self.radioChoice = tk.IntVar()
        self.check = tk.Radiobutton(
                        self.frameBack, 
                        text="15%", 
                        variable=self.radioChoice, 
                        value=0, 
                        bd=0, 
                        highlightthickness=0, 
                        bg="#4F4F4F", 
                        activebackground="#4F4F4F", 
                        font=("verdana",14,"bold"),
                        )
        self.check2 = tk.Radiobutton(
                        self.frameBack, 
                        text="20%", 
                        variable=self.radioChoice, 
                        value=1, 
                        bd=0, 
                        highlightthickness=0, 
                        bg="#4F4F4F", 
                        activebackground="#4F4F4F", 
                        font=("verdana",14,"bold")
                        )
        self.check3 = tk.Radiobutton(
                        self.frameBack, 
                        text="35%", 
                        variable=self.radioChoice, 
                        value=2, 
                        bd=0, 
                        highlightthickness=0, 
                        bg="#4F4F4F", 
                        activebackground="#4F4F4F", 
                        font=("verdana",14,"bold")
                        )
        self.check.place(relheight= 0.12, relwidth=0.22, relx=0.18, rely=0.19, anchor=tk.CENTER)
        self.check2.place(relheight= 0.12, relwidth=0.22, relx=0.5, rely=0.19, anchor=tk.CENTER)
        self.check3.place(relheight= 0.12, relwidth=0.22, relx=0.7, rely=0.19, anchor='w')


    def entry(self):

        self.entryCalc = tk.Entry(
                        self.frameBack, 
                        bd=0, 
                        font=("verdana", 20, "bold"), justify="center"
                        )
        self.entryCalc.icursor(0)
        self.entryCalc.place(relheight= 0.12 ,relwidth=0.30, relx=0.24, rely=0.33)
        
        self.entryCalc.bind("<Return>", lambda event: self.take())

        self.entryText = tk.Label(self.frameBack, text="Preço Por", bg="#4F4F4F", font=("Verdana", 15, "bold"))
        self.entryText.place(relheight=0.09, relwidth=1, relx=0.38, rely=0.28, anchor=tk.CENTER)


    '''
        collecting entries
    '''
    def take(self):
        '''
            'radioOption' get the radio choice
            'entryValue' get the first entry 'precoPor'
            'returnResult' call class Calculator to pass the values and return the result from module mode.py
        '''
        radioOption = self.radioChoice.get()
        entryValue = self.entryCalc.get().replace(",",".")   
        self.returnResult = self.classCalc.calc(radioOption, entryValue)

        self.offerLabel()

        '''
            result set the return of 'returnResult' to be shown
        '''
        self.result = tk.StringVar()
        self.result.set(self.returnResult)
        self.labelReturn = tk.Label(self.frameBack, textvariable = self.result, font=("verdana", 21, "bold"), fg='blue')
        self.labelReturn.place(relx=0.24, rely=0.55, relheight=0.14, relwidth=0.30)        
        

    '''
        just the basic functionality of the 'calcular' button
    '''
    def buttons(self):
        self.calcBt = tk.Button(self.frameBack, text="Calcular", bg="#DCDCDC", bd=0, command=self.take, font=("verdana", 11, "bold", 'italic'), justify='center')
        self.calcBt.place(relx=0.052, rely=0.33, relheight=0.12, relwidth=0.16)


    def label(self): 

        var = tk.StringVar()
        label = tk.Label(
                        self.frameBack, 
                        textvariable=var,
                        relief=tk.RAISED, 
                        bg="#4F4F4F",
                        font=("verdana", 15, "bold"),
                        bd = 0
                    )
        var.set("PREÇO DE")
        label.place(relx=0.54, rely=0.45, relheight= 0.1 ,relwidth=0.31, anchor='ne')


    def offerLabel(self):

        self.offerText = tk.Label(self.frameBack, text="Oferta -3%", bg="#4F4F4F", font=("Verdana", 12, "bold"))
        self.offerText.place(relx=0.26, rely=0.73, relwidth=0.28, relheight=0.06, anchor="w")

        self.valueOffer = tk.StringVar()
        self.valueOffer.set(f"{self.classCalc.offer():.2f}")
        self.offerReturn = tk.Label(self.frameBack, textvariable=self.valueOffer, font=("Verdana", 12, "bold"))
        self.offerReturn.place(relx=0.24, rely=0.81, relwidth=0.30, relheight=0.07, anchor="w")


    '''
        all the full label interface below
    '''
    def radiosFull(self): 

        self.fullText = tk.Label(
                        self.frameBack, 
                        text="Semanas", 
                        bg="#4F4F4F", 
                        font=("Verdana", 11, "bold")
                        )
        self.fullText.place(relx=0.65, rely=0.28, relwidth=0.24, relheight=0.07, anchor="w")
        
        self.fullChoice = tk.IntVar()
        self.fullChoice.set(6)
        self.placefullResult = tk.StringVar()
        
        self.fullOption = tk.Radiobutton(
                        self.frameBack, 
                        text="5", 
                        variable=self.fullChoice, 
                        value=5, 
                        bd=0, 
                        highlightthickness=0, 
                        bg="#4F4F4F", 
                        activebackground="#4F4F4F", 
                        font=("verdana",12,"bold"),
                        )
        self.fullOption.place(relheight=0.09, relwidth=0.1, relx=0.64, rely=0.37, anchor=tk.CENTER)

        self.fullOption2 = tk.Radiobutton(
                        self.frameBack, 
                        text="6", 
                        variable=self.fullChoice, 
                        value=6, 
                        bd=0, 
                        highlightthickness=0, 
                        bg="#4F4F4F", 
                        activebackground="#4F4F4F", 
                        font=("verdana",12,"bold"),
                        )
        self.fullOption2.place(relheight=0.09, relwidth=0.1, relx=0.77, rely=0.37, anchor=tk.CENTER)

        self.fullOption3 = tk.Radiobutton(
                        self.frameBack, 
                        text="8", 
                        variable=self.fullChoice, 
                        value=8, 
                        bd=0, 
                        highlightthickness=0, 
                        bg="#4F4F4F", 
                        activebackground="#4F4F4F", 
                        font=("verdana",12,"bold"),
                        )
        self.fullOption3.place(relheight=0.09, relwidth=0.1, relx=0.89, rely=0.37, anchor=tk.CENTER)

        self.fullTextWeek = tk.Label(
                        self.frameBack, 
                        text="Vendas 7 dias", 
                        bg="#4F4F4F", 
                        font=("verdana", 10, "bold")
                        )
        self.fullTextWeek.place(relx=0.62, rely=0.44, relwidth=0.31, relheight=0.07, anchor="w")

        self.fullTextResult = tk.Label(
                        self.frameBack, 
                        text="Qtd. a enviar", 
                        bg="#4F4F4F", 
                        font=("verdana", 10, "bold")
                        )
        self.fullTextResult.place(relx=0.62, rely=0.60, relwidth=0.31, relheight=0.07, anchor="w")

        self.entryFullWeek = tk.Entry(
                        self.frameBack, 
                        bd=0, 
                        font=("verdana", 15, "bold"), justify="center", fg='green'
                        )
        self.entryFullWeek.place(relheight= 0.089 ,relwidth=0.19, relx=0.77, rely=0.52, anchor=tk.CENTER)

        self.entryFullWeek.bind("<Return>", lambda event: self.fullCalc())

        self.calcBt = tk.Button(self.frameBack, text="Full", bg="#DCDCDC", bd=0, command=self.fullCalc, font=("verdana", 12, "bold", 'italic'), justify='center')
        self.calcBt.place(relx=0.706, rely=0.76, relheight=0.09, relwidth=0.13)


    def fullCalc(self):
        
        getFullChoice = self.fullChoice.get()
        weekEntry = self.entryFullWeek.get()
        
        self.placefullResult.set(self.classCalc.mathFull(getFullChoice, weekEntry))
        self.fullResult = tk.Label(self.frameBack, textvariable= self.placefullResult, font=("verdana", 15, "bold"), fg="blue")
        self.fullResult.place(relheight= 0.089 ,relwidth=0.19, relx=0.77, rely=0.68, anchor=tk.CENTER)


    def copyButton(self):

        copy = self.returnResult
        self.root.clipboard_clear()
        self.root.clipboard_append(copy)


    def copyText(self):

        self.copyBt = tk.Button(self.frameBack, text="Copiar", bg="#DCDCDC", bd=0, command= self.copyButton, font=("verdana", 11, "italic", 'bold'))
        self.copyBt.place(relx=0.054, rely=0.56, relheight=0.12, relwidth=0.16)

        self.copyMsg = tk.Label(self.frameBack, text="", bg="#4F4F4F", font=("verdana", 8, 'italic'))
        self.copyMsg.place(relx=0.01, rely=0.69, relheight=0.05, relwidth=0.25)

        self.copyBt.bind("<Button-1>", lambda arg: self.copyMsg.config(text="preço de copiado"))
        self.copyBt.bind("<ButtonRelease-1>", lambda arg: self.root.after(1000, lambda: self.copyMsg.config(text="")))


    def saveAs(self): 

        self.saveButton = tk.Button(self.frameBack,text="export", bg="#4F4F4F", bd=1, command= savefromHistory, font=("verdana", 8, "italic", 'bold'))
        self.saveButton.place(relheight=0.07, relwidth=0.11,relx=0.5, rely=0.94, anchor=tk.CENTER)
    

    def delButton(self):
        
        self.del_bt = tk.Button(
                        self.frameBack, 
                        text="Clear", 
                        bd=1, 
                        bg="#4F4F4F",
                        command= self.clear,
                        font=("verdana", 10, "italic", 'bold')
                        )
        self.del_bt.place(relheight=0.08, relwidth=0.10,relx=0.085, rely=0.76)


    def clear(self):

        self.entryCalc.delete(0, tk.END)
        self.valueOffer.set('')
        self.result.set('')
        self.placefullResult.set('')
        self.entryFullWeek.delete(0, tk.END)
        
        
if __name__ == "__main__":
    root = tk.Tk()
    app = Apliccation()
    root.mainloop()

    
