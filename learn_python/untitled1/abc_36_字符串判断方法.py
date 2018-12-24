#1.判断空白字符
space_str = "  \t\n\r"

print(space_str.isspace())	#不仅只检测是否为空格，而是是否为空字符

#2.判断字符串中是否只包含数字
#1>都不能判断小数

num_str = "一千零一"

print(num_str)
print(num_str.isdecimal())	#单纯的阿拉伯数字
print(num_str.isdigit())	#⑴ \u00b2像这种键盘不能直接输入的也可以
print(num_str.isnumeric())	#还可以判断中文，一个比一个高级
