#coding:utf-8
from tkinter import *
from tkinter import ttk

class Myapp():
    def __init__(self, fen) :
        self.hi = Label(fen, text="GUI Develeopment ")
        self.hi.pack()
        ttk.Button(fen, text="ME", command = self.me).pack()
        ttk.Button(fen, text="Your", command = self.your).pack()

    def me(self):
            self.hi.config(text = 'GUI Development ME ') 
    def your(self):
            self.hi.config(text= 'GUI Development Your')
def main():
    root = Tk()
    app = Myapp(root)
    root.mainloop()
if __name__ == "__main__":
    main()