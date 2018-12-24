class Cat:

	def eat(self):
		print("小猫爱吃鱼")

	def drink(self):
		print("小猫要喝水")


#创建对象
Tom = Cat()

Tom.eat()
Tom.drink()

print(Tom)	#以16进制显示内存地址

addr = id(Tom)
print("%x"%addr)