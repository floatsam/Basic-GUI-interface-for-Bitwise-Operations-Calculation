#OR operation - Karthik
from tkinter import *
from XOR import *
def or_op(a = 0, b = 0) -> int:
    if(not (a.isnumeric()) or not (b.isnumeric())):
        return str("Invalid Input")
    return int(int(a) | int(b))

def or_show(a = 0, b = 0) -> int:
    if(not (a.isnumeric()) or not (b.isnumeric())):
        return str("Invalid Input")
    return str(bin(int(a) | int(b)))

def or_info(a = 0, b = 0):
    tr = Tk()
    a = str(a)
    b = str(b)
    tr.geometry("800x500+100+100")
    tr.resizable(False, False)
    if(not (a.isnumeric()) or not (b.isnumeric())):
        tr.destroy()
    x = StringVar(tr)
    y = StringVar(tr)
    z = StringVar(tr)
    x.set(convbinary(int(a)))
    y.set(convbinary(int(b)))
    z.set(convbinary(int(a) | int(b)))
    #print(x)
    gridx = Frame(tr)
    Label(gridx, text = 'More Information', pady = '10', padx = '10', relief = 'raised', fg = 'Red',bg = '#ADD8E9', font = ('helvetica', '35')).grid()
    gridx.pack(pady = '20')
    gridy = Frame(tr)
    Label(gridy, text = 'Number A : ', pady = '10', padx = '10', relief = 'ridge', fg = '#ADD8E9', font = ('helvetica', '25'), width = '15', height = '1').grid(column = 0, row = 0)
    Label(gridy, textvariable = x, pady = '10', padx = '10', relief = 'ridge', fg = '#ADD8E9', font = ('helvetica', '25'), width = '15', height = '1').grid(column = 1, row = 0)
    Label(gridy, text = 'Number B : ', pady = '10', padx = '10', relief = 'ridge', fg = '#ADD8E9', font = ('helvetica', '25'), width = '15', height = '1').grid(column = 0, row = 1)
    Label(gridy, textvariable = y, pady = '10', padx = '10', relief = 'ridge', fg = '#ADD8E9', font = ('helvetica', '25'), width = '15', height = '1').grid(column = 1, row = 1)
    Label(gridy, text = '   OR :        ', pady = '10', padx = '10', relief = 'ridge', fg = '#ADD8E9', font = ('helvetica', '25'), width = '15', height = '1').grid(column = 0, row = 2)
    Label(gridy, textvariable = z, pady = '10', padx = '10', relief = 'ridge', fg = '#ADD8E9', font = ('helvetica', '25'), width = '15', height = '1').grid(column = 1, row = 2)
    gridy.pack(padx = '50', pady = '90')
    tr.mainloop()

#or_info(20, 30)