from tkinter import *
from tkinter import messagebox
import pyshorteners

class GUI(Tk):
    def __init__(self):
        super().__init__()
        self.title('URL Shortener')
        self.geometry('700x250')
        self.resizable(0, 0)
        self.config(bg='red')
        self.fg = 'white'
        self.bg= 'red'
        self.font = 'TimesNewRoman 25 bold'
        self.btnFont = 'calibri 17 bold'
        
    def Labels(self):
        Label(self, text='URL Shortener',justify='center', fg = self.fg, bg=self.bg, font=self.font).pack(pady=20)
        
    def Entries(self):
        self.text= Entry(self, width=50, font=self.font, justify='center', border=0)
        self.text.pack(pady=10)
    
    def Buttons(self):
        Button(self, text='Get Link', command=self.Shorten, font=self.btnFont).pack(pady=20)
    
    def Shorten(self):
        if self.text.get():
            url = self.text.get()
            
            s = pyshorteners.Shortener()
            newLink = s.tinyurl.short(url)
            
            self.text.delete(0, END)
            self.text.insert(0, f'{newLink}')
            self.text.config(state='readonly')
        else:
            messagebox.showwarning('Alert!', 'Insert link')
    
if __name__ == '__main__':
    root = GUI()
    root.Labels()
    root.Entries()
    root.Buttons()
    root.mainloop()