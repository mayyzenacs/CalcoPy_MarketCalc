
import json
import os
import pandas as pd
from datetime import datetime
from tkinter import filedialog, messagebox


APPDATA_DIR = os.getenv('LOCALAPPDATA')
HISTORY_DIR = os.path.join(APPDATA_DIR, 'CalcoPy MarketCalc')
HISTORY_FILE = os.path.join(HISTORY_DIR, 'history.json')


os.makedirs(HISTORY_DIR, exist_ok=True)


def saveHistory(precoPor, precoDe, percent):
    '''
    Saves a new calculation entry to a JSON history file.

    Args:
        precoPor (float): The input price value.
        precoDe (float): The calculated original price.
        percent (str): The discount percentage applied.
    '''
    history =  []
    
    if os.path.exists(HISTORY_FILE): 
        with open(HISTORY_FILE, 'r') as file: 
            try: 
                history = json.load(file)
            except json.JSONDecodeError:
                history = []

    if len(history) >= 50:
        history.pop(0)
                
    history.append({
        "data": datetime.now().strftime('%d/%m/%Y %H:%M'),
        "precoPor": precoPor,
        "precoDe": precoDe,
        "percent": percent
})

    with open(HISTORY_FILE, 'w') as arq: 
        json.dump(history, arq, indent=4)


def downloadHistory(): 
    '''
        Exports the calculation history to an Excel file.
    '''
    with open(HISTORY_FILE, 'r') as file:
        data = json.load(file)

    df = pd.DataFrame(data)

    fileName = f'relatório{datetime.now().strftime('%d-%m-%Y-%H-%M')}.xlsx'

    filepath = filedialog.asksaveasfilename(
        initialfile=fileName,
        filetypes=[('excel files', '*.xlsx')],
        defaultextension='.xlsx',
        title="salvar como"
    )

    if filepath:
        df.to_excel(filepath)
        messagebox.showinfo('Relatório Salvo', 'Arquivo salvo com sucesso')
    


