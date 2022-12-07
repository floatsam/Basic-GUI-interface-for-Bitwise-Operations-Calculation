#XOR operation - Uday
from tkinter import *

def xor_op(a = 0, b = 0) -> int:
    if(not (a.isnumeric()) or not (b.isnumeric())):
        return str("Invalid Input")
    return int(int(a) ^ int(b))

def xor_show(a = 0, b = 0) -> int:
    if(not (a.isnumeric()) or not (b.isnumeric())):
        return str("Invalid Input")
    return str(bin(int(a) ^ int(b)))

def xor_info(a = 2, b = 3) -> None:
    c = convbinary(int(a) ^ int(b))
    a = convbinary(int(a))
    b = convbinary(int(b))
    tr = Tk()
    #print(a)
    #print(b)
    tr.geometry("800x500+100+100")
    tr.resizable(False, False)
    #if(not (a.isnumeric()) or not (b.isnumeric())):
    #    tr.destroy()
    x = StringVar(tr)
    y = StringVar(tr)
    z = StringVar(tr)
    x.set(a)
    y.set(b)
    z.set(c)
    #print(x)
    #print(y)
    gridx = Frame(tr)
    Label(gridx, text = 'More Information', pady = '10', padx = '10', relief = 'raised', fg = 'Red',bg = '#ADD8E9', font = ('helvetica', '35')).grid()
    gridx.pack(pady = '20')
    gridy = Frame(tr)
    Label(gridy, text = 'Number A : ', pady = '10', padx = '10', relief = 'ridge', fg = '#ADD8E9', font = ('helvetica', '25'), width = '15', height = '1').grid(column = 0, row = 0)
    Label(gridy, textvariable = x, pady = '10', padx = '10', relief = 'ridge', fg = '#ADD8E9', font = ('helvetica', '25'), width = '15', height = '1').grid(column = 1, row = 0)
    Label(gridy, text = 'Number B : ', pady = '10', padx = '10', relief = 'ridge', fg = '#ADD8E9', font = ('helvetica', '25'), width = '15', height = '1').grid(column = 0, row = 1)
    Label(gridy, textvariable = y, pady = '10', padx = '10', relief = 'ridge', fg = '#ADD8E9', font = ('helvetica', '25'), width = '15', height = '1').grid(column = 1, row = 1)
    Label(gridy, text = '   XOR :      ', pady = '10', padx = '10', relief = 'ridge', fg = '#ADD8E9', font = ('helvetica', '25'), width = '15', height = '1').grid(column = 0, row = 2)
    Label(gridy, textvariable = z, pady = '10', padx = '10', relief = 'ridge', fg = '#ADD8E9', font = ('helvetica', '25'), width = '15', height = '1').grid(column = 1, row = 2)
    gridy.pack(padx = '50', pady = '90')
    #tr.after(2, tr.update)
    tr.mainloop()

def convbinary(a = 0) -> str: #Aniruddha
    temp = a
    chr = str("")
    if(a == 0):
        return "0000 "
    while(temp):
        chr = chr + str(temp % 2)
        #print(temp % 2)
        temp = temp // 2
    if(len(chr) <= 3):
        chr = chr + "0"*(4 - len(chr))
    #print(chr)
    return chr[::-1]

#print(convbinary(1))
#xor_info(1, 1)