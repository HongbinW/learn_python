class Cat:

	def eat(self):
		print("%s 爱吃鱼"% self.name)

	def drink(self):
		print("%s 要喝水" % self.name)


#创建对象
Tom = Cat()
Tom.name = "tom"	#该方法可以增加属性，但是不推荐
Tom.eat()
Tom.drink()

print(Tom)

#再创建一个猫对象
lazy_cat = Cat()
lazy_cat.name = "大懒猫"
lazy_cat.eat()
lazy_cat.drink()
print(lazy_cat)

lazy_cat2 = lazy_cat
print(lazy_cat2)