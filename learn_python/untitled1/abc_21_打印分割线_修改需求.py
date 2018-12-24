#对于新需求，只需调用之前的函数
#避免了对原来已完成函数的修改
def print_line(char,num1):
	print(char * num1)
def print_lines(char,num1):
	"""打印多行分割线

	:param char:分割线使用的分割字符
	:param num1:分割线重复的次数
	"""
	row = 0
	while row<5:
		print_line(char, num1)
		row += 1


print("-"*50)