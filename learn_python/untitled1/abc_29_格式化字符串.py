#格式化字符串后面的（）本质上就是元组
info_tuple = ("xiaoming",18,1.75)
# print("%s 年龄是 %d 身高是 %.2f"%("小明",18,1.75))
print("%s 年龄是 %d 身高是 %.2f"%info_tuple)

info_str = "%s 年龄是 %d 身高是 %.2f"%info_tuple	#元组与字符串的拼接

print(info_str)