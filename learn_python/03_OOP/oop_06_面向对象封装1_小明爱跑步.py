"""
1.小明体中75.0公斤
2.小明每次跑步会减肥0.5公斤
3.小明每次吃东西体中会增加1公斤
"""
class Person:

	def __init__(self,name,weight):
		#self.属性 = 形参
		self.name = name
		self.weight = weight
	def __str__(self):
		return "我的名字叫 %s 体重是 %.2f 公斤"%(self.name,self.weight)
	def run(self):
		self.weight = self.weight - 0.5
	def eat(self):
		self.weight = self.weight + 1

xiaoming = Person("小明", 75)
xiaoming.run()
xiaoming.eat()
print(xiaoming)

"""
增加需求，小美也爱跑步
"""
xiaomei = Person("小美",45)
xiaomei.run()
xiaomei.eat()
print(xiaomei)

print(xiaoming)