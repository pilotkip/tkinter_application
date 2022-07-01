import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
import os

class App(tk.Tk):
    app_name = "Tkinter Application"

    open_file = ""
    open_file_path = ""

    def set_title(self,title):
        self.title(title)

    def do_New(self):
        messagebox.showinfo(title="Alert", message="New")

    def do_Open_event(self,e):
        self.do_Open()

    def do_Open(self):
        my_filetypes = [('xml','.xml'), ('all files', '.*')]
        input_file = filedialog.askopenfilename(parent = self,
        initialdir=".",
        title="Please select a file:",
        filetypes=my_filetypes)
        if input_file != "":
            self.open_file_path, self.open_file = os.path.split(input_file)
            self.set_title(self.app_name + " - " + self.open_file)
    
    def do_Save_event(self,e):
        self.do_Save()

    def do_Save(self):
        if self.open_file == "":
            self.do_SaveAs()
            return

    def do_SaveAs_event(self,e):
        self.do_SaveAs()

    def do_SaveAs(self):
        my_filetypes = [('XML', '.xml')]
        save_file = filedialog.asksaveasfilename(
            initialdir=".",
            title="Please select a file name for saving:",
            filetypes=my_filetypes
        )
        if save_file != "":
            (self.open_file_path, self.open_file) = os.path.split(save_file)
            self.set_title(self.app_name + " - " + self.open_file)



    def __init__(self):
        super().__init__()
        self.geometry('800x600')
        self.option_add('*tearOff', False)
        self.set_title("Tkinter Application")
        #How should grid things expand when this window expands?
        self.columnconfigure(0,weight=1)
        self.rowconfigure(0,weight=1)

        menubar = tk.Menu(self)
        self['menu'] = menubar
        menu_file = tk.Menu(menubar)
        menubar.add_cascade(menu=menu_file, label='File')
        menu_file.add_command(label='New',command=self.do_New)
        menu_file.add_command(label='Open...',command=self.do_Open, accelerator="Ctrl+O")
        menu_file.add_command(label='Save',command=self.do_Save, accelerator="Ctrl+S")
        menu_file.add_command(label='Save as...',command=self.do_SaveAs, accelerator="Ctrl+Shift+S")
        menu_file.add_separator()
        menu_file.add_command(label='Exit', command=exit, underline=1, accelerator="Ctrl+Q")

        menu_file.bind_all("<Control-q>", exit)
        menu_file.bind_all("<Control-o>", self.do_Open_event)
        menu_file.bind_all("<Control-s>", self.do_Save_event)
        menu_file.bind_all("<Control-Shift-S>", self.do_SaveAs_event)

        self.frame = ttk.Frame(self)
        self.frame.rowconfigure(0, weight=1)
        self.frame.columnconfigure(0, weight=1)

        self.frame.grid(row=0, column=0, sticky=tk.N + tk.S + tk.E + tk.W)

        self.canvas = tk.Canvas(self.frame, bg='#ffffff', scrollregion=(0,0,1000,1000))
        self.canvas.grid(row=0, column=0, sticky=tk.N + tk.S + tk.E + tk.W)

        self.scroll_x = ttk.Scrollbar(self.frame, orient="horizontal", command=self.canvas.xview)
        self.scroll_x.grid(row=1, column=0, sticky=tk.E + tk.W)
        self.scroll_y = ttk.Scrollbar(self.frame, orient="vertical", command=self.canvas.yview)
        self.scroll_y.grid(row=0, column=1, sticky=tk.N + tk.S)

        self.canvas.configure(yscrollcommand=self.scroll_y.set, xscrollcommand=self.scroll_x.set)
        self.canvas.create_oval(200, 200, 220, 220, fill="blue")

        

if __name__ == "__main__":
    myapp = App()
    myapp.mainloop()

