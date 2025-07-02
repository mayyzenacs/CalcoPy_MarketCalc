import math
from history import saveHistory
from tkinter import messagebox

class Calculator():

    def __init__(self):
        '''
            set variables
        '''
        self.floatValue = 0
        self.percent = 0
        self.value = 0
        self.var = 0
    
    def calc(self, option, value):
        '''
            catch option and value from window.py
            verify if value is none to prevent errors
            set value(entryValue) as a float
            identify the radioOption(option) and asign it with a percent
        '''

        if value is None or value == '':
            return ''
        
        try:
            self.floatValue = float(value)

            if option == 0: 
                discount = 1 - 0.15
                percent = "15%"

            elif option == 1:  
                discount = 1 - 0.20
                percent = "20%"

            elif option == 2:
                discount = 1 - 0.35
                percent = "35%"
                
            '''
                basic calc is how percent works in real life, outcome is a math ceil to round the result and avoid lack 0,1 cent in the operation
            '''    
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
            return(fullVar)
        
        except ValueError:
           messagebox.showerror('erro', 'Valor inválido')
           return ''
        
            

    


    



