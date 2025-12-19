import tkinter as tk
from src.math_mode import Calculator
from src.history import download_archive
from tkinter import PhotoImage
from PIL import Image, ImageTk
import sys
import os

'''
    Gets the absolute path to a resource, working for both
    development and bundled PyInstaller executables.
'''
def resourcePath(relative):
    try:
        base = sys._MEIPASS
    except Exception:
        base = os.path.abspath('.')
    return os.path.join(base, relative)
    

'''
    initial class and functions calls
'''
class Apliccation(): 
    '''
        Main class 
        This class handles the creation and management of the Tkinter GUI,
        including widgets, layouts, and event handling.
    '''
    def __init__(self):
        self.root = tk.Tk()
        self.priceResult = tk.StringVar()
        self.placeFullResult = tk.StringVar()
        self.valueOffer = tk.StringVar()
        
        self.fullChoice = tk.IntVar()
        self.radioChoice = tk.IntVar()

        
        self.calc_class = Calculator()
        self.main_frame()
        self.buttons_calc_main_frame()
        self.calc_result_frame()
        self.del_button()
        self.copy_button()
        self.copy_label()
        self.offer_label()
        self.full_layout()
        self.save_as()
    

    def main_frame(self):

        self.root.configure(background= "#363636")
        self.root.geometry("480x450")
        self.root.resizable(False, False)

        logoPath = resourcePath('src/img/logo.png')
        self.bgImage = Image.open(logoPath)
        self.resizedImage = self.bgImage.resize((456,120))
        self.imageB = ImageTk.PhotoImage(self.resizedImage)
        self.bgImageLabel = tk.Label(self.root, image=self.imageB, bd=0, bg="#000000")
        self.bgImageLabel.place(relx=0.5, rely=0, anchor='n')

        iconPath = resourcePath('src/img/icon.png')
        self.img = tk.PhotoImage(file=iconPath, master=self.root)
        self.root.iconphoto(False, self.img)

        self.frameBack = tk.Frame(self.root, relief="solid", bg="#4F4F4F")
        self.frameBack.place(relx=0.5, rely=0.59, relheight= 0.78,relwidth=0.95, anchor=tk.CENTER)

        '''
            tittles and strings from main frame
        '''
        self.root.title("CalcoPy MarketCalc by Mayra Pereira")

        self.str = tk.Label(self.frameBack, text="CalcoPy MarketCalc Calculadora | Preço Comercial e Estoque",bg="#4F4F4F", font=("verdana", 9, "bold"))
        self.str.place(relheight=0.09, relwidth=1, relx=0.5, rely=0.037, anchor=tk.CENTER)

        self.choice = tk.Label(self.frameBack, text="Selecione qual porcentagem utilizar", bg="#4F4F4F", font=("Verdana", 11, "bold"))
        self.choice.place(relheight=0.08, relwidth=1, relx=0.5, rely=0.10, anchor=tk.CENTER)


    def buttons_calc_main_frame(self): 
        '''
            Sets up the primary widgets for the main calculation frame.

            This includes the radio buttons for discount options, 
            the price input field, and the main 'Calculate' button.
        ''' 
        discountOptions = [
            ('15%', 0, 0.19),
            ('25%', 1, 0.5),
            ('35%', 2, 0.8)
        ]

        for text, option, relxps in discountOptions:
            self.check = tk.Radiobutton(
                            self.frameBack, 
                            text=text, 
                            variable=self.radioChoice, 
                            value=option, 
                            bd=0, 
                            highlightthickness=0, 
                            bg="#4F4F4F", 
                            activebackground="#4F4F4F", 
                            font=("verdana",14,"bold"),
                            )
            self.check.place(relheight= 0.12, relwidth=0.22, relx=relxps, rely=0.19, anchor=tk.CENTER)
            
        self.entryText = tk.Label(self.frameBack, text="Preço Por", bg="#4F4F4F", font=("Verdana", 15, "bold"))
        self.entryText.place(relheight=0.09, relwidth=1, relx=0.38, rely=0.28, anchor=tk.CENTER)

        self.calcBt = tk.Button(self.frameBack, text="Calcular", bg="#DCDCDC", bd=0, command=self.taking_entries, font=("verdana", 11, "bold", 'italic'), justify='center')
        self.calcBt.place(relx=0.052, rely=0.33, relheight=0.12, relwidth=0.16)
        
        self.entryCalc = tk.Entry(self.frameBack,bd=0, font=("verdana", 20, "bold"), justify="center")
        self.entryCalc.place(relheight= 0.12 ,relwidth=0.30, relx=0.24, rely=0.33)
        self.entryCalc.icursor(0)
        self.entryCalc.bind("<Return>", lambda event: self.taking_entries())


    def calc_result_frame(self): 
        '''
            getting the result to show in the frame
        '''
        label = tk.Label(self.frameBack, textvariable='PREÇO DE', relief=tk.RAISED, bg="#4F4F4F",font=("verdana", 15, "bold"),bd = 0)
        label.place(relx=0.54, rely=0.45, relheight= 0.1 ,relwidth=0.31, anchor='ne')

        self.labelReturn = tk.Label(self.frameBack, textvariable = self.priceResult, font=("verdana", 21, "bold"), fg='blue')
        self.labelReturn.place(relx=0.24, rely=0.55, relheight=0.14, relwidth=0.30)        


    '''
        collecting entries
    '''
    def taking_entries(self):
        '''
            Handles the calculation process when the main button is clicked or 'Enter' is pressed.
        '''
        radioOption = self.radioChoice.get()
        entryValueCalc = self.entryCalc.get().replace(",",".") 

        result = self.calc_class.calc(radioOption, entryValueCalc)
        '''
            check if result isn't none to set specify values and call offer
        '''
        if result is not None: 
            offerPrice = self.calc_class.offer()
            self.valueOffer.set(f"{offerPrice:.2f}")
            self.priceResult.set(result)
        else:
            self.valueOffer.set('')
            self.priceResult.set('')

    
    def offer_label(self):
        '''
            offer label to make calc to set a offer -3%
        '''
        self.offerText = tk.Label(self.frameBack, text="Oferta -3%", bg="#4F4F4F", font=("Verdana", 12, "bold"))
        self.offerText.place(relx=0.26, rely=0.73, relwidth=0.28, relheight=0.06, anchor="w")

        self.offerReturn = tk.Label(self.frameBack, textvariable= self.valueOffer, font=("Verdana", 12, "bold"))
        self.offerReturn.place(relx=0.24, rely=0.81, relwidth=0.30, relheight=0.07, anchor="w")


    '''
        all the full label interface below
    '''
    def full_layout(self): 

        '''
            strings from full label
        '''
        self.fullText = tk.Label(self.frameBack, text="Semanas", bg="#4F4F4F", font=("Verdana", 11, "bold"))
        self.fullText.place(relx=0.65, rely=0.28, relwidth=0.24, relheight=0.07, anchor="w")

        self.fullChoice.set(6)

        self.fullTextWeek = tk.Label(self.frameBack, text="Vendas 7 dias", bg="#4F4F4F", font=("verdana", 10, "bold"))
        self.fullTextWeek.place(relx=0.62, rely=0.44, relwidth=0.31, relheight=0.07, anchor="w")

        self.fullTextResult = tk.Label(self.frameBack, text="Qtd. a enviar", bg="#4F4F4F", font=("verdana", 10, "bold"))
        self.fullTextResult.place(relx=0.62, rely=0.60, relwidth=0.31, relheight=0.07, anchor="w")

        fullOptionsWeek = [
            ('5', 5, 0.64),
            ('6', 6, 0.77),
            ('8', 8, 0.89)
        ]
        
        for text, week, relxps in fullOptionsWeek: 
            self.fullOption = tk.Radiobutton(
                            self.frameBack, 
                            text=text, 
                            variable=self.fullChoice, 
                            value=week, 
                            bd=0, 
                            highlightthickness=0, 
                            bg="#4F4F4F", 
                            activebackground="#4F4F4F", 
                            font=("verdana",12,"bold"),
                            )
            self.fullOption.place(relheight=0.09, relwidth=0.1, relx=relxps, rely=0.37, anchor=tk.CENTER)

        '''
            defining calc full week button and others label
        '''
        self.entryFullWeek = tk.Entry(self.frameBack, bd=0, font=("verdana", 15, "bold"), justify="center", fg='green')
        self.entryFullWeek.place(relheight= 0.089 ,relwidth=0.19, relx=0.77, rely=0.52, anchor=tk.CENTER)

        self.entryFullWeek.bind("<Return>", lambda event: self.full_Calc())

        self.calcBtFull = tk.Button(self.frameBack, text="Full", bg="#DCDCDC", bd=0, command=self.full_Calc, font=("verdana", 12, "bold", 'italic'), justify='center')
        self.calcBtFull.place(relx=0.706, rely=0.76, relheight=0.09, relwidth=0.13)

        self.fullResult = tk.Label(self.frameBack, textvariable= self.placeFullResult, font=("verdana", 15, "bold"), fg="blue")
        self.fullResult.place(relheight= 0.089 ,relwidth=0.19, relx=0.77, rely=0.68, anchor=tk.CENTER)


    def full_Calc(self):
        '''
            getting values to calc full valuess
        '''
        getFullChoice = self.fullChoice.get()
        weekEntry = self.entryFullWeek.get()

<<<<<<< HEAD:source/window.py
        fullResult = self.classCalc.mathFull(getFullChoice, weekEntry)
        if fullResult is not None:
            self.placefullResult.set(fullResult)
        else:
            self.placefullResult.set('')
=======
        fullResult = self.calc_class.mathFull(getFullChoice, weekEntry)
        if fullResult is not None:
            self.placeFullResult.set(fullResult)
        else:
            self.placeFullResult.set('')
>>>>>>> refactor:src/interface.py


    def copy_button(self):
        '''
            Copies the current price result to the clipboard.
            This method retrieves the value from the price result variable,
            copies it to the system clipboard, and displays a temporary confirmation message to the user.
        '''
        copy = self.priceResult.get()
        if copy: 
            self.root.clipboard_clear()
            self.root.clipboard_append(copy)
            self.copyMsg.config(text="Valor copiado")
            self.root.after(1000, lambda: self.copyMsg.config(text=""))


    def copy_label(self):
        '''
            Sets up copy label
        '''
        self.copyBt = tk.Button(self.frameBack, text="Copiar", bg="#DCDCDC", bd=0, command= self.copy_button, font=("verdana", 11, "italic", 'bold'))
        self.copyBt.place(relx=0.054, rely=0.56, relheight=0.12, relwidth=0.16)

        self.copyMsg = tk.Label(self.frameBack, text="", bg="#4F4F4F", font=("verdana", 8, 'italic'))
        self.copyMsg.place(relx=0.01, rely=0.69, relheight=0.05, relwidth=0.25)


    def save_as(self): 
        '''
            Sets up the 'Export' button to allow saving the calculation history.
        '''
        self.saveButton = tk.Button(self.frameBack,text="export", bg="#4F4F4F", bd=1, command= download_archive, font=("verdana", 8, "italic", 'bold'))
        self.saveButton.place(relheight=0.07, relwidth=0.11,relx=0.5, rely=0.94, anchor=tk.CENTER)
    

    def clear(self):
        '''
            Clears all input fields and resets the result labels.
        '''
        self.entryCalc.delete(0, tk.END)
        self.valueOffer.set('')
        self.priceResult.set('')
        self.placeFullResult.set('')
        self.entryFullWeek.delete(0, tk.END)


    def del_button(self):
        '''
            Sets up 'clear' button to clean labels
        '''
        self.del_bt = tk.Button(self.frameBack, text="Clear", bd=1, bg="#4F4F4F", command= self.clear, font=("verdana", 10, "italic", 'bold'))
        self.del_bt.place(relheight=0.08, relwidth=0.10,relx=0.085, rely=0.76)

        
if __name__ == "__main__":
    app = Apliccation()
    app.root.mainloop()

    
