from tkinter import *
import tkinter.messagebox
import math

# Global variables
radio_button = 'deg'
memory = None

# Window
root = Tk()
root.geometry('600x475')
root.title('GUI Calculator by Stanimir Yorgov')

# Display
display = Entry(root, font=("Helvetica", "40"), fg="#FFFFFF", bg="#181818", bd=10, justify=RIGHT, cursor="arrow", relief=SUNKEN)
display.insert(0, '0')
display.focus_set()
display.pack(expand=TRUE, fill=BOTH)

# Button functions
def button_click(button):
	temp = display.get()
	display.delete(0, END)
	if temp == '0' or temp == 'ERROR!':
		display.insert(0, str(button))
	else:
		display.insert(0, str(temp) + str(button))

def keyboard_click(*args):
	if display.get() == '0':
		display.delete(0, END)

def clear():
	display.delete(0, END)
	display.insert(0, '0')

def clear_entry(*args):
	temp = display.get()
	result = temp[:-1]
	if result == '' or result =='ERROR':
		result = '0'
	display.delete(0, END)
	display.insert(0, result)

def equals(*args):
	try:
		expression = display.get()
		result = eval(expression)
		result = round(result, 14)
		display.delete(0, END)
		display.insert(0, str(result))
	except:
		display.delete(0, END)
		display.insert(0, 'ERROR!')

def sin():
	try:
		x = float(display.get())
		global radio_button
		if radio_button == 'deg':
			result = math.sin(math.radians(x))
		else:
			result = math.sin(x)
		display.delete(0, END)
		display.insert(0, str(result))
	except:
		display.delete(0, END)
		display.insert(0, 'ERROR!')

def cos():
	try:
		x = float(display.get())
		global radio_button
		if radio_button == 'deg':
			result = math.cos(math.radians(x))
		else:
			result = math.cos(x)
		result = round(result, 14)
		display.delete(0, END)
		display.insert(0, str(result))
	except:
		display.delete(0, END)
		display.insert(0, 'ERROR!')

def tan():
	try:
		global radio_button
		x = float(display.get())
		if radio_button == 'deg':
			result = math.tan(math.radians(x))
		else:
			result = math.tan(x)
		display.delete(0, END)
		display.insert(0, str(result))
	except:
		display.delete(0, END)
		display.insert(0, 'ERROR!')

def radio_button_click(value):
	global radio_button
	radio_button = value

def sqrt():
	try:
		x = float(display.get())
		result = math.sqrt(x)
		display.delete(0, END)
		display.insert(0, str(result))
	except:
		display.delete(0, END)
		display.insert(0, 'ERROR!')

def log():
	try:
		x = float(display.get())
		result = math.log(x, 10)
		result = round(result, 14)
		display.delete(0, END)
		display.insert(0, str(result))
	except:
		display.delete(0, END)
		display.insert(0, 'ERROR!')

def exp():
	try:
		x = float(display.get())
		result = math.exp(x)
		display.delete(0, END)
		display.insert(0, str(result))
	except:
		display.delete(0, END)
		display.insert(0, 'ERROR!')

def pi():
	expression = display.get()
	display.delete(0, END)
	if expression == '0':
		display.insert(0, str(math.pi))
	else:
		display.insert(0, str(expression) + str(math.pi))

def factorial():
	try:
		x = float(display.get())
		result = math.factorial(x)
		display.delete(0, END)
		display.insert(0, str(result))
	except:
		display.delete(0, END)
		display.insert(0, 'ERROR!')

def memory_clear():
	global memory
	memory = None
	tkinter.messagebox.showinfo('Memory', 'Memory cleared!')

def memory_recall():
	global memory
	if memory != None:
		expression = display.get()
		display.delete(0, END)
		if expression == '0':
			display.insert(0, str(memory))
		else:
			display.insert(0, str(expression) + str(memory))
	else:
		tkinter.messagebox.showerror('Memory Error', 'Memory is empty!')

def memory_plus():
	try:
		global memory
		x = float(display.get())
		memory += x
		tkinter.messagebox.showinfo('Memory', 'Number stored in memory: {}'.format(memory))
	except:
		tkinter.messagebox.showerror('Memory Error', 'Check your values')

def memory_minus():
	try:
		global memory
		x = float(display.get())
		memory -= x
		tkinter.messagebox.showinfo('Memory', 'Number stored in memory: {}'.format(memory))
	except:
		tkinter.messagebox.showerror('Memory Error', 'Check your values')

def memory_set():
	try:
		global memory
		x = float(display.get())
		memory = x
		tkinter.messagebox.showinfo('Memory', 'Number stored in memory: {}'.format(memory))
	except:
		tkinter.messagebox.showerror('Memory Error', 'Check your values')

# Keyboard keys
display.bind("<Return>", equals)
display.bind("<Escape>", clear_entry)
display.bind("<Key-1>", keyboard_click)
display.bind("<Key-2>", keyboard_click)
display.bind("<Key-3>", keyboard_click)
display.bind("<Key-4>", keyboard_click)
display.bind("<Key-5>", keyboard_click)
display.bind("<Key-6>", keyboard_click)
display.bind("<Key-7>", keyboard_click)
display.bind("<Key-8>", keyboard_click)
display.bind("<Key-9>", keyboard_click)
display.bind("<Key-0>", keyboard_click)
display.bind("<Key-.>", keyboard_click)

# Button styles
button_style = {'bd':4, 'fg':'#FFFFFF', 'bg':'#282828','activeforeground':"#FFFFFF", 'activebackground':"#282828", 'font':('Helvetica', 16, 'bold'), 'width':'4', 'height':'1', 'padx':'10', 'pady':'10'}
special_style = {'bd':4, 'fg':'#FFFFFF', 'bg':'#161618','activeforeground':"#FFFFFF", 'activebackground':"#161618", 'font':('Helvetica', 16, 'bold'), 'width':'4', 'height':'1', 'padx':'10', 'pady':'10'}
numbers_style = {'bd':4, 'fg':'#FFFFFF', 'bg':'#3A3B3C','activeforeground':"#FFFFFF", 'activebackground':"#3A3B3C", 'font':('Helvetica', 16, 'bold'), 'width':'4', 'height':'1', 'padx':'10', 'pady':'10'}
radio_button_style = {'bd':2, 'fg':'#FFFFFF', 'bg':'#282828','activeforeground':"#FFFFFF", 'activebackground':"#3A3B3C", 'selectcolor':'#3A3B3C', 'font':('Helvetica', 16, 'bold'), 'width':'4', 'height':'1', 'padx':'10', 'pady':'10'}

# Button arangement
# row 1
row_1 = Frame(root)
row_1.pack(expand=TRUE, fill=BOTH)

c = StringVar(root)
c.set('deg')

radio_deg = Radiobutton(row_1, radio_button_style, text="Degrees", variable=c, value='deg', indicator = 0, command=lambda: radio_button_click(c.get()))
radio_deg.pack(side=LEFT, expand=TRUE, fill=BOTH)
radio_rad = Radiobutton(row_1, radio_button_style, text="Radians", variable=c, value='rad', indicator = 0, command=lambda: radio_button_click(c.get()))
radio_rad.pack(side=LEFT, expand=TRUE, fill=BOTH)

# row 2
row_2 = Frame(root)
row_2.pack(expand=TRUE, fill=BOTH)

button_mc = Button(row_2, special_style, text="MC", command=memory_clear).pack(side=LEFT, expand=TRUE, fill=BOTH)
button_mr = Button(row_2, special_style, text="MR", command=memory_recall).pack(side=LEFT, expand=TRUE, fill=BOTH)
button_mp = Button(row_2, special_style, text="M+", command=memory_plus).pack(side=LEFT, expand=TRUE, fill=BOTH)
button_mm = Button(row_2, special_style, text="M-", command=memory_minus).pack(side=LEFT, expand=TRUE, fill=BOTH)
button_ms = Button(row_2, special_style, text="MS", command=memory_set).pack(side=LEFT, expand=TRUE, fill=BOTH)
button_c = Button(row_2, special_style, text="C", command=clear).pack(side=LEFT, expand=TRUE, fill=BOTH)
button_ce = Button(row_2, special_style, text="CE", command=clear_entry).pack(side=LEFT, expand=TRUE, fill=BOTH)

# row 3
row_3 = Frame(root)
row_3.pack(expand=TRUE, fill=BOTH)

button_sin = Button(row_3, button_style, text="sin", command=sin).pack(side=LEFT, expand=TRUE, fill=BOTH)
button_cos = Button(row_3, button_style, text="cos", command=cos).pack(side=LEFT, expand=TRUE, fill=BOTH)
button_tan = Button(row_3, button_style, text="tan", command=tan).pack(side=LEFT, expand=TRUE, fill=BOTH)
button_7 = Button(row_3, numbers_style, text="7", command=lambda: button_click(7)).pack(side=LEFT, expand=TRUE, fill=BOTH)
button_8 = Button(row_3, numbers_style, text="8", command=lambda: button_click(8)).pack(side=LEFT, expand=TRUE, fill=BOTH)
button_9 = Button(row_3, numbers_style, text="9", command=lambda: button_click(9)).pack(side=LEFT, expand=TRUE, fill=BOTH)
button_divide = Button(row_3, button_style, text="/", command=lambda: button_click('/')).pack(side=LEFT, expand=TRUE, fill=BOTH)

# row 4
row_4 = Frame(root)
row_4.pack(expand=TRUE, fill=BOTH)

button_pow_2 = Button(row_4, button_style, text="x^2", command=lambda: button_click('**2')).pack(side=LEFT, expand=TRUE, fill=BOTH)
button_pow_y = Button(row_4, button_style, text="x^y", command=lambda: button_click('**')).pack(side=LEFT, expand=TRUE, fill=BOTH)
button_10_pow_x = Button(row_4, button_style, text="10^x", command=lambda: button_click('10**')).pack(side=LEFT, expand=TRUE, fill=BOTH)
button_4 = Button(row_4, numbers_style, text="4", command=lambda: button_click(4)).pack(side=LEFT, expand=TRUE, fill=BOTH)
button_5 = Button(row_4, numbers_style, text="5", command=lambda: button_click(5)).pack(side=LEFT, expand=TRUE, fill=BOTH)
button_6 = Button(row_4, numbers_style, text="6", command=lambda: button_click(6)).pack(side=LEFT, expand=TRUE, fill=BOTH)
button_multiply = Button(row_4, button_style, text="*", command=lambda: button_click('*')).pack(side=LEFT, expand=TRUE, fill=BOTH)

# row 5
row_5 = Frame(root)
row_5.pack(expand=TRUE, fill=BOTH)

button_sqrt = Button(row_5, button_style, text="sqrt", command=sqrt).pack(side=LEFT, expand=TRUE, fill=BOTH)
button_log = Button(row_5, button_style, text="log", command=log).pack(side=LEFT, expand=TRUE, fill=BOTH)
button_exp = Button(row_5, button_style, text="exp", command=exp).pack(side=LEFT, expand=TRUE, fill=BOTH)
button_1 = Button(row_5, numbers_style, text="1", command=lambda: button_click(1)).pack(side=LEFT, expand=TRUE, fill=BOTH)
button_2 = Button(row_5, numbers_style, text="2", command=lambda: button_click(2)).pack(side=LEFT, expand=TRUE, fill=BOTH)
button_3 = Button(row_5, numbers_style, text="3", command=lambda: button_click(3)).pack(side=LEFT, expand=TRUE, fill=BOTH)
button_minus = Button(row_5, button_style, text="-", command=lambda: button_click('-')).pack(side=LEFT, expand=TRUE, fill=BOTH)

# row 6
row_6 = Frame(root)
row_6.pack(expand=TRUE, fill=BOTH)

button_mod = Button(row_6, button_style, text="mod", command=lambda: button_click('%')).pack(side=LEFT, expand=TRUE, fill=BOTH)
button_pi = Button(row_6, button_style, text="pi", command=pi).pack(side=LEFT, expand=TRUE, fill=BOTH)
button_factorial = Button(row_6, button_style, text="n!", command=factorial).pack(side=LEFT, expand=TRUE, fill=BOTH)
button_point = Button(row_6, button_style, text=".", command=lambda: button_click('.')).pack(side=LEFT, expand=TRUE, fill=BOTH)
button_0 = Button(row_6, numbers_style, text="0", command=lambda: button_click(0)).pack(side=LEFT, expand=TRUE, fill=BOTH)
button_equals = Button(row_6, button_style, text="=", command=equals).pack(side=LEFT, expand=TRUE, fill=BOTH)
button_plus = Button(row_6, button_style, text="+", command=lambda: button_click('+')).pack(side=LEFT, expand=TRUE, fill=BOTH)


root.mainloop()