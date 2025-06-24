
import json
import os
import pandas as pd
from datetime import datetime
from tkinter import filedialog, messagebox


def saveHistory(precoPor, precoDe, percent):
    history =  []

    if os.path.exists('history.json'): 
        with open('history.json', 'r') as archive: 
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

    with open('history.json', 'w') as arq: 
        json.dump(history, arq, indent=4)


def savefromHistory(): 
    with open('history.json', 'r') as file:
        data = json.load(file)

    df = pd.DataFrame(data)

    filepath = filedialog.asksaveasfilename(
        filetypes=[('Excel files', '*.xlsx')],
        defaultextension='.xlsx',
        title="salvar como"
    )

    if filepath:
        df.to_excel(filepath)
        messagebox.Message('Arquivo salvo com sucesso')
    else: 
        pass
    


