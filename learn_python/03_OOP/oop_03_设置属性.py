class Cat:

	def __init__(self,new_name):
		self.name = new_name
	def eat(self):
		print("%s 爱吃鱼"% self.name)

	def drink(self):
		print("%s 要喝水" % self.name)


#创建对象
Tom = Cat("tom")

Tom.eat()
Tom.drink()

lazy_cat = Cat("大懒猫")
lazy_cat.eat()
lazy_cat.drink()

