def demo(num,num_list):
	print("函数开始")
	num += num
	num_list = num_list + num_list	#注意与num_list+=num_list区分
	print(num)
	print(num_list)
	print("函数完成")

gl_num = 9
gl_num_list = [1,2,3]
demo(gl_num,gl_num_list)
print(gl_num)
print(gl_num_list)
