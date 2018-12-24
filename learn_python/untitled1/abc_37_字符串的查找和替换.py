hello_str = "hello world"

#1.判断是否以指定字符串开始
print(hello_str.startswith("he"))	#注意区分大小写

#2.判断是否以指定字符串结束
print(hello_str.endswith("ld"))

#3.查找指定字符串
#indes同样可以查找指定的字符串在大字符串中的索引
print((hello_str.find("llo")))
print((hello_str.find("abc")))		#区分index，通过find不会报错，返回-1

#4.替换字符串
#replace方法执行完成后，会返回一个新的字符串
#但不会修改原有字符串的内容
print(hello_str.replace("world","python"))
print(hello_str)



