from mode import Calculator
import json
import os
import pandas as pd
from datetime import datetime
from tkinter import filedialog, messagebox


def saveHistory(precoPor, PrecoDe, Percent):
    history =  []

    if os.path.exists('history.json'): 
        with open('history.json', 'r') as archive: 
            try: 
                history = json.load(archive)
            except:
                history = []
                
    history.append({
        "data": datetime.now().strftime('%d/%m/%Y %H:%M'),
        "precoPor": precoPor,
        "precoDe": PrecoDe,
        "percent": Percent
})

    with open('history.json', 'w') as arq: 
        json.dump(history, arq, indent=4)


    def downloadHistory(): 
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
        

saveHistory(45.45, 56.56, '35%')