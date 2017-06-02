# -*- coding: utf-8 -*-

# 测试文件
# Author: Alex
# Created Time: 2017年06月02日 星期五 11时15分12秒
from tgrocery import Grocery

grocery = Grocery('sample')
grocery.train('train_data.txt', delimiter=';')
grocery.save()

print("*"*40)
new_grocery = Grocery('sample')
new_grocery.load()
print(new_grocery.test('train_data.txt', delimiter=';'))

print("*"*40)
print(new_grocery.predict("考生必读：新托福写作考试评分标准"))
