from tkinter import *
import tkinter.messagebox as messagebox


class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.creatwidgets()

    def creatwidgets(self):
        self.incomeLabel = Label(self, text='请输入税前月收入')
        self.incomeLabel.pack()
        self.incomeInput = Entry(self)
        self.incomeInput.pack()
        self.insuranceLabel = Label(self, text='请输入五险一金')
        self.insuranceLabel.pack()
        self.insuranceInput = Entry(self)
        self.insuranceInput.pack()
        self.alertButton = Button(self, text='计算', command=self.calculate)
        self.alertButton.pack()

    def calculate(self):
        income = float(self.incomeInput.get())
        insurance = float(self.insuranceInput.get())
        new_rule = [(0, 0.03, 0),
                    (3000, 0.1, 210),
                    (12000, 0.2, 1410),
                    (25000, 0.25, 2660),
                    (35000, 0.3, 4410),
                    (55000, 0.35, 7160),
                    (80000, 0.45, 15160)
                    ]  # 新个税税率
        old_rule = [(0, 0.03, 0),
                    (1500, 0.1, 105),
                    (4500, 0.2, 555),
                    (9000, 0.25, 1005),
                    (35000, 0.3, 2755),
                    (55000, 0.35, 5505),
                    (80000, 0.45, 13505)
                    ]  # 旧个税税率

        def calctax(rule, threshold):
            pt = income - insurance - threshold  # 应纳税所得额 = 税前收入 - 五险一金 - 起征点
            tax = 0  # 应纳税额 = 应纳税所得额 × 税率 - 速算扣除数
            for n in rule:
                if pt > n[0]:
                    tax = pt * n[1] - n[2]
                else:
                    break
            return tax

        old = calctax(old_rule, 3500)
        new = calctax(new_rule, 5000)
        messagebox.showinfo('计算结果', '''
        税前月收入：{}
        五险一金：{}
        旧税率应纳税：{:.2f}元，税后收入：{:.2f}元
        新税率应纳税：{:.2f}元，税后收入：{:.2f}元
        '''.format(income, insurance, old, income-insurance-old, new, income-insurance-new))


app = Application()
app.master.title('新税率税后收入计算器')
app.mainloop()
