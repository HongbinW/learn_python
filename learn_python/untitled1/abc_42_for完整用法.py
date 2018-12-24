for num in [1,2,3]:
	print(num)

	if num == 6:
		break
else:
	#因为循环体内部break退出了循环，else下方的代码就不会被执行
	#应用环境：当搜索指定东西的时候，在找到东西的时候要直接退出， 而不是继续遍历；若找不到，则可在else中输出没有这个东西
	print("会执行吗？")

print("循环结束")