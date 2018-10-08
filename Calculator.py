p = int(input('请输入税前月收入：'))
i = int(input('请输入五险一金：'))
def CalcOld():
    threshold = 3500
    pt = p - i - threshold
    tax = 0
    if pt > 0:
        if pt > 80000:
            tax = pt*0.45 - 13505
        elif pt > 55000:
            tax = pt*0.35 - 5505
        elif pt > 35000:
            tax = pt*0.3 - 2755
        elif pt > 9000:
            tax = pt*0.25 - 1005
        elif pt > 4500:
            tax = pt*0.2 - 555
        elif pt > 1500:
            tax = pt*0.1 - 105
        else:
            tax = pt*0.03
        return tax
    else:
        return tax

def CalcNew():
    threshold = 5000
    pt = p - i - threshold
    tax = 0
    if pt > 0:
        if pt > 80000:
            tax = pt*0.45 - 15160
        elif pt > 55000:
            tax = pt*0.35 - 7160
        elif pt > 35000:
            tax = pt*0.3 - 4410
        elif pt > 25000:
            tax = pt*0.25 - 2660
        elif pt > 12000:
            tax = pt*0.2 - 1410
        elif pt > 3000:
            tax = pt*0.1 - 210
        else:
            tax = pt*0.03
        return tax
    else:
        return tax

def main():
    old = CalcOld()
    new = CalcNew()
    print(f'税前月收入：{p}')
    print(f'五险一金：{i}')
    print(f'旧税率应纳税：{old}元，税后收入：{p-i-old}元')
    print(f'新税率应纳税：{new}元，税后收入：{p-i-new}元')

if __name__ == '__main__':
    main()
    print('Done!')


