def measure():

	print("测量开始...")
	temp = 39
	wetness = 50
	print("测量结束...")

	# result (temp,wetness)
	return temp,wetness			#此方法返回也是元组

result = measure()
print(result)

gl_temp,gl_wetness = measure()
#使用此方法，要保证变量个数和元组元素个数保持一致
print(gl_temp)
print(gl_wetness)