__author__ = 'ColeDixon'

from tkinter import *
from tkinter import ttk

class Calculator:

    def __init__(self, master):

        #MASTER SETTINGS
        master.title('CALCULATOR')
        master.resizable(False, False)

        #HEADER
        self.header_frame = ttk.Frame(master)
        self.header_frame.pack()

        ttk.Label(self.header_frame, text = 'Python Calculator').grid(row = 0, column = 2, sticky = 'e')
        self.input = ttk.Label(self.header_frame).grid(row = 1, column = 0, columnspan = 4)
        self.num_entry = ttk.Entry(self.input, justify = RIGHT)
        self.num_entry.pack(padx = 10, pady = 5)

        #SEPARATOR
        self.separator = ttk.Frame(height = 2, relief = SUNKEN)
        self.separator.pack(fill = X, padx = 5, pady = 5)

        #PANEL
        self.panel = ttk.Frame(master)
        self.panel.pack()

        #NUMBER BUTTONS
        self.one = ttk.Button(self.panel, text = '1', width = 3)
        self.one.grid(row = 3, column = 0, padx = 2, pady = 1)
        self.two = ttk.Button(self.panel, text = '2', width = 3)
        self.two.grid(row = 3, column = 1, padx = 2, pady = 1)
        self.three = ttk.Button(self.panel, text = '3', width = 3)
        self.three.grid(row = 3, column = 2, padx = 2, pady = 1)
        self.four = ttk.Button(self.panel, text = '4', width = 3)
        self.four.grid(row = 4, column = 0, padx = 2, pady = 1)
        self.five = ttk.Button(self.panel, text = '5', width = 3)
        self.five.grid(row = 4, column = 1, padx = 2, pady = 1)
        self.six = ttk.Button(self.panel, text = '6', width = 3)
        self.six.grid(row = 4, column = 2, padx = 2, pady = 1)
        self.seven = ttk.Button(self.panel, text = '7', width = 3)
        self.seven.grid(row = 5, column = 0, padx = 2, pady = 1)
        self.eight = ttk.Button(self.panel, text = '8', width = 3)
        self.eight.grid(row = 5, column = 1, padx = 2, pady = 1)
        self.nine = ttk.Button(self.panel, text = '9', width = 3)
        self.nine.grid(row = 5, column = 2, padx = 2, pady = 1)
        self.zero = ttk.Button(self.panel, text = '0', width = 8)
        self.zero.grid(row = 6, column = 0, columnspan = 2, padx = 2, pady = 1)
        self.dec = ttk.Button(self.panel, text = '.', width = 3)
        self.dec.grid(row = 6, column = 2, padx = 2, pady = 1)

        #OPERATOR BUTTONS
        self.add = ttk.Button(self.panel, text = '+', width = 4)
        self.add.grid(row = 3, column = 3, padx = 5, pady = 1)
        self.sub = ttk.Button(self.panel, text = '-', width = 4)
        self.sub.grid(row = 4, column = 3, padx =5, pady = 1)
        self.multi = ttk.Button(self.panel, text = '*', width = 4)
        self.multi.grid(row = 5, column = 3, padx = 5, pady = 1)
        self.div = ttk.Button(self.panel, text = '/', width = 4)
        self.div.grid(row = 6, column = 3, padx = 5, pady = 1)
        self.equal = ttk.Button(self.panel, text = '=', width = 10)
        self.equal.grid(row = 7, column = 2, columnspan = 2, padx = 2, pady = 1)
        self.clear = ttk.Button(self.panel, text = 'CLEAR', width = 9)
        self.clear.grid(row = 7, column = 0, columnspan = 2, padx = 2, pady = 1)

        #BIND CLICK EVENTS
        self.clear.bind('<1>', lambda e: self.clear_())
        self.one.bind('<1>', lambda e: self.callback(1))
        self.two.bind('<1>', lambda e: self.callback(2))
        self.three.bind('<1>', lambda e: self.callback(3))
        self.four.bind('<1>', lambda e: self.callback(4))
        self.five.bind('<1>', lambda e: self.callback(5))
        self.six.bind('<1>', lambda e: self.callback(6))
        self.seven.bind('<1>', lambda e: self.callback(7))
        self.eight.bind('<1>', lambda e: self.callback(8))
        self.nine.bind('<1>', lambda e: self.callback(9))
        self.zero.bind('<1>', lambda e: self.callback(0))
        self.dec.bind('<1>', lambda e: self.callback('.'))
        self.add.bind('<1>', lambda e: self.callback('+'))
        self.sub.bind('<1>', lambda e: self.callback('-'))
        self.multi.bind('<1>', lambda e: self.callback('*'))
        self.div.bind('<1>', lambda e: self.callback('/'))
        self.equal.bind('<1>', lambda e: self.math_())

    def clear_(self):
        self.num_entry.delete(0, 'end')

    def callback(self, number):
        self.num_entry.insert('end', number)

    def math_(self):
        try:
            result = eval(self.num_entry.get())
            self.clear_()
            self.num_entry.insert('end', result)
        except:
            self.clear_()
            self.num_entry.insert('end', "ERROR")



def main():
    root = Tk()
    Calculator(root)
    root.mainloop()

if __name__ == "__main__": main()
