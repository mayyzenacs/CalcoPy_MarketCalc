from math import ceil
from source.history import saveHistory
from tkinter import messagebox


class Calculator():
    '''
        Performs various calculations related to e-commerce pricing and stock management.
    '''

    def __init__(self):
        '''
            set variables
        '''
        self.floatValue = 0
    
    
    def calc(self, option, value):
        '''
            Calculates the original price based on a user-selected discount.

            Args:
                option (int): The selected discount option (0, 1, or 2).
                value (str): The price input from the user.

            Returns:
                float: The calculated original price, or None on error.
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
                Reverse the discount calculation to find the original price
                Round the result up to two decimal places to avoid cents loss.
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
            Calculates an offer price by applying a 3% discount to the current value.
        '''
        return self.floatValue - (self.floatValue * 0.03)


    ## CÁLCULO DO ESTOQUE FULL POR SEMANA
    def mathFull(self, fullWeeks, salesNumber): 
        '''
            Calculates the number of items to send to the 'Full' center.
            Args:
            fullWeeks (int): The number of weeks for the stock calculation.
            salesNumber (str): The number of items sold in the last 7 days.
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
        
            

    


    



