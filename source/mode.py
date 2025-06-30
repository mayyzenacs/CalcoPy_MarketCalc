import math
from history import saveHistory
from tkinter import messagebox

## DEFININDO CLASSE DE CÁLCULO
class Calculator():

    def __init__(self):
        self.floatValue = 0
        self.percent = 0
        self.value = 0
        self.var = 0
    
    ## FUNÇÃO QUE REALIZA O CALCULO PRINCIPAL
    def calc(self, option, value):

        if value is None or value == '':
            return ''
        
        try:
            self.floatValue = float(value)

            if option == 0: 
                discount = 1 - 0.10
                percent = "10%"

            elif option == 1:  
                discount = 1 - 0.20
                percent = "20%"

            elif option == 2:
                discount = 1 - 0.35
                percent = "35%"
                
            var = self.floatValue / discount
            outcome = math.ceil(var * 100) / 100
            saveHistory(value, outcome, percent)
            return outcome
        except:
            messagebox.showerror('erro', 'Valor inválido')
            return ''

    ## FUNÇÃO QUE CALCULO O VALOR PARA OFERTA MELI
    def offer(self):
        return self.floatValue - (self.floatValue * 0.03) 
    

    ## CÁLCULO DO ESTOQUE FULL POR SEMANA
    def mathFull(self, fullOption, fullWeeks): 
        if fullWeeks == '':
            return ''
        

        try:
            fullVar = int(fullOption) * int(fullWeeks)
            print(fullOption, fullWeeks)
            return(fullVar)
        
        except ValueError:
           messagebox.showerror('erro', 'Valor inválido')
           return ''
        
            

    


    



