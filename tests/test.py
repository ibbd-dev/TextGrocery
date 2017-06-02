# -*- coding: utf-8 -*-

# 测试文件
# Author: Alex
# Created Time: 2017年06月02日 星期五 11时15分12秒
from tgrocery import Grocery

train_src = [
    ('education', '名师指导托福语法技巧：名词的复数形式'),
    ('education', '中国高考成绩海外认可 是“狼来了”吗？'),
    ('sports', '图文：法网孟菲尔斯苦战进16强 孟菲尔斯怒吼'),
    ('sports', '四川丹棱举行全国长距登山挑战赛 近万人参与')
]

grocery = Grocery('sample')
grocery.train(train_src)
grocery.save()

print("*"*40)
new_grocery = Grocery('sample')
new_grocery.load()
res = new_grocery.test(train_src)
print(type(res))
print(res)
print(res.accuracy_labels)
print(res.show_result())

print("*"*40)
res = new_grocery.predict("考生必读：新托福写作考试评分标准")
print(res)
print(res.dec_values)
