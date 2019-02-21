from tkinter import Tk, ttk, filedialog, N, E, S, W
from hashlib import sha256

filename = ''
def getFileName():
    global filename
    filename = filedialog.askopenfilename()
    file_label.configure(text=filename)

def calc_sha256(path):
    sha256_hash = sha256()
    with open(path, 'rb') as file_desc:
        for byte_block in iter(lambda: file_desc.read(4096), b""):
            sha256_hash.update(byte_block)
    result_label.configure(text=sha256_hash.hexdigest())

root = Tk()
root.title('hash-what')
mainframe = ttk.Frame(root, padding="5 5 15 15")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

file_button = ttk.Button(mainframe, text="Select File...", command=getFileName)
file_button.grid(column=1, row=1)
file_label = ttk.Label(mainframe, text=filename)
file_label.grid(column=2, row=1, sticky=(W))

sha256_button = ttk.Button(mainframe, text="SHA256", command=lambda: calc_sha256(filename))
sha256_button.grid(column=1, row=2)

result_label = ttk.Label(mainframe, text='')
result_label.grid(column=2, row=2, sticky=(W))

for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

root.mainloop()
