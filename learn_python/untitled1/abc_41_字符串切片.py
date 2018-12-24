num_str = "0123456789"

#1.截取从2-5位置的字符串
print(num_str[2:6])		#包括位置5，因此要截到位置6

#2.截取从2-末尾的字符串
print((num_str[2:]))

#3.截取从开始-5位置的字符串
print(num_str[0:6])
print(num_str[:6])
#4.截取完整的字符串
print(num_str[:])

#5.从开始位置，每隔一个字符截取字符串
print(num_str[::2])		#从头到尾，每隔一个取一个，所以步长为2

#6.从索引1开始，每隔一个取一个
print(num_str[1::2])

#7.截取从2-(末尾-1)的字符串
print(num_str[2:-1])		#num_str[-1]=9

#8.截取字符串末尾两个字符
print(num_str[-2:])

#9.字符串的逆序（面试题）
print(num_str[::-1])