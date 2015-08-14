__author__ = 'ColeDixon'

from tkinter import *
from tkinter import ttk

class Calculator:

    def PressOne(self,e):
        if self.state == 0:
            self.operand1 = self.operand1 * 10
            self.operand1 += 1
            self.num_entry.delete(0,END)
            self.num_entry.insert(END,self.operand1)
            print (self.operand1)
        else:
            self.operand2 = self.operand2 * 10
            self.operand2 += 1
            self.num_entry.delete(0,END)
            self.num_entry.insert(END,self.operand2)
            print (self.operand2)

    def PressTwo(self,e ):
        if self.state == 0:
            self.operand1 = self.operand1 * 10
            self.operand1 += 2
            self.num_entry.delete(0,END)
            self.num_entry.insert(END,self.operand1)
            print (self.operand1)
        else:
            self.operand2 = self.operand2 * 10
            self.operand2 += 2
            self.num_entry.delete(0,END)
            self.num_entry.insert(END,self.operand2)
            print (self.operand2)

    def PressThree(self,e ):
        if self.state == 0:
            self.operand1 = self.operand1 * 10
            self.operand1 += 3
            self.num_entry.delete(0,END)
            self.num_entry.insert(END,self.operand1)
            print (self.operand1)
        else:
            self.operand2 = self.operand2 * 10
            self.operand2 += 3
            self.num_entry.delete(0,END)
            self.num_entry.insert(END,self.operand2)
            print (self.operand2)

    def PressFour(self,e ):
        if self.state == 0:
            self.operand1 = self.operand1 * 10
            self.operand1 += 4
            self.num_entry.delete(0,END)
            self.num_entry.insert(END,self.operand1)
            print (self.operand1)
        else:
            self.operand2 = self.operand2 * 10
            self.operand2 += 4
            self.num_entry.delete(0,END)
            self.num_entry.insert(END,self.operand2)
            print (self.operand2)
    def PressFive(self,e ):
        if self.state == 0:
            self.operand1 = self.operand1 * 10
            self.operand1 += 5
            self.num_entry.delete(0,END)
            self.num_entry.insert(END,self.operand1)
            print (self.operand1)
        else:
            self.operand2 = self.operand2 * 10
            self.operand2 += 5
            self.num_entry.delete(0,END)
            self.num_entry.insert(END,self.operand2)
            print (self.operand2)
    def PressSix(self,e ):
        if self.state == 0:
            self.operand1 = self.operand1 * 10
            self.operand1 += 6
            self.num_entry.delete(0,END)
            self.num_entry.insert(END,self.operand1)
            print (self.operand1)
        else:
            self.operand2 = self.operand2 * 10
            self.operand2 += 6
            self.num_entry.delete(0,END)
            self.num_entry.insert(END,self.operand2)
            print (self.operand2)
    def PressSeven(self,e ):
        if self.state == 0:
            self.operand1 = self.operand1 * 10
            self.operand1 += 7
            self.num_entry.delete(0,END)
            self.num_entry.insert(END,self.operand1)
            print (self.operand1)
        else:
            self.operand2 = self.operand2 * 10
            self.operand2 += 7
            self.num_entry.delete(0,END)
            self.num_entry.insert(END,self.operand2)
            print (self.operand2)
    def PressEight(self,e ):
        if self.state == 0:
            self.operand1 = self.operand1 * 10
            self.operand1 += 8
            self.num_entry.delete(0,END)
            self.num_entry.insert(END,self.operand1)
            print (self.operand1)
        else:
            self.operand2 = self.operand2 * 10
            self.operand2 += 8
            self.num_entry.delete(0,END)
            self.num_entry.insert(END,self.operand2)
            print (self.operand2)
    def PressNine(self,e ):
        if self.state == 0:
            self.operand1 = self.operand1 * 10
            self.operand1 += 9
            self.num_entry.delete(0,END)
            self.num_entry.insert(END,self.operand1)
            print (self.operand1)
        else:
            self.operand2 = self.operand2 * 10
            self.operand2 += 9
            self.num_entry.delete(0,END)
            self.num_entry.insert(END,self.operand2)
            print (self.operand2)
    def PressZero(self,e ):
        if self.state == 0:
            self.operand1 = self.operand1 * 10
            self.num_entry.delete(0,END)
            self.num_entry.insert(END,self.operand1)
            print (self.operand1)
        else:
            self.operand2 = self.operand2 * 10
            self.num_entry.delete(0,END)
            self.num_entry.insert(END,self.operand2)
            print (self.operand2)
    def PressAdd(self,e ):
        self.state = 1
    def PressSub(self,e ):
        self.state = 2
    def PressMulti(self,e ):
        self.state = 3
    def PressDiv(self,e ):
        self.state = 4
    def PressClear(self,e ):
        self.state = 0
        self.operand1 = 0
        self.operand2 = 0
        self.num_entry.delete(0,END)
    def PressEqual(self,e ):
        if self.state == 1:
            result = self.operand1 + self.operand2
            self.num_entry.delete(0,END)
            self.num_entry.insert(END,result)
            print (result)
        elif self.state == 2:
            result = self.operand1 - self.operand2
            self.num_entry.delete(0,END)
            self.num_entry.insert(END,result)
            print (result)
        elif self.state == 3:
            result = self.operand1 * self.operand2
            self.num_entry.delete(0,END)
            self.num_entry.insert(END,result)
            print (result)
        elif self.state == 4:
            if self.operand2 == 0:
                result = "ERROR!!!"
            else:
                result = self.operand1 / self.operand2
            self.num_entry.delete(0,END)
            self.num_entry.insert(END,result)
            print (result)
        self.state = 0
        self.operand1 = 0
        self.operand2 = 0



    def __init__(self, master):

        self.operand1 = 0
        self.operand2 = 0
        self.state = 0

        #MASTER SETTINGS
        master.title('CALCULATOR')
        master.resizable(False, False)

        #HEADER
        self.header_frame = ttk.Frame(master)
        self.header_frame.pack()

        ttk.Label(self.header_frame, text = 'Python Calculator').grid(row = 0, column = 2, sticky = 'e')
        self.input = ttk.Label(self.header_frame).grid(row = 1, column = 0, columnspan = 4)
        self.num_entry = ttk.Entry(self.input, justify=RIGHT)
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
        self.nine = ttk.Button(self.panel, text = '9', width = 4)
        self.nine.grid(row = 5, column = 2, padx = 2, pady = 1)
        self.zero = ttk.Button(self.panel, text = '0', width = 3)
        self.zero.grid(row = 6, column = 0, padx = 2, pady = 1)
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
        self.one.bind('<Button-1>',self.PressOne)
        self.two.bind('<Button-1>',self.PressTwo)
        self.three.bind('<Button-1>',self.PressThree)
        self.four.bind('<Button-1>',self.PressFour)
        self.five.bind('<Button-1>',self.PressFive)
        self.six.bind('<Button-1>',self.PressSix)
        self.seven.bind('<Button-1>',self.PressSeven)
        self.eight.bind('<Button-1>',self.PressEight)
        self.nine.bind('<Button-1>',self.PressNine)
        self.zero.bind('<Button-1>',self.PressZero)
        self.add.bind('<Button-1>',self.PressAdd)
        self.sub.bind('<Button-1>',self.PressSub)
        self.multi.bind('<Button-1>',self.PressMulti)
        self.div.bind('<Button-1>',self.PressDiv)
        self.clear.bind('<Button-1>',self.PressClear)
        self.equal.bind('<Button-1>',self.PressEqual)


def main():
    root = Tk()
    Calculator(root)
    root.mainloop()

if __name__ == "__main__": main()
