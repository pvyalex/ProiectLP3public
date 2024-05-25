import tkinter as tk
from tkinter import ttk
import pandas as pd


date = {
    "key1": ["keyword1", "keyword2", "keyword3"],
    "key2": ["keyword4", "keyword5"],
    "key3": ["keyword6", "keyword7", "keyword8", "keyword9", "keyword10"]
}



def afiseaza_tabel():

    max_lungime_keywords = max(len(keywords) for keywords in date.values())


    dataframe = pd.DataFrame.from_dict(date, orient='index')


    for widget in frame_tabel.winfo_children():
        widget.destroy()


    tree = ttk.Treeview(frame_tabel)
    tree = ttk.Treeview(frame_tabel)
    a = []
    lungime_maxima = 0

    for lista in date.values():
        lungime_lista = len(lista)
        if lungime_lista > lungime_maxima:
            lungime_maxima = lungime_lista

    for i in range(lungime_maxima):
        a.append(str(i))

    tree["columns"] = a
    # Configurăm coloanele
    tree.column("#0", width=100, minwidth=100, anchor=tk.W)
    for col in tree["columns"]:
        tree.column(col, width=100, minwidth=100, anchor=tk.W)
        tree.heading(col, text="Keyword", anchor=tk.W)
    for key, values in dataframe.iterrows():
        tree.insert("", "end", text=key, values=tuple(values))
    # Adăugăm datele în Treeview
    for key, values in dataframe.iterrows():
        tree.insert("", "end", text=key, values=tuple(values))

    tree.pack(expand=True, fill=tk.BOTH)



root = tk.Tk()
root.title("Interfață grafică")
root.geometry("600x300")


frame_tabel = ttk.Frame(root)
frame_tabel.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=10, pady=10)


button_tabel = ttk.Button(root, text="Afișează tabel", command=afiseaza_tabel)
button_tabel.pack(side=tk.LEFT, padx=10, pady=10)


root.mainloop()
