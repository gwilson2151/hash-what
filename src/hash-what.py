from tkinter import Tk, ttk, filedialog, N, E, S, W
from model import sha256_calculator

def getFileName():
    filename = filedialog.askopenfilename()
    file_label.configure(text=filename)
    calculate = sha256_calculator(filename)
    hash = calculate()
    result_label.configure(text=hash)

root = Tk()
root.title('hash-what')
mainframe = ttk.Frame(root, padding="5 5 15 15")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

file_button = ttk.Button(mainframe, text="Select File...", command=getFileName)
file_button.grid(column=1, row=1, sticky=(W))
file_label = ttk.Label(mainframe, text='')
file_label.grid(column=2, row=1, sticky=(W))

sha256_label = ttk.Label(mainframe, text='SHA256')
sha256_label.grid(column=1, row=2, sticky=(W))

result_label = ttk.Label(mainframe, text='')
result_label.grid(column=2, row=2, sticky=(W))

for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

root.mainloop()
