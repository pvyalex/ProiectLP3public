import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import pandas as pd
import requests
import time
import multidict as multidict
from wordcloud import WordCloud

# Lista universităților
lista_universitatii = ["upb.ro", "utcb.ro", "uauim.ro", "usamv.ro"]
new_data = {}

# Obținerea datelor de la API
for universitate in lista_universitatii:
    url = "https://api.builtwith.com/kw2/api.json"
    params = {
        'KEY': 'cee7f3bb-87a7-4add-acac-0ab4733e3172',
        'LOOKUP': universitate
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        domain = data['Keywords'][0]['Domain']
        keywords = data['Keywords'][0]['Keywords']
        new_data[domain] = keywords

        with open("../rezultate.txt", "a") as fisier_in:
            for i in keywords:
                fisier_in.write(i + " ")
    except requests.exceptions.HTTPError as err:
        print(f"HTTP error occurred: {err}")
    except Exc
        print(f"Other error occurred: {err}")
    time.sleep(1)

# Funcție pentru aparițiile cuvintelor cheie
def aparitii_keywords(dictionar_siteuri):
    rezultat = {}
    for site, keywords_list in dictionar_siteuri.items():
        for keyword in keywords_list:
            if keyword in rezultat:
                rezultat[keyword] += 1
            else:
                rezultat[keyword] = 1
    return rezultat

newest_data = aparitii_keywords(new_data)

# Funcție pentru frecvența cuvintelor
def getFrequencyDictForText(sentence):
    fullTermsDict = multidict.MultiDict()
    tmpDict = {}
    for text in sentence.split(" "):
        val = tmpDict.get(text, 0)
        tmpDict[text.lower()] = val + 1
    for key in tmpDict:
        fullTermsDict.add(key, tmpDict[key])
    return fullTermsDict

# Funcție pentru crearea imaginii word cloud
def makeImage(text):
    wc = WordCloud(background_color="white", max_words=10000)
    wc.generate_from_frequencies(text)
    wc.to_file("wordcloud.png")

# Funcție pentru afișarea word cloud-ului
def afiseaza_wordcloud():
    image_file = "../wordcloud.png"
    image = Image.open(image_file)
    image.thumbnail((800, 800))
    photo = ImageTk.PhotoImage(image)
    canvas_wordcloud.create_image(0, 0, anchor='nw', image=photo)
    canvas_wordcloud.image = photo

# Funcție pentru generarea și afișarea word cloud-ului
def on_generate_button_click():
    global wordcloud_displayed, tabel_displayed
    if wordcloud_displayed:
        canvas_wordcloud.pack_forget()
        wordcloud_displayed = False
    else:
        text = open('../rezultate.txt', encoding='utf-8').read()
        makeImage(getFrequencyDictForText(text))
        afiseaza_wordcloud()
        canvas_wordcloud.pack(expand=True, fill=tk.BOTH)
        wordcloud_displayed = True
        tabel_displayed = False
        for widget in frame_tabel.winfo_children():
            widget.destroy()

# Funcție pentru afișarea tabelului
def afiseaza_tabel():
    global tabel_displayed, wordcloud_displayed
    if tabel_displayed:
        for widget in frame_tabel.winfo_children():
            widget.destroy()
        tabel_displayed = False
    else:
        # Adăugarea unui Canvas pentru a permite scroll-ul
        canvas_tabel = tk.Canvas(frame_tabel)
        scrollbar_x = ttk.Scrollbar(frame_tabel, orient=tk.HORIZONTAL, command=canvas_tabel.xview)
        canvas_tabel.configure(xscrollcommand=scrollbar_x.set)
        frame_tabel_content = ttk.Frame(canvas_tabel)

        # Crearea tabelului
        dataframe = pd.DataFrame.from_dict(new_data, orient='index')
        tree = ttk.Treeview(frame_tabel_content)
        a = []
        lungime_maxima = 0
        for lista in new_data.values():
            lungime_lista = len(lista)
            if lungime_lista > lungime_maxima:
                lungime_maxima = lungime_lista
        for i in range(lungime_maxima):
            a.append(str(i))
        tree["columns"] = a
        tree.column("#0", width=150, minwidth=150, anchor=tk.W)
        tree.heading("#0", text="Site", anchor=tk.W)
        for col in a:
            tree.column(col, width=150, minwidth=150, anchor=tk.W)
            tree.heading(col, text=f"Keyword {int(col) + 1}", anchor=tk.W)
        for key, values in dataframe.iterrows():
            tree.insert("", "end", text=key, values=tuple(values))
        tree.pack(expand=True, fill=tk.BOTH)
        canvas_tabel.create_window((0, 0), window=frame_tabel_content, anchor='nw')
        canvas_tabel.update_idletasks()
        canvas_tabel.configure(scrollregion=canvas_tabel.bbox("all"))
        canvas_tabel.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        scrollbar_x.pack(side=tk.BOTTOM, fill=tk.X)

        tabel_displayed = True
        wordcloud_displayed = False
        canvas_wordcloud.pack_forget()

# Crearea ferestrei principale
root = tk.Tk()
root.title("Proiect Lp3")
root.geometry("1000x800")
wordcloud_displayed = False
tabel_displayed = False

# Frame pentru butoane
button_frame = ttk.Frame(root)
button_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nw")

# Frame pentru afișare
frame_display = ttk.Frame(root, width=800, height=800)
frame_display.grid(row=0, column=1, padx=10, pady=10, rowspan=2, sticky="nsew")

# Configurarea grilei
root.grid_columnconfigure(1, weight=1)
root.grid_rowconfigure(1, weight=1)

# Canvas pentru word cloud
canvas_wordcloud = tk.Canvas(frame_display, width=800, height=800)
canvas_wordcloud.pack_forget()

# Frame pentru tabel
frame_tabel = ttk.Frame(frame_display)
frame_tabel.pack(expand=True, fill=tk.BOTH)

# Butoane pentru generarea word cloud și afișarea tabelului
button_generate = ttk.Button(button_frame, text="WordCloud", command=on_generate_button_click)
button_generate.pack(pady=10)
button_tabel = ttk.Button(button_frame, text="Tabel", command=afiseaza_tabel)
button_tabel.pack(pady=10)

# Rularea interfeței grafice
root.mainloop()

# Golește fișierul rezultate.txt la sfârșitul execuției
x = open("../rezultate.txt", "w")
x.close()
