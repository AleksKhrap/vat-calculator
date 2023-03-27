from tkinter import END, Label, Tk, IntVar, Radiobutton, W, Entry, Button, messagebox


def show_help():
    """Выводит справку"""
    messagebox.showinfo("Помощь", "Вводите имеющиеся данные в поле 'Сумма:'")


def validate(n_v):
    """Проверяет, что введена цифра"""
    return n_v == "" or n_v.isnumeric()


def clear():
    """Очищает ввод"""
    n_entry.delete(0, END)


def calc():
    """Проводит вычисления"""
    a = nds.get()
    b = s.get()
    result = 0
    if a == 0 and b == 0:
        result = n.get() * 1.2
    if a == 1 and b == 0:
        result = n.get() * 1.1

    if a == 0 and b == 1:
        result = n.get() - (n.get() / 120 * 20)
    if a == 1 and b == 1:
        result = n.get() - (n.get() / 110 * 10)

    if a == 0 and b == 2:
        result = n.get() + (n.get() / 0.2)
    if a == 1 and b == 2:
        result = n.get() + (n.get() / 0.1)
    if n.get() == 0:
        messagebox.showinfo("Введите данные!")
    messagebox.showinfo("Результат", f"Сумма: {result}")



calculator = Tk()
x = (calculator.winfo_screenwidth() - calculator.winfo_reqwidth()) / 2
y = (calculator.winfo_screenheight() - calculator.winfo_reqheight()) / 2
calculator.wm_geometry("+%d+%d" % (x - 100, y - 50))
calculator.title("Калькулятор НДС")

Label(text="НДС %:").grid(row=0, column=0, sticky=W)
nds = IntVar()
nds.set(0)
Radiobutton(text='20%', variable=nds, value=0).grid(row=0, column=1, padx=5, pady=5, sticky=W)
Radiobutton(text='10%', variable=nds, value=1).grid(row=1, column=1, padx=5, pady=5, sticky=W)

Label(text="Способ вычисления:").grid(row=2, column=0, sticky=W)
s = IntVar()
s.set(0)
Radiobutton(text='Начислить НДС (прибавить НДС к сумме)', variable=s, value=0).grid(row=2, column=1, padx=5, pady=5,
                                                                                        sticky=W)
Radiobutton(text='Выделить НДС (вычесть НДС из суммы)', variable=s, value=1).grid(row=3, column=1, padx=5, pady=5,
                                                                                      sticky=W)
Radiobutton(text='Рассчитать сумму, зная НДС', variable=s, value=2).grid(row=4, column=1, padx=5, pady=5, sticky=W)

n = IntVar()
n.set('')
Label(text="Сумма:").grid(row=5, column=0, sticky=W)
reg = (calculator.register(validate), '%P')
n_entry = Entry(validate='key', validatecommand=reg, textvariable=n)
n_entry.grid(row=5, column=1, padx=5, pady=5, sticky=W)

Button(text="Помощь", command=show_help).grid(row=0, column=3, padx=5, pady=5, sticky=W)
Button(text="Очистить", command=clear).grid(row=5, column=3, padx=5, pady=5, sticky=W)
Button(text="Рассчитать", command=calc).grid(row=6, column=1, padx=5, pady=5, sticky=W)

calculator.mainloop()
