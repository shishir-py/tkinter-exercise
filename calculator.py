
from tkinter import *
from tkinter import ttk


expressioon =""
def button_click(number):
    global expressioon
    expressioon = expressioon +str(number)
    result.set(expressioon)

def equal_press():
    try:
        global expressioon
        total_value = str(eval(expressioon))
        result.set(total_value)
        expressioon = ""
    except:
        expressioon = ""
        result.set(" error ")

def clear_press():
      
    global expressioon
    expressioon = ""
    result.set("")
if __name__ == "__main__":

    root =Tk()
    root.title("Calculator")
    root.geometry('320x250')
    # root.resizable(0,0)
    font_style =('Arial', 24 ,'bold')
    result = StringVar() 
    second_font = ("Arial",20)
    Result =Entry(root, width=45, borderwidth=5, textvariable=result)
    Result.grid(row=0, column=0, columnspan=4,pady=10,ipadx=5)
    button_frame = Frame(root)
    button_frame.grid(row=1,column=0, columnspan=4)
    button_1 = ttk.Button(button_frame, text='1',command=lambda:button_click(1))
    button_2 = ttk.Button(button_frame, text='2',command=lambda:button_click(2))
    button_3 = ttk.Button(button_frame, text='3',command=lambda:button_click(3))
    button_4 = ttk.Button(button_frame, text='4',command=lambda:button_click(4))
    button_5 = ttk.Button(button_frame, text='5',command=lambda:button_click(5))
    button_6 = ttk.Button(button_frame, text='6',command=lambda:button_click(6))
    button_7 = ttk.Button(button_frame, text='7',command=lambda:button_click(7))
    button_8 = ttk.Button(button_frame, text='8',command=lambda:button_click(8))
    button_9 = ttk.Button(button_frame, text='9',command=lambda:button_click(9))
    button_dot = ttk.Button(button_frame, text='.',command=lambda:button_click('.'))
    button_0 = ttk.Button(button_frame, text='0',command=lambda:button_click(0))
    button_equal =ttk.Button(button_frame, text='=',command=lambda:equal_press(),width=24)
    button_add =ttk.Button(button_frame, text='+',command=lambda:button_click("+"))
    button_div =ttk.Button(button_frame, text='/',command=lambda:button_click("/"))
    button_mul =ttk.Button(button_frame, text='x',command=lambda:button_click("*"))
    button_sub =ttk.Button(button_frame, text='-',command=lambda:button_click("-"))
    button_clear =ttk.Button(button_frame, text='AC',command=lambda:clear_press())
   



    button_clear.grid(row=1,column=0)  

    button_add.grid(row=1,column=3)



    button_1.grid(row=6,column=0)
    button_2.grid(row=6,column=1)
    button_3.grid(row=6,column=2)
    button_sub.grid(row=6,column=3)

    button_4.grid(row=5,column=0)
    button_5.grid(row=5,column=1)
    button_6.grid(row=5,column=2)
    button_mul.grid(row=5,column=3)

    button_7.grid(row=4,column=0)
    button_8.grid(row=4,column=1)
    button_9.grid(row=4,column=2)
    button_div.grid(row=4,column=3)

    button_dot.grid(row=7,column=0)
    button_0.grid(row=7,column=1)
    button_equal.grid(row=7,column=2,columnspan=2)
    root.mainloop()