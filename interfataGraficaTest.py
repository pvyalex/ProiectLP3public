import tkinter as tk
def save_info():
    global text_var1, text_var2
    text_var1 = entry1.get()
    text_var2 = entry2.get()
    print("Variabila 1:", text_var1)
    print("Variabila 2:", text_var2)


root = tk.Tk()
root.title("Interfata Grafica 800x800")
root.geometry("800x800")


label1 = tk.Label(root, text="site ul 1")
label1.pack(pady=5)
entry1 = tk.Entry(root, width=30)
entry1.pack(pady=5)

label2 = tk.Label(root, text="site ul 2")
label2.pack(pady=5)
entry2 = tk.Entry(root, width=30)
entry2.pack(pady=5)

save_button = tk.Button(root, text="Salvează", command=save_info)

button1 = tk.Button(root, text="keywords_position")
button1.pack(pady=10)

button2 = tk.Button(root, text="keywords + avg monthly")
button2.pack(pady=10)

button3 = tk.Button(root, text="trafic")
button3.pack(pady=10)

root.mainloop()

save_button.pack(pady=10)

root.mainloop()
