#个税计算器
import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext

def taxcalculation():
    income= answer1.get()
    riskgold=answer2.get()
#新税
    taxable=income-riskgold-5000
    if taxable>80000:
        tax=taxable*0.45-15160
    elif taxable>55000:
        tax = taxable * 0.35 - 7160
    elif taxable > 35000:
        tax = taxable * 0.30 - 4410
    elif taxable > 25000:
        tax = taxable * 0.25 - 2660
    elif taxable > 12000:
        tax = taxable * 0.20 - 1410
    elif taxable > 3000:
        tax = taxable * 0.10 - 210
    else:
        tax = taxable * 0.03 - 0
#旧税

    taxable2 = income - riskgold - 3500
    if taxable2 > 80000:
        tax2 = taxable2 * 0.45 - 13505
    elif taxable > 55000:
        tax2 = taxable2 * 0.35 - 5505
    elif taxable > 35000:
        tax2 = taxable2 * 0.30 - 2755
    elif taxable > 9000:
        tax2 = taxable2 * 0.25 - 1005
    elif taxable > 4500:
        tax2 = taxable2 * 0.20 - 555
    elif taxable > 1500:
        tax2 = taxable2 * 0.10 - 105
    else:
        tax2 = taxable2 * 0.03 - 0
    output.insert(tk.INSERT, '税前月收入: %.2f 元\n\n\
五险一金: %.2f 元\n\n旧税率应纳税: %.2f 元,\
税后收入: %.2f 元\n\n新税率应纳税: %.2f 元,\
税后收入: %.2f 元' % (income ,riskgold,tax2, income - riskgold - tax2,tax, income - riskgold - tax))

root = tk.Tk()
root.title("个税计算器")
window_left = ttk.Frame(root)
window_left.pack(ipadx=10, ipady=10, fill='y', side=tk.LEFT)
label = ttk.Label(window_left, text="请输入您的税前月收入：")
label.pack(padx=10, pady=10)
answer1=tk.DoubleVar()
entry1 = ttk.Entry(window_left, width=20, textvariable=answer1)
entry1.pack()
label2 = ttk.Label(window_left, text="请输入您的五险一金：")
label2.pack(padx=10, pady=10)
answer2 = tk.DoubleVar()
entry2 = ttk.Entry(window_left, width=20, textvariable=answer2)
entry2.pack()
btn = ttk.Button(window_left, width=20,text="点我就知道到手多少了！", command=taxcalculation)
btn.pack(padx=10, pady=10)
window_right = ttk.Frame(root)
window_right.pack(ipadx=10, ipady=10, fill='y', side=tk.RIGHT)
output = scrolledtext.ScrolledText(window_right, height=10, width=25, highlightbackground='black', highlightthickness=1)
output.pack(pady=30)

root.mainloop()