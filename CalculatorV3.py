# 计算新旧税率下的个人所得税
p = float(input('请输入税前月收入：'))
i = float(input('请输入五险一金：'))
new_rule = [(0, 0.03, 0),
            (3000, 0.1, 210),
            (12000, 0.2, 1410),
            (25000, 0.25, 2660),
            (35000, 0.3, 4410),
            (55000, 0.35, 7160),
            (80000, 0.45, 15160)
            ] # 新个税税率
old_rule = [(0, 0.03, 0),
            (1500, 0.1, 105),
            (4500, 0.2, 555),
            (9000, 0.25, 1005),
            (35000, 0.3, 2755),
            (55000, 0.35, 5505),
            (80000, 0.45, 13505)
            ] # 旧个税税率


def calctax(rule, threshold): # rule:对应个税税率 threshold:对应个税起征点
    pt = p - i - threshold # 应纳税所得额 = 税前收入 - 五险一金 - 起征点
    tax = 0 # 应纳税额 = 应纳税所得额 × 税率 - 速算扣除数
    for n in rule:
        if pt > n[0]:
            tax = pt*n[1] - n[2]
        else:
            break
    return tax


def main():
    old = calctax(old_rule, 3500)
    new = calctax(new_rule, 5000)
    print('税前月收入：{}'.format(p))
    print('五险一金：{}'.format(i))
    print('旧税率应纳税：{:.2f}元，税后收入：{:.2f}元'.format(old, p-i-old))
    print('新税率应纳税：{:.2f}元，税后收入：{:.2f}元'.format(new, p-i-new))


if __name__ == '__main__':
    main()
    input('按下任意键退出程序')
