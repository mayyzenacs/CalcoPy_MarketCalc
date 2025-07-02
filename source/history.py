
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
    history =  []

    if os.path.exists(HISTORY_FILE): 
        with open(HISTORY_FILE, 'r') as archive: 
            try: 
                history = json.load(archive)
            except:
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


def savefromHistory(): 
    with open(HISTORY_FILE, 'r') as file:
        data = json.load(file)

    df = pd.DataFrame(data)

    filepath = filedialog.asksaveasfilename(
        filetypes=[('Excel files', '*.xlsx')],
        defaultextension='.xlsx',
        title="salvar como"
    )

    if filepath:
        df.to_excel(filepath)
        messagebox.showinfo('Sucesso', f'Arquivo salvo com sucesso em {filepath}')
    


