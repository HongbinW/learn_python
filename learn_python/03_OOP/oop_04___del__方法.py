class Cat:

	def __init__(self,new_name):
		self.name = new_name
		print("%s 来了"%self.name)

	def __del__(self):
		print("%s 去了"%self.name)

#tom是一个全局变量
tom = Cat("Tom")
print(tom.name)
#del关键字 可删除一个对象
# del tom
print("-"*50)