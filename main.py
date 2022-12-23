"""
                                        GUI калькулятор на библеотеке TKINTER
                                                Version: 1.2
"""

import tkinter as tk

window = tk.Tk()
window.title('CALC')
window.geometry('460x595')
window['bg'] = '#444'
window.resizable(width=False, height=False)

n = ['x**2', '//', 'C', '<<', '1', '2', '3', '+', '4', '5', '6', '-', '7', '8', '9', '*', '.', '0', '=', '/']
oper = ['-', '+', '/', '*', '//', '**']
nums = [str(i) for i in range(10)]
num = 0
frame_1 = tk.Frame(master=window, bg='#444', height=2)
frame_1.pack(pady=(5, 0))

frame_2 = tk.Frame(master=window, bg='#444')
frame_2.pack()

input_val = tk.Entry(master=frame_1, font=('', 40), width=15)
input_val.grid(row=0, pady=10, padx=5)

def fn(value_text) -> str:
    if '+' in value_text:
        a, b = map(int, value_text.split('+'))
        return a + b
    elif '-' in value_text and value_text[0] != '-':
        a, b = map(int, value_text.split('-'))
        return a - b
    elif '**' in value_text:
        a, b = map(int, value_text.split('**'))
        return a ** b
    elif '//' in value_text:
        a, b = map(int, value_text.split('//'))
        return a // b
    elif '*' in value_text:
        a, b = map(int, value_text.split('*'))
        return a * b
    elif '/' in value_text:
        a, b = map(int, value_text.split('/'))
        if '0' not in [a, b]:
            return a / b
        else:
            return '0'


def check_is_operator(val):
    if val[-1] in nums:
        get_rez = 0
        if val[0] == '-':
            text_val = val[1:]
        else:
            text_val = val

        for o in oper:
            get_rez += text_val.count(o)
            if get_rez:
                input_val.delete(0, tk.END)
                input_val.insert(0, fn(val))
                break

def insert_simbol(simbol):
    if simbol in ['clr', 'clr_one']:
        match simbol:
            case 'clr_one':
                input_val.delete(len(input_val.get())-1)
            case 'clr':
                input_val.delete(0, tk.END)
    elif simbol in oper:
        val = input_val.get()
        if not val:
            if simbol == '-':
                input_val.insert(0, simbol)
        else:
            if val[-1] in nums:
                check_is_operator(val=val)
                input_val.insert(tk.END, simbol)
            elif val[-1] in oper and len(val) >= 2:
                if val[-1] in oper:
                    if val[-2] in oper:
                        input_val.delete(len(val)-2, tk.END)
                        input_val.insert(tk.END, simbol)
                    else:
                        input_val.delete(len(val) - 1)
                        input_val.insert(tk.END, simbol)
    elif simbol in ['=']:
        check_is_operator(val=input_val.get())
    elif simbol in ['.']:
        ...
    else:
        input_val.insert(tk.END, simbol)


btn = tk.Button(master=frame_2, text=f'{n[0]}', bg='#227', fg='#fff', font=('', 15), width=8, height=3,
                command=lambda: insert_simbol(f'**'))
btn.grid(row=0, column=0, padx=5, pady=5)
btn = tk.Button(master=frame_2, text=f'{n[1]}', bg='#227', fg='#fff', font=('', 15), width=8, height=3,
                command=lambda: insert_simbol(f'//'))
btn.grid(row=0, column=1, padx=5, pady=5)
btn = tk.Button(master=frame_2, text=f'{n[2]}', bg='#733', fg='#fff', font=('', 15), width=8, height=3,
                command=lambda: insert_simbol(f'clr'))
btn.grid(row=0, column=2, padx=5, pady=5)
btn = tk.Button(master=frame_2, text=f'{n[3]}', bg='#633', fg='#fff', font=('', 15), width=8, height=3,
                command=lambda: insert_simbol(f'clr_one'))
btn.grid(row=0, column=3, padx=5, pady=5)

btn = tk.Button(master=frame_2, text=f'{n[4]}', bg='#666', fg='#fff', font=('', 15), width=8, height=3,
                command=lambda: insert_simbol(f'{n[4]}'))
btn.grid(row=1, column=0, padx=5, pady=5)
btn = tk.Button(master=frame_2, text=f'{n[5]}', bg='#666', fg='#fff', font=('', 15), width=8, height=3,
                command=lambda: insert_simbol(f'{n[5]}'))
btn.grid(row=1, column=1, padx=5, pady=5)
btn = tk.Button(master=frame_2, text=f'{n[6]}', bg='#666', fg='#fff', font=('', 15), width=8, height=3,
                command=lambda: insert_simbol(f'{n[6]}'))
btn.grid(row=1, column=2, padx=5, pady=5)
btn = tk.Button(master=frame_2, text=f'{n[7]}', bg='#227', fg='#fff', font=('', 15), width=8, height=3,
                command=lambda: insert_simbol(f'{n[7]}'))
btn.grid(row=1, column=3, padx=5, pady=5)

btn = tk.Button(master=frame_2, text=f'{n[8]}', bg='#666', fg='#fff', font=('', 15), width=8, height=3,
                command=lambda: insert_simbol(f'{n[8]}'))
btn.grid(row=2, column=0, padx=5, pady=5)
btn = tk.Button(master=frame_2, text=f'{n[9]}', bg='#666', fg='#fff', font=('', 15), width=8, height=3,
                command=lambda: insert_simbol(f'{n[9]}'))
btn.grid(row=2, column=1, padx=5, pady=5)
btn = tk.Button(master=frame_2, text=f'{n[10]}', bg='#666', fg='#fff', font=('', 15), width=8, height=3,
                command=lambda: insert_simbol(f'{n[10]}'))
btn.grid(row=2, column=2, padx=5, pady=5)
btn = tk.Button(master=frame_2, text=f'{n[11]}', bg='#227', fg='#fff', font=('', 15), width=8, height=3,
                command=lambda: insert_simbol(f'{n[11]}'))
btn.grid(row=2, column=3, padx=5, pady=5)

btn = tk.Button(master=frame_2, text=f'{n[12]}', bg='#666', fg='#fff', font=('', 15), width=8, height=3,
                command=lambda: insert_simbol(f'{n[12]}'))
btn.grid(row=3, column=0, padx=5, pady=5)
btn = tk.Button(master=frame_2, text=f'{n[13]}', bg='#666', fg='#fff', font=('', 15), width=8, height=3,
                command=lambda: insert_simbol(f'{n[13]}'))
btn.grid(row=3, column=1, padx=5, pady=5)
btn = tk.Button(master=frame_2, text=f'{n[14]}', bg='#666', fg='#fff', font=('', 15), width=8, height=3,
                command=lambda: insert_simbol(f'{n[14]}'))
btn.grid(row=3, column=2, padx=5, pady=5)
btn = tk.Button(master=frame_2, text=f'{n[15]}', bg='#227', fg='#fff', font=('', 15), width=8, height=3,
                command=lambda: insert_simbol(f'{n[15]}'))
btn.grid(row=3, column=3, padx=5, pady=5)

btn = tk.Button(master=frame_2, text=f'{n[16]}', bg='#666', fg='#fff', font=('', 15), width=8, height=3,
                command=lambda: insert_simbol(f'{n[16]}'))
btn.grid(row=4, column=0, padx=5, pady=5)
btn = tk.Button(master=frame_2, text=f'{n[17]}', bg='#666', fg='#fff', font=('', 15), width=8, height=3,
                command=lambda: insert_simbol(f'{n[17]}'))
btn.grid(row=4, column=1, padx=5, pady=5)
btn = tk.Button(master=frame_2, text=f'{n[18]}', bg='#272', fg='#fff', font=('', 15), width=8, height=3,
                command=lambda: insert_simbol(f'{n[18]}'))
btn.grid(row=4, column=2, padx=5, pady=5)
btn = tk.Button(master=frame_2, text=f'{n[19]}', bg='#227', fg='#fff', font=('', 15), width=8, height=3,
                command=lambda: insert_simbol(f'{n[19]}'))
btn.grid(row=4, column=3, padx=5, pady=5)


window.mainloop()

