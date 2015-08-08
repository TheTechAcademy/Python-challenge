__author__ = 'ColeDixon'

# Edited by Cory Phigler 8/07-08/2015

from tkinter import *
from tkinter import ttk

# Added all these def's and moved all the Gui outside of the class

class Calc():

    def __init__(self):
        
        total = 0
        self.current = ""
        self.new_num = True
        self.op_pending = False
        self.op = ""
        self.eq = False

    def num_press(self, num):
        self.eq = False
        temp = num_entry.get()
        temp2 = str(num)      
        if self.new_num:
            self.current = temp2
            self.new_num = False
        else:
            if temp2 == '.':
                if temp2 in temp:
                    return
            self.current = temp + temp2
        self.display(self.current)        
    
    def calc_total(self):
        self.eq = True
        self.current = float(self.current)
        if self.op_pending == True:
            self.do_sum()
        else:
            self.total = float(text_box.get())

    def display(self, value):
            num_entry.delete(0, END)
            num_entry.insert(0, value)

    def do_sum(self):
        if self.op == "add":
            self.total += self.current
        if self.op == "minus":
            self.total -= self.current
        if self.op == "times":
            self.total *= self.current
        if self.op == "divide":
            self.total /= self.current
        self.new_num = True
        self.op_pending = False
        self.display(self.total)

    def operation(self, op): 
        self.current = float(self.current)
        if self.op_pending:
            self.do_sum()
        elif not self.eq:
            self.total = self.current
        self.new_num = True
        self.op_pending = True
        self.op = op
        self.eq = False

    def cancel(self):
        self.eq = False
        self.current = "0"
        self.display(0)
        self.new_num = True

sum1 = Calc()
root = Tk()
calc = Frame(root)
calc.grid()
               
# changed everything to grid. Changed master to root

#MASTER SETTINGS
root.title('CALCULATOR')
root.resizable(False, False)

#HEADER
header_frame = ttk.Frame(root)
header_frame.grid()

ttk.Label(header_frame, text = 'Python Calculator').grid(row = 0, column = 2, sticky = 'e')
input = ttk.Label(header_frame).grid(row = 1, column = 0, columnspan = 4)
num_entry = ttk.Entry(input)
num_entry.grid(padx = 5, pady = 5)
num_entry.insert(0, "0")

#SEPARATOR
separator = ttk.Frame(height = 2, relief = SUNKEN)
separator.grid(row = 3, padx = 5, pady = 5, sticky="ew")

#PANEL
panel = ttk.Frame(root)
panel.grid()

#NUMBER BUTTONS
one = ttk.Button(panel, text = '1', width = 3, command = lambda: sum1.num_press(1))
one.grid(row = 3, column = 0, padx = 2, pady = 1)
two = ttk.Button(panel, text = '2', width = 3, command = lambda: sum1.num_press(2))
two.grid(row = 3, column = 1, padx = 2, pady = 1)
three = ttk.Button(panel, text = '3', width = 3, command = lambda: sum1.num_press(3))
three.grid(row = 3, column = 2, padx = 2, pady = 1)
four = ttk.Button(panel, text = '4', width = 3, command = lambda: sum1.num_press(4))
four.grid(row = 4, column = 0, padx = 2, pady = 1) # changed but should not have any effect?
five = ttk.Button(panel, text = '5', width = 3, command = lambda: sum1.num_press(5))
five.grid(row = 4, column = 1, padx = 2, pady = 1)
six = ttk.Button(panel, text = '6', width = 3, command = lambda: sum1.num_press(6))
six.grid(row = 4, column = 2, padx = 2, pady = 1)
seven = ttk.Button(panel, text = '7', width = 3, command = lambda: sum1.num_press(7))
seven.grid(row = 5, column = 0, padx = 2, pady = 1)
eight = ttk.Button(panel, text = '8', width = 3, command = lambda: sum1.num_press(8))
eight.grid(row = 5, column = 1, padx = 2, pady = 1)
nine = ttk.Button(panel, text = '9', width = 3, command = lambda: sum1.num_press(9)) # changed to conform to width
nine.grid(row = 5, column = 2, padx = 2, pady = 1) # change from pack to grid
zero = ttk.Button(panel, text = '0', width = 9, command = lambda: sum1.num_press(0)) # changed to conform to Clear button
zero.grid(row = 6, column = 0, columnspan = 2, padx = 2, pady = 1) # changed colspan to columnspan
dec = ttk.Button(panel, text = '.', width = 3, command = lambda: sum1.num_press("."))
dec.grid(row = 6, column = 2, padx = 2, pady = 1)

#OPERATOR BUTTONS
add = ttk.Button(panel, text = '+', width = 4, command = lambda: sum1.operation("add"))
add.grid(row = 3, column = 3, padx = 5, pady = 1)
sub = ttk.Button(panel, text = '-', width = 4, command = lambda: sum1.operation("minus"))
sub.grid(row = 4, column = 3, padx =5, pady = 1)
multi = ttk.Button(panel, text = '*', width = 4, command = lambda: sum1.operation("times"))
multi.grid(row = 5, column = 3, padx = 5, pady = 1)
div = ttk.Button(panel, text = '/', width = 4, command = lambda: sum1.operation("divide"))
div.grid(row = 6, column = 3, padx = 5, pady = 1)
equal = ttk.Button(panel, text = '=', width = 10, command = sum1.calc_total)
equal.grid(row = 7, column = 2, columnspan = 2, padx = 2, pady = 1)
clear = ttk.Button(panel, text = 'CLEAR', width = 9, command=sum1.cancel)
clear.grid(row = 7, column = 0, columnspan = 2, padx = 2, pady = 1)      

    
root.mainloop()     
'''
def main():
    root = Tk()
    Calculator(root)
    root.mainloop()

if __name__ == "__main__": main()
'''
