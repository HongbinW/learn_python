#输入苹果的单价
price_str = input("苹果的价格：")
#输入苹果的重量
weight_str = input("苹果的重量：")
#计算总金额
price = float(price_str)
weight = float(weight_str)  #注意由于两个字符串之间不能做乘法，所以要将其换做float型
money = price * weight

print("总金额",money)