"""
                                        GUI калькулятор на библеотеке TKINTER
                                                Version: 1.1
"""

import tkinter as tk

window = tk.Tk()
window.title('CALC')
window.geometry('460x595')
window['bg'] = '#444'
window.resizable(width=False, height=False)

n = ['x**2', '//', 'C', '<<', '1', '2', '3', '+', '4', '5', '6', '-', '7', '8', '9', '*', '.', '0', '=', '/']

num = 0
frame_1 = tk.Frame(master=window, bg='#444', height=2)
frame_1.pack(pady=(5, 0))

frame_2 = tk.Frame(master=window, bg='#444')
frame_2.pack()

input_val = tk.Label(master=frame_1, font=('', 28), width=20, height=2)
input_val.grid(row=0, pady=5, padx=5)

def fn(value_text) -> str:
    if '+' in value_text:
        a, b = list(map(int, value_text.split('+')))
        return a + b
    elif '-' in value_text:
        a, b = list(map(int, value_text.split('-')))
        return a - b
    elif '*' in value_text:
        a, b = list(map(int, value_text.split('*')))
        return a * b
    elif '/' in value_text:
        a, b = list(map(int, value_text.split('/')))
        return a / b
    elif '**' in value_text:
        a, b = list(map(int, value_text.split('**')))
        return a ** b
    elif '//' in value_text:
        a, b = list(map(int, value_text.split('//')))
        return a // b


def insert_simbol(simbol):
    text = input_val.cget('text')
    match simbol:
        case 'clr':
            input_val.config(text='')
        case 'clr_one':
            text = text[:-1]
            input_val.config(text=text)
        case '=':
            input_val.config(text=f'{input_val.cget("text")}{simbol}{fn(text)}')
        case _:
            if not text and simbol not in ['**', '//', '*', '+', '/']:
                input_val.config(text=f'{input_val.cget("text")}{simbol}')
            elif simbol in ['**', '//', '*', '+', '/'] and text[-1] in ['**', '//', '*', '+', '/']:
                if simbol == '-' and text[-1] == '-':
                    input_val.config(text=f'{input_val.cget("text")[:-1]}{simbol}')
                else:
                    input_val.config(text=f'{input_val.cget("text")[:-1]}{simbol}')
            else:
                input_val.config(text=f'{input_val.cget("text")}{simbol}')


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

btn = tk.Button(master=frame_2, text=f'{n[4]}', font=('', 15), width=8, height=3,
                command=lambda: insert_simbol(f'{n[4]}'))
btn.grid(row=1, column=0, padx=5, pady=5)
btn = tk.Button(master=frame_2, text=f'{n[5]}', font=('', 15), width=8, height=3,
                command=lambda: insert_simbol(f'{n[5]}'))
btn.grid(row=1, column=1, padx=5, pady=5)
btn = tk.Button(master=frame_2, text=f'{n[6]}', font=('', 15), width=8, height=3,
                command=lambda: insert_simbol(f'{n[6]}'))
btn.grid(row=1, column=2, padx=5, pady=5)
btn = tk.Button(master=frame_2, text=f'{n[7]}', bg='#227', fg='#fff', font=('', 15), width=8, height=3,
                command=lambda: insert_simbol(f'{n[7]}'))
btn.grid(row=1, column=3, padx=5, pady=5)

btn = tk.Button(master=frame_2, text=f'{n[8]}', font=('', 15), width=8, height=3,
                command=lambda: insert_simbol(f'{n[8]}'))
btn.grid(row=2, column=0, padx=5, pady=5)
btn = tk.Button(master=frame_2, text=f'{n[9]}', font=('', 15), width=8, height=3,
                command=lambda: insert_simbol(f'{n[9]}'))
btn.grid(row=2, column=1, padx=5, pady=5)
btn = tk.Button(master=frame_2, text=f'{n[10]}', font=('', 15), width=8, height=3,
                command=lambda: insert_simbol(f'{n[10]}'))
btn.grid(row=2, column=2, padx=5, pady=5)
btn = tk.Button(master=frame_2, text=f'{n[11]}', bg='#227', fg='#fff', font=('', 15), width=8, height=3,
                command=lambda: insert_simbol(f'{n[11]}'))
btn.grid(row=2, column=3, padx=5, pady=5)

btn = tk.Button(master=frame_2, text=f'{n[12]}', font=('', 15), width=8, height=3,
                command=lambda: insert_simbol(f'{n[12]}'))
btn.grid(row=3, column=0, padx=5, pady=5)
btn = tk.Button(master=frame_2, text=f'{n[13]}', font=('', 15), width=8, height=3,
                command=lambda: insert_simbol(f'{n[13]}'))
btn.grid(row=3, column=1, padx=5, pady=5)
btn = tk.Button(master=frame_2, text=f'{n[14]}', font=('', 15), width=8, height=3,
                command=lambda: insert_simbol(f'{n[14]}'))
btn.grid(row=3, column=2, padx=5, pady=5)
btn = tk.Button(master=frame_2, text=f'{n[15]}', bg='#227', fg='#fff', font=('', 15), width=8, height=3,
                command=lambda: insert_simbol(f'{n[15]}'))
btn.grid(row=3, column=3, padx=5, pady=5)

btn = tk.Button(master=frame_2, text=f'{n[16]}', font=('', 15), width=8, height=3,
                command=lambda: insert_simbol(f'{n[16]}'))
btn.grid(row=4, column=0, padx=5, pady=5)
btn = tk.Button(master=frame_2, text=f'{n[17]}', font=('', 15), width=8, height=3,
                command=lambda: insert_simbol(f'{n[17]}'))
btn.grid(row=4, column=1, padx=5, pady=5)
btn = tk.Button(master=frame_2, text=f'{n[18]}', bg='#272', fg='#fff', font=('', 15), width=8, height=3,
                command=lambda: insert_simbol(f'{n[18]}'))
btn.grid(row=4, column=2, padx=5, pady=5)
btn = tk.Button(master=frame_2, text=f'{n[19]}', bg='#227', fg='#fff', font=('', 15), width=8, height=3,
                command=lambda: insert_simbol(f'{n[19]}'))
btn.grid(row=4, column=3, padx=5, pady=5)


window.mainloop()
