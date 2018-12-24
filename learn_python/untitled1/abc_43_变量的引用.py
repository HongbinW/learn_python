def test(num):
	num +=1
	print("在函数内部%d对应的内存地址是%d"%(num ,id(num)))
	# return num

	result = "hello"
	print("函数要返回的数据的内存地址是%d"%id(result))
	return result
# pass

#1.定义一个数字的变量

a = 10
#数据的地址本质上就是一个数字
print("a变量保存数据的内存地址是%d"%id(a))


#2.调用test函数
r = test(a)
# print(a,b,id(b))
# print("当前a变量保存数据的内存地址是%d"%id(a))
print("%s的内存地址是%d"%(r,id(r)))
