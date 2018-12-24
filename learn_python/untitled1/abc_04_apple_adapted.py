#输入苹果的单价
price = float(input("苹果的价格："))
#输入苹果的重量
weight = float(input("苹果的重量："))
#计算总金额
money = price * weight
print("总金额",money)

#该方法减少了中间变量的使用，节约空间