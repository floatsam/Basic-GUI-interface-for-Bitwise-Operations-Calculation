#Tkinter/main driver code - Aniruddha

from XOR import *
from AND import *
from OR import *
from NOT import *

def XOR_2():
    x1 = str(xor_show(q1.get(), q2.get()))
    z.set(x1)
    x.set(bin(int(q1.get())))
    y1.set(bin(int(q2.get())))
    info.set("XOR operation is done to find difference between values, here each bit is operated on, which has 4 outcomes\n1 ^ 0 = 0\n0 ^ 1 = 0\n1 ^ 1 = 1\n0 ^ 0 = 1")

def AND_2():
    x1 = str(and_show(q1.get(), q2.get()))
    z.set(x1)
    x.set(bin(int(q1.get())))
    y1.set(bin(int(q2.get())))
    info.set("AND operation is done to find whether if both values are 1, here each bit is operated on, this has 4 outcomes\n1 & 0 = 0\n0 & 1 = 1\n1 & 1 = 1\n0 & 0 = 0")

def NOT_2():
    x1 = str(not_show(q1.get(), q2.get()))
    z.set(x1)
    x.set(bin(int(q1.get())))
    y1.set(bin(int(q2.get())))
    info.set("NOT operation is done to negate a value, here each bit is operated on and essentially forms the 1's complement of the same, this has only 2 outcomes\n~1 = 0\n~0 = 1")

def OR_2():
    x1 = str(or_show(q1.get(), q2.get()))
    z.set(x1)
    x.set(bin(int(q1.get())))
    y1.set(bin(int(q2.get())))
    info.set("OR operation is done to find if atleast 1 bit is 1, here each bit is operated on, which has only 4 outcomes\n1 | 0 = 1\n1 | 0 = 1\n0 | 0 = 0\n1 | 1 = 1")

choicer = int()

def chosen():
    global choicer
    global q1
    global q2
    #print(q1.get())
    #print(choicer)
    if(choicer == 1):
        xor_info(q1.get(), q2.get())
        #print("1")
    elif(choicer == 2):
        and_info(int(q1.get()), int(q2.get()))
    elif(choicer == 3):
        not_info(int(q1.get()), int(q2.get()))
    elif(choicer == 4):
        or_info(int(q1.get()), int(q2.get()))

def XOR_1():
    x1 = str(xor_op(q1.get(),q2.get()))
    m.set(x1)
    XOR_2()
    global choicer
    choicer = 1
    
def AND_1():
    x1 = str(and_op(q1.get(), q2.get()))
    m.set(x1)
    AND_2()
    global choicer
    choicer = 2

def NOT_1():
    x1 = (not_op(q1.get(), q2.get()))
    m.set(x1)
    NOT_2()
    global choicer
    choicer = 3

def OR_1():
    x1 = str(or_op(q1.get(), q2.get()))
    m.set(x1)
    OR_2()
    global choicer
    choicer = 4

root = Tk()
m = StringVar()
x = StringVar()
y1 = StringVar()
z = StringVar()
info = StringVar()
root.title("Calc")
root.geometry('1280x800+20+25')
frame = Frame(root)
#frame.grid()
Label(frame, text = "Bitwise Operations Calculator", font = ('Helvetica', 25), pady = '30', fg = 'Red').pack()
frame.pack()

frame1 = Frame(root)
Label(frame1, text = "Enter No. 1", font = ('Times New Roman', 20), pady = '15', padx = '80', fg = 'Blue').pack(side = 'left')
Label(frame1, text = "Enter No. 2", font = ('Times New Roman', 20), pady = '15', padx = '80', fg = 'Blue').pack(side = 'right')
frame1.pack()

frame2 = Frame(root)
q1 = Entry(frame2, bg = "#FFCCCB", relief = "raised", width = '30', font = ('Helvetica', '15'))
q2 = Entry(frame2, bg = "#FFCCCB", relief = "raised", width = '30', font = ('Helvetica', '15'))
q1.pack(side = 'left', pady = '25', padx = '50')
q2.pack(side = 'right', pady = '25', padx = '50')
frame2.pack()

frame3 = Frame(root)
Label(frame3, text = 'Choose your operation', pady = '15', fg = "Red", font = ('Times New Roman', '15')).pack(side = 'top')
frame3.pack()

frame4 = Frame(root)
Button(frame4, text = "XOR",bg = '#ADD8E6', padx = '25', pady = '20', command = XOR_1, height = ' 1', width = '10').pack(side = 'left', padx = '25')
Button(frame4, text = "AND",bg = '#ADD8E6', padx = '25', pady = '20', command = AND_1, height = ' 1', width = '10').pack(side = 'left', padx = '25')
Button(frame4, text = "OR",bg = '#ADD8E6', padx = '25', pady = '20', command = OR_1, height = ' 1', width = '10').pack(side = 'right', padx = '25')
Button(frame4, text = "NOT",bg = '#ADD8E6', padx = '25', pady = '20', command = NOT_1, height = ' 1', width = '10').pack(side = 'right', padx = '25')
frame4.pack(pady = '25')

resultfrm = Frame(root)
Label(resultfrm,text = 'Result := ', font = ('Helvetica', 25), padx = '20', pady = '20', fg = '#ADD8E9', bg = 'Red', width = '5').pack(side = 'left')
Label(resultfrm,textvariable = m, font = ('Helvetica', 25), padx = '20', pady = '20', fg = '#ADD8E9', bg = 'Red', width = '5').pack(side = 'right')
resultfrm.pack(side = 'left', padx = '25', pady = '15')

explainfrm = Frame(root)
Label(explainfrm, text = 'No. 1 :', padx = '10', pady = '10', font = ('helvetica', 15), bg = '#ADD8E9', width = '12').grid(column = 0, row = 0)
Label(explainfrm, textvariable = x, padx = '10', pady = '10', font = ('helvetica', 15), bg = '#ADD8E9', width = '12').grid(column = 0, row = 1)
Label(explainfrm, text = 'No. 2', padx = '10', pady = '10', font = ('helvetica', 15), bg = '#ADD8E9', width = '12').grid(column = 1, row = 0)
Label(explainfrm, textvariable = y1, padx = '10', pady = '10', font = ('helvetica', 15), bg = '#ADD8E9', width = '12').grid(column = 1, row = 1)
Label(explainfrm, text = 'Result', padx = '10', pady = '10', font = ('helvetica', 15), bg = '#ADD8E9', width = '12').grid(column = 2, row = 0)
Label(explainfrm, textvariable = z, padx = '10', pady = '10', font = ('helvetica', 15), bg = '#ADD8E9', width = '12').grid(column = 2, row = 1)
explainfrm.pack(side = 'right', padx = '15', pady = '15')


def infy():
    inf = Tk()
    inf.title("Explanation")
    inf.geometry("500x500+100+100")
    xc = info
    Label(inf, textvariable = xc, pady = '10', padx = '10',bg = '#ADD8E9', font = ('helvetica', 10)).pack(side = 'top')
    inf.resizable(False, False)
    inf.mainloop()


expl = Frame(root)
Button(expl, text = "Information", pady = '10', padx = '10',bg = '#ADD8E9', font = ('helvetica', 10), command = chosen, width = '15', height = '2').pack()
expl.pack(side = 'top',padx = '15', pady = '15')

root.resizable(True, True)
root.mainloop()