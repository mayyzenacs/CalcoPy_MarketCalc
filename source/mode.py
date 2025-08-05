from math import ceil
from source.history import saveHistory
from tkinter import messagebox

class Calculator():

    def __init__(self):
        '''
            set variables
        '''
        self.floatValue = 0
    
    
    def calc(self, option, value):
        '''
            catch option and value from window.py
            verify if value is none to prevent errors
            set value(entryValue) as a float
            identify the radioOption(option) and asign it with a percent
        '''
        
        try:
            priceValue = value.strip()

            self.floatValue = float(priceValue)

            if self.floatValue <= 0 or self.floatValue > 999999:
                messagebox.showerror('erro', 'valor não permitido')
                return None
            
            
            discounts = {
                0: (0.15, '15%'),
                1: (0.25, '25%'),
                2: (0.35, '35%'),
            }

            if option in discounts:
                discount, percent = discounts[option]
            else:
                messagebox.showerror('erro','Opção inválida')
    
            '''
                basic calc is how percent works in real life, outcome is a math ceil to round the result and avoid lack 0,1 cent in the operation
            '''    
            originalValue = self.floatValue / (1 - discount)

            outcome = ceil(originalValue * 100) / 100

            saveHistory(self.floatValue, outcome, percent)
            
            return outcome
        
        except:
            messagebox.showerror('erro', 'Valor inválido')
            return None

    def offer(self):
        '''
            calcule the offer price from a value, it's useful for e-commerce that uses mercado livre and participate from recurrent offers
        '''
        return self.floatValue - (self.floatValue * 0.03)


    ## CÁLCULO DO ESTOQUE FULL POR SEMANA
    def mathFull(self, fullWeeks, salesNumber): 
        '''
            calculate how many items you need to send to full (a shipment method) uses the number of items that you sold in a certain number of weeks 
        '''
            
        try:
            salesNumberInt = int(salesNumber)
            
            
            if salesNumberInt <= 0:
                messagebox.showerror('erro', 'Valor inválido para full')
                return None
                
            fullVar = int(salesNumber) * fullWeeks
            return fullVar
        
        except ValueError:
           messagebox.showerror('erro', 'Valor inválido para full')
           return None
        
            

    


    



