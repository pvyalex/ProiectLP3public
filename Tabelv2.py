import tkinter as tk
from tkinter import ttk

# Definirea dicționarului
dict_sites = {
    'site1': ['keyword1', 'keyword2', 'keyword3', 'keyword2', 'keyword5', 'keyword7', 'keyword2', 'keyword5',
              'keyword7', 'keyword2', 'keyword5', 'keyword7', 'keyword2', 'keyword5', 'keyword7', 'keyword2',
              'keyword5', 'keyword7', 'keyword2', 'keyword5', 'keyword7', 'keyword2', 'keyword5', 'keyword7',
              'keyword2', 'keyword5', 'keyword7'],
    'site2': ['keyword2', 'keyword5', 'keyword7']
}


def create_table(canvas, frame, dictionary):

    for widget in frame.winfo_children():
        widget.destroy()

    col_count = 1
    ttk.Label(frame, text="Site", font=('Arial', 12, 'bold')).grid(row=0, column=0, padx=5, pady=5)
    for i in range(max(len(keywords) for keywords in dictionary.values())):
        ttk.Label(frame, text=f"Keyword {i + 1}", font=('Arial', 12, 'bold')).grid(row=0, column=col_count, padx=5,
                                                                                   pady=5)
        col_count += 1

    row_count = 1
    for site, keywords in dictionary.items():
        ttk.Label(frame, text=site, font=('Arial', 10)).grid(row=row_count, column=0, padx=5, pady=5)
        col_count = 1
        for keyword in keywords:
            ttk.Label(frame, text=keyword, font=('Arial', 10)).grid(row=row_count, column=col_count, padx=5, pady=5)
            col_count += 1
        row_count += 1

    frame.update_idletasks()
    canvas.config(scrollregion=canvas.bbox("all"))


def create_gui(dictionary):

    root = tk.Tk()
    root.title("Tabel 2 cuvinte cheie ")

    button_frame = ttk.Frame(root)
    button_frame.grid(row=0, column=0, sticky=(tk.W, tk.E))

    generate_button = ttk.Button(button_frame, text="Tabel",
                                 command=lambda: create_table(canvas, frame, dictionary))
    generate_button.pack(padx=10, pady=10)

    canvas = tk.Canvas(root)
    canvas.grid(row=1, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

    scrollbar_x = ttk.Scrollbar(root, orient=tk.HORIZONTAL, command=canvas.xview)
    scrollbar_x.grid(row=2, column=0, sticky=(tk.W, tk.E))

    canvas.configure(xscrollcommand=scrollbar_x.set)

    frame = ttk.Frame(canvas)
    canvas.create_window((0, 0), window=frame, anchor='nw')

    root.grid_rowconfigure(1, weight=1)
    root.grid_columnconfigure(0, weight=1)

    root.mainloop()


create_gui(dict_sites)
